# Hardcoded stock prices
stock_prices = {
    "AAPL": 175.00,
    "GOOGL": 2850.50,
    "TSLA": 720.30,
    "AMZN": 3440.25,
    "MSFT": 299.00
}

portfolio = {}
total_investment = 0

print("Welcome to the Stock Tracker!")
print("Available stocks:", ', '.join(stock_prices.keys()))
print("Type 'done' to finish input.\n")

# Step 1: Take input from user
while True:
    stock = input("Enter stock symbol: ").upper()
    if stock == 'DONE':
        break
    if stock in stock_prices:
        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
            portfolio[stock] = quantity
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Stock not found. Please choose from available list.")

# Step 2: Calculate total investment
print("\nInvestment Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_investment += value
    print(f"{stock}: {qty} shares x ${price:.2f} = ${value:.2f}")

print(f"\nTotal Investment: ${total_investment:.2f}")

# Step 3: Optional — Save to file
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save == 'yes':
    with open("stock_investment_summary.txt", "w") as file:
        file.write("Stock Investment Summary:\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = qty * price
            file.write(f"{stock}: {qty} x ${price:.2f} = ${value:.2f}\n")
        file.write(f"\nTotal Investment: ${total_investment:.2f}")
    print("Summary saved to 'stock_investment_summary.txt'.")
