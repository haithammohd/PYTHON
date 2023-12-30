# 12. Write a program that requests the user to enter two numbers and prints the sum, product,
# difference and quotient of the two numbers.
a=float(input("Please enter first number:"))
b=float(input("Please enter second number:"))
s=a+b
p=a*b
d=a-b
q=a/b
print("You enter first number is ",a," and second number is ",b)
print("Thier sum:",a,"+",b,"=",s)
print("Thier product:",a,"*",b,"=",p)
print("Thier difference:",a,"-",b,"=",d)
print("Thier quotient:",a,"/",b,"=",q)