# Movie Ticket Price Calculator

age = int(input("Enter your age: "))

if age < 5:
    price = 0
    print("🎉 Your ticket is FREE!")

elif age <= 12:
    price = 100
    print("👦 Child ticket")

elif age <= 60:
    price = 200
    print("👤 Adult ticket")

else:
    price = 120
    print("👴 Senior citizen ticket")

print("Your ticket price is ₹", price)