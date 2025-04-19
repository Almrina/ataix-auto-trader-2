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

The script will:
- Read orders from the `orders.json` file.
- Check the status of each order.
- Create a sell order if the buy order is filled.
- Update the status of each order in the `orders.json` file.

## Notes

- The script currently creates sell orders with a 2% price increase over the original price of the buy order.
- You need to have sufficient funds in your account to create sell orders.
- Error messages will be printed in the console if something goes wrong with the API requests.

### Key Points:
1. **Code blocks** (e.g., for installation instructions or code snippets) are wrapped in triple backticks (```) to format them properly.
2. You can replace the placeholder `<your-username>` with your actual GitHub username in the clone command.
3. The headings are marked with `#` for different levels of headings (`#` for main heading, `##` for subheadings).
4. Any important file references (like `orders.json`) should be wrapped in backticks to format them as code.

This will give you a nicely formatted `README.md` file once added to your GitHub repository.
