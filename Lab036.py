# write a program to calculate & display the loop
# given numerical score ( e.g. A,B,C,D or F)
# based on the following grade:
# input - score -89
# output - B

# A = 90-100
# B = 80-89
# C = 70-79
# D = 60-69
# E = 0-59

# multiple loop: if, elseif ,else

score = int(input("Enter the score\n"))

if score >=90 and score <=100:
    print("Grade is A")
elif score >=80 and score <=89:
    print("Grade is B")
elif score >=70 and score <=79:
    print("Grade is C")
elif score >=60 and score <=69:
    print("Grade is D")
elif score >=0 and score <=59:
    print("Grade is E")

else:
    print("Invalid score")

#output: Enter the score
#101
#Invalid score

# Enter the score
# 67
# Grade is D

