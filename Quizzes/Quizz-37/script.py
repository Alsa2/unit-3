class CounpoundInterest():
    def __init__(self, principal, rate, number_of_years):
        self.principal = principal
        self.rate = rate
        self.number_of_years = number_of_years

class AccountingProgram():
    def __init__(self):
        self.Compound = CounpoundInterest(1000, 0.05, 3)

    def set_principal(self, principal):
        if principal < 0:
            raise ValueError("Principal should be greater than zero")
        self.Compound.principal = principal
    def set_rate(self, rate):
        if rate < 0:
            raise ValueError("Interest rate should be greater than zero")
        self.Compound.rate = rate
    def set_years(self, number_of_years):
        if number_of_years < 0:
            raise ValueError("Years should be greater than zero")
        self.Compound.number_of_years = number_of_years
    def calculate_interest(self):
        return (int((self.Compound.principal * (1 + self.Compound.rate) ** self.Compound.number_of_years)*100)/100)