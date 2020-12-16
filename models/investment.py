class Investment:

    def __init__(self, investor, company, equity, payment, date_of_investment, id = None):
        self.investor = investor
        self.company = company
        self.equity = equity
        self.payment = payment
        self.date_of_investment = date_of_investment
        self.valuation = int((100*int(payment))/int(equity))
        self.id = id