# Take two integer numbers from user and want to add them
#we need to use input function

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

#type conversion: convert string to integer (because here + sign is doing concatination)

result =int(num1) + int(num2)
print(result)


# + : if it is int then it will do addition
# + : if it is string then it will do concatination

#if we want to convert string to int then use = int
#if we want to convert int to string then use = str

print(type(int(num1)))

