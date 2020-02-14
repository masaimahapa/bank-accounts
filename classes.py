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


#------------------------------------------------------------
class BankAccount:
    #Initializer/ 
    def __init__(self, account_number, balance=1000, interest=0.12, monthly_fee=50):
        self.balance= balance
        self.interest= interest
        self.monthly_fee= monthly_fee
        self.bank= Bank()
        self.account_number= account_number
        self.password= self.get_password(account_number, self.bank)
        
    def get_password(self, account_number, bank):
        return bank.bank_accounts[account_number]['password']
        
        

    #Instance method
    def finish_month(self):
        #interest
        self.balance= (self.balance+ self.balance* self.interest/12)
        #minus bank charges
        self.balance=self.balance- self.monthly_fee
        return round(self.balance, 2)
    """
    #Instance Method
    def deposit(self, amount):
        #add the amount deposited
        self.balance+= amount
        return round(self.balance,2)
        
    #Instance method
    def withdraw(self, amount):
        #minus the amount withdrew
        self.balance-= amount
        return round(self.balance,2)
    """

    def withdraw(self, bank, amount, password):
        bank.withdraw(self.account_number, amount, password)
        
    def deposit(self, bank, amount):
        bank.deposit(self.account_number, amount)

#_------------------------------------------------------------------
class Customer:
    def __init__(self, id_number):
        self.id_number= id_number
        
        self.bank= Bank()
        self.accounts_owned= self.get_accounts(id_number, self.bank)
        

    def set_password(self, account_number):
        psw= input('Enter password')
        return psw
    
    def get_accounts(self, id_number, bank):
        accounts= bank.bank_accounts
        #print(accounts)
        owned=[]
        for each in accounts.keys():
            if accounts[each]['id_number']== id_number:
                my_acc=accounts[each]
                my_acc['account_number']= each
                owned.append(my_acc)
        return owned
        

    def check_password(self, psw, entered_pass):
        if psw== entered_pass:
            return True
        else:
            return False