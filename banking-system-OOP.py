#AUTHOR: ARDA ALP

import time

class user(object):

  def __init__(self, name, surname, age):
    self.name = name
    self.surname = surname
    self.age = age
    
  def info(self):
    print("\n***Account Details***")
    print("Name:",self.name)
    print("Surname:", self.surname)
    print("Age:", self.age)

class account(user):

  def __init__(self, name, surname, age, balance=0, creditReturn=0):
    super().__init__(name, surname, age)
    self.balance = balance
    self.creditReturn = creditReturn
    
  def accountInfo(self):
    self.info()
    print("Balance:",self.balance)
    
  def invest(self):
    amount = int(input("Enter The Amount:")) 
    self.balance += amount
    print("Invest Successful\nNew Balance:", self.balance) 
    
  def withdrawal(self):
    amount = int(input("Enter The Amount:"))
    if amount > self.balance:
      print("Insufficient Balance!")
    else:
      self.balance -= amount
      print("Withdrawal Successful\nNew Balance:", self.balance) 
    
  def getCredit(self):
    self.interestRate = self.age / 1000 #Interest Rate Direct Proportion With Age
    amount = int(input("Enter Credit Amount:"))
    self.creditReturn = amount + (amount * self.interestRate) 
    self.balance += amount
    print("Credit Process Successful!")
    print("Interest Rate:",self.interestRate) 
    print("New Balance:",self.balance) 
    print("Credit Return:",int(self.creditReturn))
  
  def loans(self):
    print("***Your Loans***") 
    if self.creditReturn == 0:
      print("You Don't Have Any Loan!")
    else:
      print("You Have An Loan") 
      print("Repayable Amount:",int(self.creditReturn)) 

  def repayLoan(self):
    if self.creditReturn > 0:
      amount = int(input("Enter The Repay Amount:"))
      if amount > self.balance:
        print("Insufficient Balance!") 
      else:
        if amount > self.creditReturn:
          print("Amount Bigger Than Your Loan!") 
          print("Your Loan:",int(self.creditReturn)) 
        elif amount == self.creditReturn:
          print("You Was Pay All Your Loans!")
          self.creditReturn -= amount           
          self.balance -= amount
          print("Account Balance: {}\nLoan: {}".format(self.balance, int(self.creditReturn))) 
        else:
          print("You Was Pay A Little Bit Loan!")
          self.creditReturn -= amount
          self.balance -= amount
          print("Account Balance: {}\nLoan: {}".format(self.balance, int(self.creditReturn))) 
    else:
      print("You Don't Have Any Loan!")
         

print("***New Account Creating***")
name = str(input("Enter Your Name:"))
surname = str(input("Enter Your Surname:")) 
age = int(input("Enter Your Age:")) 
    
print("\nAccount Created Successfully!")
    
ac1 = account(name, surname, age)

while True:

  print("\n***Movements***")
  move = int(input("1-Account Details\n2-Invest\n3-Withdrawal\n4-Get Credit\n5-My Loans\n6-Pay Loans\nYour Movement:"))

  if move == 1:
    time.sleep(0.7)
    ac1.accountInfo()
    time.sleep(0.8) 

  elif move == 2:
    time.sleep(0.7)
    ac1.invest()
    time.sleep(0.8)

  elif move == 3:
    time.sleep(0.7)
    ac1.withdrawal()
    time.sleep(0.8)

  elif move == 4:
    time.sleep(0.7)
    ac1.getCredit() 
    time.sleep(0.8)
    
  elif move == 5:
    time.sleep(0.7)
    ac1.loans()
    time.sleep(0.8)
    
  elif move == 6:
    time.sleep(0.7)
    ac1.repayLoan()
    time.sleep(0.8)

  else:
    time.sleep(0.7)
    print("Undefined Movement!")
    time.sleep(0.8)
    
