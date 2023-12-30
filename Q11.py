# 11.State the order of evaluation of the operators in each of the following Python statements
# and show the value of x after each statement is performed.
# a) x = 7 + 3 * 6 / 2 - 1
# b) x = 2 % 2 + 2 * 2 - 2 / 2
# c) x = ( 3 * 9 * ( 3 + ( 9 * 3 / ( 3 ) ) ) )
print(" a) x = 7 + 3 * 6 / 2 - 1")
M=3*6
D=M/2
A=7+D
S=A-1
print("Multiplication")
print("x = 7 +",M,"/ 2 - 1")
print("Division")
print("x = 7 +",D,"- 1")
print("Additional")
print("x =",A,"- 1")
print("Substraction")
print("x=",S)