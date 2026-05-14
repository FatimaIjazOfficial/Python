# If the bill was $150.00, split between 5 people, with 12% tip.
print("Welcome to the tip calculater! ")
bill = float(input("What was the total bill? $"))
people = int(input("How many people split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# Each person should pay (150.00 / 5) * 1.12 = 33.6
bill_per_person = (bill + bill * tip / 100) / people
# Format the result to 2 decimal places = 33.60
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
