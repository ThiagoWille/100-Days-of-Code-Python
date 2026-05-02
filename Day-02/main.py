print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?\n"))
people = int(input("How many people will split the bill?\n"))

full_price = (bill * (1 + (tip / 100)))
split_bill = ( full_price / people)

print(f"Each person should pay: ${round(split_bill, 2)}")
