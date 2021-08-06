class Appliance:
    days_in_month = 30

    def __init__(self, cost):
        self.cost = cost

    def get_monthly_expense(self):
        return self.cost * self.days_in_month

