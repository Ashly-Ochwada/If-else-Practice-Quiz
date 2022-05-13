#8. Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
 #            Unit                                                     Price  
#First 100 units                                               no charge
#Next 100 units                                              Rs 5 per unit
#After 200 units                                             Rs 10 per unit
#(For example if input unit is 350 than total bill amount is Rs2000)
amount=0
num=int(input("Enter number of electric unit"))
if num<=100:
     amount=0
if num>100 and num<=200:
     amount=(num-100)*5
if num>200:
     amount=500+(num-200)*10
print("Amount to pay :",amount)

                                      