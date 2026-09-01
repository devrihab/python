bill= int(input("Enter The Bill Amount: "))

discount= (bill*10)/100

if(bill<=2000):
 print("Yout Have No Discount, the Bill Amount is: ",bill,"Rs")
else:
 print("Congrats, The Discounted Bill Amount is: ", bill-discount,"Rs")