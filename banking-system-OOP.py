#AUTHOR: ARDA ALP

import time

class User(object):

  def __init__(self, name, surname, age):
    self.name = name
    self.surname = surname
    self.age = age
    
  def info(self):
    print("\n***Account Details***")
    print("Name:",self.name)
    print("Surname:", self.surname)
    print("Age:", self.age)

class Account(User):

  def __init__(self, name, surname, age, balance=0, creditReturn=0):
    super().__init__(name, surname, age)
    self.balance = balance
    self.creditReturn = creditReturn
    
  def accountInfo(self):
    self.info()
    print("Balance:",self.balance)
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
    print("Balance:",self.balance) 
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
      self.interestRate = self.age / 250 #Interest Rate Direct Proportion With Age
      amount = int(input("Enter Credit Amount:"))
      self.creditReturn = amount + (amount * self.interestRate) 
      self.balance += amount
      print("Credit Process Successful!")
      print("Interest Rate:",self.interestRate) 
      print("New Balance:",self.balance) 
      print("Credit Return:",int(self.creditReturn))
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
      print("Repayable Amount:",int(self.creditReturn)) 
      input('<-- Press "Enter" For Go Back') 

  def repayLoan(self):
    print("\n***Loan Payment***")
    if self.creditReturn > 0:
      print("Your Loan:",int(self.creditReturn)) 
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
          print("Your Loan:",int(self.creditReturn))
          input('<-- Press "Enter" For Go Back') 
        elif amount == self.creditReturn:
          print("You Was Pay All Your Loans!")
          self.creditReturn -= amount           
          self.balance -= amount
          print("Account Balance: {}\nLoan: {}".format(self.balance, int(self.creditReturn))) 
          input('<-- Press "Enter" For Go Back') 
        else:
          print("You Was Pay A Little Bit Loan!")
          self.creditReturn -= amount
          self.balance -= amount
          print("Account Balance: {}\nLoan: {}".format(self.balance, int(self.creditReturn))) 
          input('<-- Press "Enter" For Go Back') 
    else:
      print("You Don't Have Any Loan!")
      input('<-- Press "Enter" For Go Back')  
 
print("***New Account Creating***")
name = str(input("Enter Your Name:"))
surname = str(input("Enter Your Surname:")) 
age = int(input("Enter Your Age:")) 
    
print("\nAccount Created Successfully!")
    
ac1 = Account(name, surname, age)

def move():
  movements = {
    "1": ac1.accountInfo, 
    "2": ac1.invest, 
    "3": ac1.withdrawal, 
    "4": ac1.getCredit, 
    "5": ac1.loans, 
    "6": ac1.repayLoan
  }
  
  move = str(input("1-Account Details\n2-Invest\n3-Withdrawal\n4-Get Credit\n5-My Loans\n6-Pay Loans\nYour Movement:"))
  return movements[move]()
    
while True:
  print("\n***Movements***")
  move()