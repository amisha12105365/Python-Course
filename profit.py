# Profit or Loss Calculator

cost_price = float(input("Enter the cost price: ₹"))
selling_price = float(input("Enter the selling price: ₹"))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("🎉 You made a profit of ₹", profit)

elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("😔 You made a loss of ₹", loss)

else:
    print("🙂 No profit, no loss!")