#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
bill = input("How much is the bill?")
people = input("How many people is the bill being split between?")
tip = input("What percentage tip do you want to leave?")
tip_percent = float(tip) / 100 + 1

per_person = float(bill) / int(people) * float(tip_percent)

print(f"Each person should pay: {round(per_person, 2)}")