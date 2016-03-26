class Customer(object):
    """ A customer of ABC Bank with a checking account. Customers following properties:

    Attributes:
    name: A string representing the customer's name.
    balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0):
        """
        :param name:
        :param balance:
        :return: A customer object whose name is *name* and starting balance is *balance*.
        """
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """
        :param amount:
        :return: Return the balance remaining after withdrawing *amount* dollars.
        """
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """
        :param amount:
        :return: Return the balance remaining after depositing *amount* dollars.
        """
        self.balance += amount
        return self.balance

serge = Customer('Serge Urakhchin', 500.0)
print serge
print serge.balance
print serge.withdraw(100)
print Customer.withdraw(serge,100)
print serge.deposit(1000)


