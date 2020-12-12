class Company:
    
    def __init__(self, name, industry, investor_id):
        self.name = name
        self.industry = industry
        self.rounds = []
        self.investors = []
        self.valuation = []
        self.investor_id = investor_id