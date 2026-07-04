class Bank:
    def __init__(self):
        self.name = " "
        self._account_number=" "
        self.balance=0
        self.minimum_balance=1000
    def open_account(self):
        self.name=input("enter the name")
        self.balance=int(input("enter the initial balance"))

    def deposit(self):
        amount=int(input("enter the amount"))
        self.balance +=amount
        print("deposit successful")
    def withdraw(self):
        amount=int(input("enter the amount"))
        if (amount<=self.balance):
            self.balance-=amount
        else:
            print("insuffiecient balance") 
    def display_balance(self):
        print(f"Your current balance is {self.balance}")
    def display(self):
        print(f"Your name is {self.name}")
        print(f"Your balance is{self.balance}")
        print(f"Your account number is{self._account_number}")
    def transfer(self):
        rac = int(input("enter the account number:"))
        amount =int(input("enter the amount "))
        self.balance-=amount
        print(f" the end balance{self.balance}")
    def change_name(self):
        self.name=input("enter the changed name:")
        print(f"{self.name}")
    def minidisplay(self):
        print(f"the minimun balance for the account is : {self.minidisplay}")
    print("=========XYZ BANK=========")
    print(''' 1.Open account
          2.Deposit
          3.Withdraw
          4.Transfer
          5.Balance
          6.Mini Statement
          7.Customer Details
          8.Bank report
          9Exit''')
choice=int(input("enter the choice"))
while True:
    
    if(choice==1):
        print(f"{choice}.Open Account")
        break
    elif(choice==2):
        print(f"{choice}.Deposit")
        break
    elif(choice==3):
        print(f"{choice}.Withdraw")
        break
    elif(choice==4):
        print(f"{choice}.Transfer")
        break
    elif(choice==5):
        print(f"{choice}.Balance")
        break
    elif(choice==6):
        print(f"{choice}.Mini Statement")
        break
    elif(choice==7):
        print(f"{choice}.Customer Detail")
        break
    elif(choice==8):
        print(f"{choice}.Bank Report")
        break
    elif(choice==9):
        print("Exit")
        break


acc1=Bank()
acc1.name="himani"
acc1.account_number=123
print('----------------------')
acc1.deposit()
print('--------------------')

acc1.withdraw()
print('----------------------')

acc1.display_balance()
print('----------------------')

acc1.display()
print('----------------------')
acc1.transfer()
print('----------------------')
acc1.change_name()
print('----------------------')
acc1.minidisplay()



#     def open_account(self):
#         self.name=input("enter the name")
#         self.balance=int(input("enter the balance"))
#         print(f"Account open for {self.name} with balance{self.balance}")
    
#     password=input("enter the pass")
#     if password=='ADMIN':
#         print("Welcome to XYZ BANK")
    
