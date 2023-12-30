# 8. Tip, Tax, and Total
# Write a program that calculates the total amount of a meal purchased at a 
# restaurant. The
# program should ask the user to enter the charge for the food, and then 
# calculate the amount
# of a 15 percent tip and 7 percent sales tax. Display each of these amounts 
# and the total.
c=float(input("Please enter the charge for the food:"))
tip=c*0.15
tax=c*0.07
total=c+tip+tax
print("You enter the charge for the food:",c)
print("Thier Tip is:",tip)
print("Thier sales tax is:",tax)
print("The total amount of a meal purchased is:",total)