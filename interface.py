import system

while True:
    print("\n***New Account Creating***")
    name = str(input("Enter Your Name:"))
    surname = str(input("Enter Your Surname:"))
    age = int(input("Enter Your Age:"))

    name = name.upper()
    surname = surname.upper()

    if age >= 18:
        print("\nAccount Created Successfully! Welcome", name, surname)
        ac1 = system.Account(name, surname, age)

        def move():
                movements = [ac1.accountInfo, ac1.invest, ac1.withdrawal, ac1.getCredit, ac1.loans, ac1.repayLoan, ac1.deleteAccount]

                move = int(input("1-Account Details\n2-Invest\n3-Withdrawal\n4-Get Credit\n5-My Loans\n6-Pay Loans\n7-Delete Account\nYour Movement:"))
                move = move - 1 ## List start with zeroth element so move must be move - 1
                return movements[move]()

        while True:
            if ac1.accountCheck == False:
                break
            else:
                print("\n***Movements***")
                move()

    else:
        print("\nYou Must Be Bigger Than 18! \nAccount Not Created...")
