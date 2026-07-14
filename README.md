# Stock Portfolio Tracker

## Description
The Stock Portfolio Tracker is a simple Python program that calculates the total investment value of a user's stock portfolio. It uses a predefined dictionary of stock prices, accepts user input for stock names and quantities, calculates the investment for each stock, and stores the total investment value in a text file.

## Features
- Displays available stocks and their prices.
- Accepts multiple stock entries from the user.
- Calculates investment value for each stock.
- Calculates the total portfolio investment.
- Saves the total investment value to `portfolio.txt`.
- Handles invalid stock names.

## Technologies Used
- Python 3

## Stock Prices Used

| Stock | Price |
|--------|------:|
| AAPL | ₹180 |
| TSLA | ₹250 |
| GOOG | ₹300 |
| MSFT | ₹220 |
| AMZN | ₹270 |

## How to Run

1. Clone this repository:
   ```bash
   git clone <repository-link>
   ```

2. Navigate to the project folder:
   ```bash
   cd Task-2_StockPortfolio
   ```

3. Run the program:
   ```bash
   python stock_tracker.py
   ```

4. Enter the required stock names and quantities when prompted.

5. The program will display the total investment and save the result in `portfolio.txt`.

## Example Output

```
========================================
      STOCK PORTFOLIO TRACKER
========================================

Available Stocks:
AAPL : ₹180
TSLA : ₹250
GOOG : ₹300
MSFT : ₹220
AMZN : ₹270

How many different stocks do you own? 3

Stock 1
Enter Stock Name: AAPL
Enter Quantity: 5
Investment in AAPL: ₹900

Stock 2
Enter Stock Name: TSLA
Enter Quantity: 2
Investment in TSLA: ₹500

Stock 3
Enter Stock Name: MSFT
Enter Quantity: 4
Investment in MSFT: ₹880

========================================
Total Investment Value = ₹2280
========================================

Result has been saved in portfolio.txt
```

## Output File

The program creates a file named `portfolio.txt` containing:

```
Total Investment Value = ₹2280
```

## Author

**Swetha**