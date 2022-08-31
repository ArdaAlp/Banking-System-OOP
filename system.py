# AUTHOR: ARDA ALP

import time
import random

class User(object):

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def info(self):
        print("\n***Account Details***")
        print("Name:", self.name)
        print("Surname:", self.surname)
        print("Age:", self.age)

class Account(User):

    def __init__(self, name, surname, age, balance=0, creditReturn=0, accountCheck=True):
        super().__init__(name, surname, age)
        self.balance = balance
        self.creditReturn = creditReturn
        self.accountCheck = accountCheck

    def accountInfo(self):
        self.info()
        print("Balance:", self.balance)
        input('<-- Press "Enter" For Go Back')

    def invest(self):
        print("\n***Investing***")
        amount = int(input("Enter The Amount:"))
        self.balance += amount
        print("Invest Successful\nNew Balance:", self.balance)
        input('<-- Press "Enter" For Go Back')

    def withdrawal(self):
        print("\n***Withdrawaling***")
        amount = int(input("Enter The Amount:"))
        print("Balance:", self.balance)
        if amount > self.balance:
            print("Insufficient Balance!")
            input('<-- Press "Enter" For Go Back')
        else:
            self.balance -= amount
            print("Withdrawal Successful\nNew Balance:", self.balance)
            input('<-- Press "Enter" For Go Back')

    def getCredit(self):
        print("\n***Credit Application***")
        if self.creditReturn == 0:
            self.interestRate = self.age / 250  # Interest Rate Direct Proportion With Age
            amount = int(input("Enter Credit Amount:"))
            if amount <= 250:
                self.creditReturn = amount + self.age
            else:
                self.creditReturn = amount + (amount * self.interestRate)
            self.balance += amount
            print("Credit Process Successful!")
            print("Interest Rate:", self.interestRate)
            print("New Balance:", self.balance)
            print("Credit Return:", int(self.creditReturn))
            input('<-- Press "Enter" For Go Back')
        else:
            print("You Was Already Get An Credit!\nFirstly Pay Your Credit Returns")
            self.loans()

    def loans(self):
        print("\n***Your Loans***")
        if self.creditReturn == 0:
            print("You Don't Have Any Loan!")
            input('<-- Press "Enter" For Go Back')
        else:
            print("You Have An Loan")
            print("Repayable Amount:", int(self.creditReturn))
            input('<-- Press "Enter" For Go Back')

    def repayLoan(self):
        print("\n***Loan Payment***")
        if self.creditReturn > 0:
            print("Your Loan:", int(self.creditReturn))
            amount = int(input("Enter The Repay Amount:"))
            if amount > self.balance:
                print("Insufficient Balance!")
                input('<-- Press "Enter" For Go Back')
            elif amount == 0:
                print("Please Enter Any Amount!")
                input('<-- Press "Enter" For Go Back')
            else:
                if amount > self.creditReturn:
                    print("Amount Bigger Than Your Loan!")
                    print("Your Loan:", int(self.creditReturn))
                    input('<-- Press "Enter" For Go Back')
                elif amount == self.creditReturn:
                    print("You Was Pay All Your Loans!")
                    self.creditReturn -= amount
                    self.balance -= amount
                    print("Account Balance: {}\nLoan: {}".format(
                        self.balance, int(self.creditReturn)))
                    input('<-- Press "Enter" For Go Back')
                else:
                    print("You Was Pay A Little Bit Loan!")
                    self.creditReturn -= amount
                    self.balance -= amount
                    print("Account Balance: {}\nLoan: {}".format(
                        self.balance, int(self.creditReturn)))
                    input('<-- Press "Enter" For Go Back')
        else:
            print("You Don't Have Any Loan!")
            input('<-- Press "Enter" For Go Back')

    def deleteAccount(self):
        print("\n***Account Delete Process***")
        if self.creditReturn > 0:
            print("You Have An Loan You Must Pay It Firstly!\n-Nice Try :)")
            input('<-- Press "Enter" For Go Back')
        else:
            ensure = str(input("Are You Sure? (YES/NO): "))
            ensure = ensure.upper()
            if ensure == "NO":
                print("\nAccount Delete Process Canceled! \nAccount Doesn't Deleted")
                input('<-- Press "Enter" For Go Back')
            elif ensure == "YES":
                code = random.randrange(10000, 99999)
                codeCheck = int(
                    input("Please Enter The Code! (Code:{}) \nCode: ".format(code)))
                if codeCheck == code:
                    print(
                        "The Code Is Correct! \nAccount Deleted! \n\n----- Thanks For You Choose The Us... -----")
                    self.accountCheck = False
                    input('<-- Press "Enter" For Create New Account')
                else:
                    print("Invalid Code! \nProcess Canceled, Account Doesn't Deleted!")
                    input('<-- Press "Enter" For Go Back')
