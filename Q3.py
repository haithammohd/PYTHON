# 3. Land Calculation
# One acre of land is equivalent to 43,560 square feet. Write a program that 
# asks the user to enter the total square feet in a tract of land and calculates 
# the number of acres in the tract.
# Hint: divide the amount entered by 43,560 to get the number of acres.
s=float(input("please enter total square feet in a tract of land:"))
a=s/43560
print("You enter total square feet in a tract of land is:",s)
print("Their equivalent number of acres in the tract is:",a)