import datetime
import random

database = {}

x = datetime.datetime.now()

def generatedaccountnumber():
    return random.randrange(0000000000, 9999999999)

def login():
    print('*** Login Page ***')
    print('Enter your account details below! ')
    accountnumberfromuser = int(input('Please put in your registered account number: '))
    password = input('Put in your password carefully: ')

    for accountnumber, userdetails in database.items():
        if(accountnumber == accountnumberfromuser):
            if (userdetails[3] == password):
                bankoperation(userdetails)
                isloginsuccessful = True
            else:
                print('Invalid account or password')
                login()
        else:
            print('Invalid account or password')
            login()

def bankoperation(user):

    print(f"** ** Welcome %s , You logged in on the ** ** "%user[1])
    print(x)
    selectedoption = int(input(""" *** *** What operation will you like to perform? *** ***
                               
    [1] Withdrawal
    [2] Deposit
    [3] Complaint
    [4] Logout
    [5] Exit 
    
    """))
    
    if (selectedoption == 1):
        withdrawal()
    elif (selectedoption == 2):
        deposit()
    elif (selectedoption == 3):
        complaint()
    elif (selectedoption == 4):
        logout()
    elif (selectedoption == 5):
        exit()
    else:
        print('Invalid option')
        bankoperation()

def register():
    print("*** Register Here With Us ***")
    first_name = input("What is your first name: ")
    last_name = input("What is your last name: ")
    email = input("Kindly enter your E-mail address: ")
    password = input("Create a unique password for yourself: ")
    accountnumber = generatedaccountnumber()
    print("*** ***Welcome to Zuri Bank*** *** ")
    print(x)
    print("*** *** Here is your account number ***%d*** " %accountnumber)
    print(" *** *** Keep your details a secret, most especially your password *** *** ")
    database[accountnumber] = [first_name, last_name, email, password]
    login()



def withdrawal():
    money = input("How much would you like to withdraw: ")
    print("Take your cash, thank you for using this service: %s " %money)
    done()

def deposit():
    deposit = input("How much would you like to deposit: " )
    print("Current balance: %s "%deposit)
    done()

def complaint():
    comlaint = input("What complaint will you like to report?: " )
    print('Thank you for contacting us.')
    done()

def done():
    print(" would you love to perform another transaction or logout. ")
    choose = int(input('Press 1 to continue\nPress 2 to logout\n'))
    if (choose == 1):
        do = int(input("""Welcome back 
                       
    [1] Withdrawal
    [2] Deposit
    [3] Complaint """))
    
        if (do  == 1):
            withdrawal()
        elif (do  == 2):
            deposit()
        elif (do == 3):
            complaint()
        else:
            print("Option invalid")
            done()

    elif (choose == 2):
        print(" Okay, Thank you!!! ")
        logout()
    else:
        print("Invalid input")
        done()

def logout():
    login()

def exit():
    exit()


register()