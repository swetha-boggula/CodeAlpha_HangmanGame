# Stock Portfolio Tracker

# Hardcoded dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 300,
    "MSFT": 220,
    "AMZN": 270
}

print("=" * 40)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 40)

print("\nAvailable Stocks:")
for stock in stock_prices:
    print(f"{stock} : ₹{stock_prices[stock]}")

# Total investment
total_investment = 0

# Number of stocks to enter
num_stocks = int(input("\nHow many different stocks do you own? "))

for i in range(num_stocks):

    print(f"\nStock {i + 1}")

    stock_name = input("Enter Stock Name: ").upper()

    if stock_name in stock_prices:

        quantity = int(input("Enter Quantity: "))

        investment = stock_prices[stock_name] * quantity

        print(f"Investment in {stock_name}: ₹{investment}")

        total_investment += investment

    else:
        print("Invalid Stock Name!")

print("\n" + "=" * 40)
print(f"Total Investment Value = ₹{total_investment}")
print("=" * 40)

# Save result to a text file (UTF-8 encoding)
with open("portfolio.txt", "w", encoding="utf-8") as file:
    file.write(f"Total Investment Value = ₹{total_investment}")

print("\nResult has been saved in portfolio.txt")