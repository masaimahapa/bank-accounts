import os
class Bank:

    def __init__(self, bank_name='absa'):
        self.bank_name= bank_name
        self.bank_accounts= {
            '1':{'balance':1000, 'password': 'secret1', 'id_number':'01', 'type':'savings'},
            '2':{'balance': 2000, 'password': 'secret2', 'id_number':'02', 'type':'savings'},
            '3':{'balance':3000, 'password': 'secret3', 'id_number':'03', 'type':'cheque'},
            '4':{'balance':4000, 'password': 'secret3', 'id_number':'03', 'type':'savings'},           
            
        }
        
    
    def withdraw(self, bank_account_number, amount, secret_password):
        #if the account exists, withdraw
        if self.check_account(bank_account_number):
            self.bank_accounts[bank_account_number]['balance']-=amount
    
            print('Your remaining balance : ')
            print(self.bank_accounts[bank_account_number].get('balance'))            


    def deposit(self, bank_account_number, amount):
        #if account exists, deposit
        if self.check_account(bank_account_number):
            self.bank_accounts[bank_account_number]['balance']+=amount

            print('new balance is:')
            print(self.bank_accounts[bank_account_number]['balance'])
            #print(self.bank_accounts)

    def transfer(self, from_bank_account_number,to_bank_account_number, amount, secret_password):
        #if both bank accounts exist
        if self.check_account(from_bank_account_number) and self.check_account(to_bank_account_number):
            if self.bank_accounts[from_bank_account_number]['balance'] >= amount:
                self.bank_accounts[from_bank_account_number]['balance']-= amount
                self.bank_accounts[to_bank_account_number]['balance']+= amount
                
                print(f'sent R{amount} from account number {from_bank_account_number} to account number {to_bank_account_number}')
                print(f"sender now has {self.bank_accounts[from_bank_account_number]['balance']}")
                print(f"reciepient now has {self.bank_accounts[to_bank_account_number]['balance']}")
                      
    def check_account(self, acc_number):
        #check if the account actually exists
        if acc_number in self.bank_accounts.keys():
            return True
        else: 
            return False

