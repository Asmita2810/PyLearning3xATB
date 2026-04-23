#create a program that determine whether a given year is leap year

# logic: A year is a leap year if:
#
# It is divisible by 4 and not divisible by 100,
# OR
# It is divisible by 400

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")



#output: Enter a year: 2016
#2016 is a leap year