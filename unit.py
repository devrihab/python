units= int(input("Enter The Units of Current Consumed: "))

if(units<=100):
 print("The Bill Amount is: ", units*6,"Rs")
else:
 print("The Bill Amount is: ", units*8,"Rs")