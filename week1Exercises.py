# 1.
print(15 / 4)
print(17 % 3)
print(5 ** 3)

# 2.
print(type(42))
print(type(3.14159))
print(type("Hello World"))

# 3.
firstName, LastName = "Tony", "Kang"
print(firstName, LastName)

# 4.
age = 28
currentYear = 2025
print(currentYear-28+100)

# 5.
fav_color = input("What is your favorite color? ")
print("wow", fav_color, "is your favorite color")

# 6.
print(len(fav_color))

# 7.
height = "2.453"
float_height = float(height)
print(float_height*2)

# 8.
is_monday = True
is_sunny = False
print(is_monday and is_sunny)
print(is_monday or is_sunny)
print(not is_sunny)

# 9.
x = 12
y = 8
print(x > y)
print(x == y)
print(x <= 25)

# 10.
name = input("What is your name? ")
age = input("What is your age? ")
print("Hello " + name + ", You age is " + age)
if int(age) > 18:
    print("You're old enough.")

# 11.
print("Humpty Dumpty sat on a wall\nHumpty Dumpty had a GREAT fall\nAll the kings horses and all the kings men\nCouldn\’t put Humpty together again!!!")

# 12.
firstName = input("What is your first name? ")
print("!" + f'{firstName}!'*2)

# 13.
print(10, end=" ")
print("+", end=" ")
print(8, end=" ")
print("-", end=" ")
print(5, end=" ")
print("=", end=" ")
print(10 + 8 - 5, end=" ")

# 14.
print("\n")
weight = 70
height = 1.75
BMI = round(weight / (height**2), 2)
print(f"Weight: {weight}kg\n", end="")
print("Height: {}m".format(height))
print("BMI: %.2f" % (BMI))

# 15.
name = "Henry Jones"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print("my name is", name, ", I am", age, "years old\n")
print("my skills are")
print("-", skill1, "(" +level1+ ")")
print("-", skill2, "(" +level2+ ")", end=' ')
print("-", skill3, "(" +level3+ " )\n")
print("I am looking for a job with a salary of", lower, "-", upper, "pounds per month")















