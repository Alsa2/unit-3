class Account:
    def __init__(self, holder_name:str, holder_email:str, number:list, balance:int):
        self.holder_name = holder_name
        self.holder_email = holder_email
        self.number = number
        self.balance = balance
        print("You have created a new object")
    
    def get_account_no(self)->str:
        return "".join(self.number)
    def set_holder_name(self, name:str):
        self.holder_name = name
    def set_holder_email(self, email:str):
        self.holder_email = email
    def get_balance(self)->int:
        return self.balance
    def set_balance(self, balance:int):
        self.balance = balance
