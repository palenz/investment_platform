class Investment:

    def __init__(self, investor, company, equity, payment, date, id = None):
        self.investor = investor
        self.company = company
        self.equity = equity
        self.payment = payment
        self.date = date
        self.id = id