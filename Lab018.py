#strings
#bunch of characters
# '' , "" , """ """
name = "Asmita"
print(name)
name = 'Asmita'
print(name)
name = """Asmita , is a good person
....
....
"""
print(name)
print(type(name))


# use of '' , "" , """ """

dir = "C:/Users/Asmita/PycharmProjects/PythonProject/Ex_13112025"
print(dir)

# R - Raw string
# if we want to print the string as it is then we can use r

dir = r'C:\Asmita\PycharmProjects\PythonProject\Ex_13112025'
print(dir)


#Format of the string
first_name = "Harry"
last_name = "Potter"
print(first_name + " " + last_name)
print(first_name , last_name)

# f is used to format the string - it will replace the value of the variable
#{} - placeholder
print(f'Your full name is {first_name} {last_name}')