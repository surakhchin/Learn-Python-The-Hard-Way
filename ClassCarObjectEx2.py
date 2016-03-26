class Car(object):
    """ A car for sale by Serge U Dealership.

    Attributes:
    wheels: An integer representing the number of wheels the car has.
    miles: The integral number of miles driven on the car.
    make: The make of the car as a string.
    model: The model of the car as a string.
    year: The integral year the car was built.
    sold_on: The date the vehicle was sold.
    """

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """
        :param wheels: An integer representing the number of wheels the car has.
        :param miles: The integral number of miles driven on the car.
        :param make: The make of the car as a string.
        :param model: The model of the car as a string.
        :param year: The integral year the car was built.
        :param sold_on: The date the vehicle was sold.
        :return: A new Car object
        """
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """
        :return: Return the sale price for this car as a float amount.
        """
        if self.sold_on is not None:
            return 0.0 # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """
        :return: Return the price for which we would pay to purchase the vehicle.
        """
        if self.sold_on is None:
            return 0.0 # Not yet sold
        return 8000 - (.10 * self.miles)
carA = Car(4,40000, "nissan", "leaf", 2016, None)
print carA.year
print carA.make
print carA