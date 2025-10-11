print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
number_people = input("How many people to split the bill? ")
percentage_tip = int(tip)/100
total_bill = float(bill) + (float(bill) * percentage_tip)
each_person = round((total_bill/int(number_people)),2)
print(f"Each person should pay: {each_person}")
