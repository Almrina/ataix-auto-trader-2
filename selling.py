import json
import requests

API_BASE_URL = "https://api.ataix.kz"
API_KEY = "key"
ORDERS_FILE = "orders.json"


def load_orders():
    try:
        with open(ORDERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_orders(orders):
    with open(ORDERS_FILE, "w", encoding="utf-8") as f:
        json.dump(orders, f, indent=4, ensure_ascii=False)
    print("Orders saved to file.")


def send_request(endpoint, method="GET", data=None):
    url = f"{API_BASE_URL}{endpoint}"
    headers = {
        "accept": "application/json",
        "X-API-Key": API_KEY
    }

    try:
        response = requests.request(method, url, json=data, headers=headers)
        if response.ok:
            return response.json()
        else:
            print(f"API request failed with code {response.status_code}: {response.text}")
            return None
    except requests.RequestException as e:
        print(f"Network error: {e}")
        return None


def update_orders():
    orders = load_orders()
    updated_orders = []

    for order in orders:
        order_id = order.get("orderID")
        if not order_id:
            continue

        # Skip already handled orders or sell orders
        if order.get("side") == "sell" or order.get("linkedTo"):
            updated_orders.append(order)
            continue

        print(f"Checking order {order_id} on exchange...")

        response = send_request(f"/api/orders/{order_id}")
        if not response or not isinstance(response, dict) or "result" not in response:
            print(f"Invalid API response for {order_id}")
            updated_orders.append(order)
            continue

        result = response["result"]
        status_from_api = result.get("status")
        print(f"Order {order_id} status from API: {status_from_api}")

        if status_from_api == "filled":
            order["status"] = "filled"
            updated_orders.append(order)

            # Create sell order
            try:
                original_price = float(order["price"])
                new_price = round(original_price * 1.02, 2)  # +2% price increase
                quantity = float(order.get("quantity", 1))

                print(f"Creating sell order for {order['symbol']} at price {new_price}")

                # Debug: print out the sell order data before sending the request
                print(f"Sell order data: {{ 'symbol': '{order['symbol']}', 'price': {new_price}, 'side': 'sell', 'type': 'limit', 'quantity': {quantity} }}")

                sell_order_response = send_request("/api/orders", method="POST", data={
                    "symbol": order["symbol"],
                    "price": str(new_price),
                    "side": "sell",
                    "type": "limit",
                    "quantity": 1
                })

                # Debug: print response from API
                if sell_order_response:
                    print(f"Sell order response: {sell_order_response}")

                if sell_order_response and "result" in sell_order_response:
                    sell_result = sell_order_response["result"]
                    sell_result["linkedTo"] = order_id  # Link to buy order
                    updated_orders.append(sell_result)
                    print(f"Sell order {sell_result['orderID']} created successfully.")
                else:
                    print("Failed to create sell order. Response:", sell_order_response)

            except Exception as e:
                print(f"Error creating sell order: {e}")
        else:
            # For other statuses (new, cancelled), keep the original status
            order["status"] = status_from_api  # new, cancelled, etc.
            updated_orders.append(order)

    save_orders(updated_orders)


if __name__ == "__main__":
    update_orders()
