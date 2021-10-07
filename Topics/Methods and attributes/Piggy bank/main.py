class PiggyBank:
    def __init__(self, dollars, cents):
        self.cents = cents % 100
        self.dollars = cents // 100
        self.dollars += dollars

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += (self.cents + deposit_cents) // 100
        self.cents = (self.cents + deposit_cents) % 100
        self.dollars += deposit_dollars

