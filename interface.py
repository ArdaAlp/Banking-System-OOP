import system

print("***New Account Creating***")
name = str(input("Enter Your Name:"))
surname = str(input("Enter Your Surname:"))
age = int(input("Enter Your Age:"))

name = name.upper()
surname = surname.upper()

if age >= 18:
    print("\nAccount Created Successfully! Welcome", name, surname)
    ac1 = system.Account(name, surname, age)

    def move():
            movements = {
                "1": ac1.accountInfo,
                "2": ac1.invest,
                "3": ac1.withdrawal,
                "4": ac1.getCredit,
                "5": ac1.loans,
                "6": ac1.repayLoan,
                "99": ac1.deleteAccount
            }

            move = str(input(
                "1-Account Details\n2-Invest\n3-Withdrawal\n4-Get Credit\n5-My Loans\n6-Pay Loans\n99-Delete Account\nYour Movement:"))
            return movements[move]()


    while True:
        if ac1.accountCheck == False:
            break
        else:
            print("\n***Movements***")
            move()

else:
    print("\nYou Must Be Bigger Than 18! \nAccount Not Created...")
