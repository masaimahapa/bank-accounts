import bank
import customer


import os
global absa
def show_absa():
    print('---------------------------------------------------------------------')
    print('                  Absa. Today. Tomorrow. Together')
    print('---------------------------------------------------------------------')

def get_account_number():
    acc_num= input('enter your account number: ')
    return acc_num



def show_menu():
    print('---------------------------------------------------------------------')
    print('choose transaction')
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Transfer')
    print('4. show my accounts')
    print('5. reset password')
    print('0. exit')
    print('---------------------------------------------------------------------')

def bank_loop():
    #create an instance of Bank
    absa= bank.Bank()
    
    user_input=-1

    while user_input != 0:
        show_absa()
        show_menu()
        user_input= input('enter:  ')        
        if user_input=='1':
            #deposit money into a bank accout
            account_number= get_account_number() 
            amount= float(input('how much do you want to deposit?'))
            os.system('clear')
            show_absa()
            absa.deposit(account_number, amount)
        elif user_input=='2':
            #withdraw from a bank account
            account_number= get_account_number() 
            amount= float(input('how much do you want to withdraw?  '))
            psw= input('enter password:  ')
            os.system('clear')
            show_absa()
            absa.withdraw(account_number, amount, psw)

        elif user_input=='3':
            #transfer from bank account to bank account
            account_number= get_account_number()
            to_account= input('enter account you are sending money to:  ')
            amount= float(input('enter how much money to transfer: '))
            psw= input('enter password:  ')
            os.system('clear')
            show_absa()
            absa.transfer(account_number, to_account, amount, psw)
        
        elif user_input=='4':
            #how many bank accounts owned
            id_num= input('enter ID number: ')
            user= customer.Customer(id_num)
            accounts=user.accounts_owned
            for idx, each in enumerate(accounts):
                print(f"{idx}. Account number: {each['account_number']}. Type {each['type']} . has a Balance of : {each['balance']}.")
                print(' ')

        elif user_input=='5':
            #reset password
            id_num= input('enter ID number: ')
            user= customer.Customer(id_num)
            acc_number= input('enter account number')
            absa.bank_accounts[acc_number]['password']= user.set_password(acc_number)
            print(absa.bank_accounts)


        elif user_input=='0':
            #exit the program, break the while loop.
            break
        input('press enter to continue')
        os.system('clear')



def main():
    #clear the terminal
    os.system('clear')
    #run the bank loop
    bank_loop()
    print('Thank you for choosing ABSA bank. Have a nice day')

if __name__ == "__main__":
    main()
