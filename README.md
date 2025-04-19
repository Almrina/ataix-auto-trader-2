Here's the `README.md` for your project:

```markdown
# order-tracker

This Python script interacts with the Ataix exchange API to track and create sell orders based on the status of previously placed buy orders. It checks the status of buy orders and automatically generates sell orders once the buy order is filled. The script reads orders from a local `orders.json` file and updates the order statuses based on API responses.

## Features

- Tracks buy orders from the Ataix exchange.
- Creates sell orders automatically once a buy order is filled.
- Saves order details and statuses in a local JSON file (`orders.json`).
- Handles API communication with the Ataix exchange, including error handling for failed requests.

## Requirements

- Python 3.6+
- `requests` library for making API calls

You can install the required library with pip:

```bash
pip install requests
```

## Setup

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/<your-username>/order-tracker.git
    ```
   
2. Replace the `API_KEY` in the script with your own Ataix API key.

3. Ensure you have an `orders.json` file in the same directory, or let the script create it for you.

## Usage

Run the script to check the status of existing buy orders and automatically generate sell orders when applicable.

```bash
python order_tracker.py
```

The script will:
- Read orders from the `orders.json` file.
- Check the status of each order.
- Create a sell order if the buy order is filled.
- Update the status of each order in the `orders.json` file.

## Notes

- The script currently creates sell orders with a 2% price increase over the original price of the buy order.
- You need to have sufficient funds in your account to create sell orders.
- Error messages will be printed in the console if something goes wrong with the API requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Make sure to replace `<your-username>` with your actual GitHub username in the `git clone` command. Let me know if you need any further adjustments!
