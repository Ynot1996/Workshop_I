# 1.
num = int(input("Enter a integer number: "))
if num == 1945:
    print("This war is over!!")

# 2.
num = int(input("Enter a integer number: "))
if num < 0:
    print(num*-1)
else:
    print(num)

# 3.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
operation = input("Enter a operation: ")
operation = operation.lower()
if num1 and num2 and operation:
    print(f"number 1: {num1}\n")
    print(f"number 2: {num2}\n")
    print(f"operation: {operation}\n")
    match operation:
        case "add":
            print(f"{num1} + {num2} = {num1+num2}")
        case "subtract":
            print(f"{num1} - {num2} = {num1-num2}")
        case "multiply":
            print(f"{num1} * {num2} = {num1*num2}")

# 4.
hourly_wage = int(input("Hourly wage: "))
hours = int(input("hours: "))
dayOfTheWeek = int(input("day of the week: "))
if dayOfTheWeek != "Saturday" or "Sunday":
    print(hourly_wage * hours * dayOfTheWeek)
else:
    print(hourly_wage * hours * dayOfTheWeek * 2)

# 5.
temperature =int(input("Temperature?"))
rainOrNot = input("Will it rain (yes / no)")
if temperature > 20:
    print("wear jeans and a T")
elif temperature > 10:
    print()























