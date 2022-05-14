#Q2. Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
#   
 #       Cost price (in Rs)                                       Tax
 #       > 100000                                                  15 %
 #       > 50000 and <= 100000                          10%
  #      <= 50000                                                  5%#

tax = 0
price =int(input("Enter the price of bike " ))
if price > 100000:
     tax = 15/100*price
elif price >50000 and price <=100000:
     tax = 10/100*price
else:
     tax = 5/100*price
print("Tax to be paid ",tax)