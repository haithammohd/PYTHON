# 10. Stock Transaction Program
# Last month Joe purchased some stock in Acme Software, Inc. Here are the 
# details of the
# purchase:
# • The number of shares that Joe purchased was 1,000.
# • When Joe purchased the stock, he paid $32.87 per share.
# • Joe paid his stockbroker a commission that amounted to 2 percent of the 
# amount he paid
# for the stock.
# Two weeks later Joe sold the stock. Here are the details of the sale:
# • The number of shares that Joe sold was 1,000.
# • He sold the stock for $33.92 per share.
# • He paid his stockbroker another commission that amounted to 2 percent of
# the amount
# he received for the stock.
# Write a program that displays the following information:
# • The amount of money Joe paid for the stock.
# • The amount of commission Joe paid his broker when he bought the stock.
# • The amount that Joe sold the stock for.
# • The amount of commission Joe paid his broker when he sold the stock.
# • Display the amount of money that Joe had left when he sold the stock and 
# paid his
# broker (both times). If this amount is positive, then Joe made a profit. If the 
# amount is
# negative, then Joe lost money.
p_paid=1000*32.87
p_c=p_paid*0.02
sale=1000*33.92
c_sale=sale*0.02
print("The amount of money Joe paid for the stock is:",p_paid)
print("The amount of commission Joe paid his broker when he bought the stock is:",p_c)
print("The amount that Joe sold the stock is:",sale)
print("The amount of commission Joe paid his broker when he sold the stock is:",c_sale)
p=(sale-c_sale)-(p_paid+p_c)
if(p>0):
    print("The amount of money that Joe had left is profit:",p)
else:
    print("The amount of money that Joe had left is Lose:",p*-1)
    
