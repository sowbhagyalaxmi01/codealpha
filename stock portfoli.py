prices = {
    "AAPL": 180,
    "NFLX": 250,
    "GOOG": 150
}

total = 0

stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in prices:
    total = prices[stock_name] * quantity
    print("Total investment value:", total)

    file = open("stock_result.txt", "w")
    file.write("Stock: " + stock_name + "\n")
    file.write("Quantity: " + str(quantity) + "\n")
    file.write("Total Value: " + str(total))
    file.close()

    print("Result saved in stock_result.txt")

else:
    print("Stock not available")