#oops challege 
class Account:

    def __init__(self,owner,balance): #initializing attributes
          self.balance = balance
          self.owner = owner

    def deposit(self): #creating a method called deposit
        damount= int(input('enter the amount to deposit : '))
        self.balance = self.balance + damount
        print(f"the initial amount of user {self.owner} is :{self.balance}")

    def withdraw(self): #creating a method called withdraw
        wamount = int(input('enter the amount to withdraw : '))

        if wamount >= self.balance: #checking for exceeding amounts
            print('The amount is not Valid!')
        else:
            self.balance = self.balance - wamount
            print(f"the initial amount of user {self.owner} is :{self.balance}")


#account / object creation 
acct1 = Account('Rix',100)

acct1.deposit()
acct1.withdraw()