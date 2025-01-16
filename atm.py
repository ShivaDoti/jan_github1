username="Doti Shiva"
password=1234
user_name=input("Enter the user name:")
user_password=int(input("enter the password:"))
s='''
    1.credit
    2.debit
    3.mini statement
    4.exit'''
Amount=5000
if user_name==username and user_password==password:
 while True:
    print(s)
    option=int(input("enter the option:"))
    if option==1:
        credit_amount=float(input("enter the amount:"))
        print("amount after credit:",Amount+credit_amount)
    elif option==2:
        debit_amount=float(input("enter the debit amount:"))
        print("amount after debit:",Amount-debit_amount)
        if debit_amount>Amount:
            print("sorry you dont have sufficient Balance Try again")
    
    elif option==3:
        print("### mini statement:",Amount)
    elif option==4:
        print("thank you vist again")
        break
        
else:
    print('''sorry user or password is incorrect 
          Try again!!!!''')

