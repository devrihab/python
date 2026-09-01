name = input("Enter Your Name: ")
member = input("Are You a Member (y/n)")
print("Enter Price of Three Products")
price1 = int(input("1."))
price2 = int(input("2."))
price3 = int(input("3."))
total = price1+price2+price3

delivery = 50

offer1 = total-(total*20)/100
offer2 = total-(total*15)/100
offer3 = total-(total*10)/100

if(total>=5000):
    if(member=="y"):
            print("Congrats You Have 20% Discount\nAdditional 5% Membership Discount\nPay Rs",offer1-(total*5)/100)
    else:
            print("Congrats You Have 20% Discount\n Pay Rs",offer1)
elif(total>=3000):
   
    if(member=="y"):
        print("Congrats You Have 15% Discount\nAdditional 5% Membership Discount\nPay Rs",offer2-(total*5)/100)
    else:
        print("Congrats You Have 15% Discount\n Pay Rs",offer2)
elif(total>=1500):
    print("Congrats You Have 10% Discount\n Bill Amount Rs",offer3,"+ Delivery Rs",delivery,"\nPay Rs",total+delivery)
else:
    print("Bill Amount Rs",total,"\nDelivery Rs",delivery,"\nPay Rs",total+delivery)



  