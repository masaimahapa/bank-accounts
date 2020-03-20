
from bank import Bank

class Customer:
    def __init__(self, id_number):
        self.id_number= id_number
        
        self.bank= Bank('absa')
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