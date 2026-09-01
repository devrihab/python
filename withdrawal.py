balance = int(input("Enter Your Balance: "))
amount = int(input("Enter The Amount to Withdraw: "))

if(amount>balance):
    print("Insufficient Balance")
else:
    print("Withdrawal Successful")    