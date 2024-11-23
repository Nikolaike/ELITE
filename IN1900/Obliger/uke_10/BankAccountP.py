class BankAccountP:
    def __init__(self, first_name, last_name, number, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def get_balance(self):
        return self.balance
    def print_info(self):
        first = self.first_name; last = self.last_name
        number = self.number; bal = self.balance
        s = f"{first} {last}, {number}, balance: {bal}"
        print(s)
    def transfer(self,amount, new_account):
        self.withdraw(amount)
        new_account.deposit(amount)

def test_BankaccountP():
    TestBank1 = BankAccountP("Nikolai", "Engstad", 1, 10000)
    TestBank2 = BankAccountP("Trym", "Holm", 2, 20)
    expected1 = 8000
    expected2 = 2020
    TestBank1.transfer(2000, TestBank2)
    computed1 = TestBank1.get_balance()
    computed2 = TestBank2.get_balance()
    success = computed1 == expected1 and computed2 == expected2
    assert success
test_BankaccountP()
"""
Terminal>py .\BankAccountP.py
"""
