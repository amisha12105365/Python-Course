# Understanding AND and OR Operators

age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ")

if age >= 18 and has_ticket == "yes":
    print("✅ You can enter!")

elif age >= 18 or has_ticket == "yes":
    print("⚠️ One condition is true.")

else:
    print("❌ You cannot enter.")