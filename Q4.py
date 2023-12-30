# 4. Total Purchase
# A customer in a store is purchasing five items. Write a program that asks for 
# the price of
# each item, and then displays the subtotal of the sale, the amount of sales 
# tax, and the total.
# Assume the sales tax is 6 percent.
n=0
total=0
while(n<=4):
    n=n+1
    a=str(n)
    print("Item:",n)
    price=int(input("Enter price of item no"+a+":"))
    tax=price*6/100
    subtotal=price+tax
    total=total+subtotal
    print("The amount of sales tax is:",tax)
    print("Subtotal of sales is:",subtotal)
    print("Total sales is:",total)