
print("Welcome to Python Pizza")
bill = 0
size = input("What size of pizza do you want? S, M or L? ")
if size == "S":
    bill += 20
elif size == "M":
    bill += 30
elif size == "L":
    bill += 50


pepperoni = input("Do you want pepperoni? Y or N? ")
if pepperoni == "Y":
    if size == "S":
        bill += 5
    else:
        bill += 10

extra_cheese = input("Do you want extra cheese? Y or N? ")
if extra_cheese == "Y":
    bill += 3
    print(f"Your total bill is ${bill}")
else:
    print(f"Your total bill is ${bill}")


