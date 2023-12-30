# 6. Sales Tax
# Write a program that will ask the user to enter the amount of a purchase. 
# The program
# should then compute the state and county sales tax. Assume the state sales 
# tax is 4 percent
# and the county sales tax is 2 percent. The program should display the 
# amount of the purchase, the state sales tax, the county sales tax, the total 
# sales tax, and the total of the sale
# (which is the sum of the amount of purchase plus the total sales tax).
# Hint: use the value 0.02 to represent 2 percent, and 0.04 to represent 4 
# percent.
p=float(input("Please enter the amount of a purchase:"))
statetax=p*0.04
countytax=p*0.02
totaltax=statetax+countytax
totalsale=p+totaltax
print("The amount of the purchase is:",p)
print("The state sales tax is:",statetax)
print("The county sales tax is:",countytax)
print("The total sales tax is:",totaltax)
print("The total sales is:",totalsale)