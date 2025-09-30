a_name = "John"
age = 20

print("Printing it all on", end='')
print("one line")

print("Printing it all on", end=' ')
print("one line")

print("Printing it all on", end=', ')
print("one line")

num1, num2 = 50, 500
print(f'{num1}, {num2}')
print("There are {1}, {0}".format(num1, num2))

name = "John"
print("num1 is %d and name is %s" % (num1, name))