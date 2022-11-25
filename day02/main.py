print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tips = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
pers = int(input("How many people to split the bill? "))

total = bill + (tips/100 * bill)
print(total)
each_person = round(total/pers,2)

print(f"Each person should pay: ${each_person}")