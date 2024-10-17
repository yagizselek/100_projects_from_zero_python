
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15? "))
people = int(input("How many people to split the bill? "))

total_bill = bill + bill * tip / 100

each_bill = total_bill / people

each_bill_est = round(each_bill, 2)

if each_bill_est.is_integer():
    print(f"Each person should pay: ${int(each_bill_est)}")
else:
    print(f"Each person should pay: ${each_bill_est}")

#I added an if/else system to verify if the final bill is an integer or a float.