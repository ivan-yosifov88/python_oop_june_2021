class Account:

    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __add__(self, other):
        new_owner = f"{self.owner}&{other.owner}"
        new_amount = self.amount + other.amount
        new_transaction = self._transactions + other._transactions
        new_account = Account(new_owner, new_amount)
        new_account._transactions = new_transaction

        return new_account

    def __eq__(self, other):
        return self.balance == other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @property
    def transactions(self):
        return self._transactions

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if not 0 <= account.balance + amount_to_add:
            raise ValueError("sorry cannot go in debt!")
        account.transactions.append(amount_to_add)
        return f"New balance: {account.balance}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self.validate_transaction(self, amount)


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
