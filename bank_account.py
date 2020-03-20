from bank import Bank

class BankAccount:
    #Initializer 
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

    def withdraw(self, bank, amount, password):
        bank.withdraw(self.account_number, amount, password)
        
    def deposit(self, bank, amount):
        bank.deposit(self.account_number, amount)
