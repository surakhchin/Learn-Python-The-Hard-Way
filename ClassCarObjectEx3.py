from abc import ABCMeta, abstractmethod

class Vehicle(object):
    """ A vehicle for sale by Serge U. Dealership.
        Attributes:
            wheels: An integer representing the number of wheels.
            miles: The integral number of miles driven on the vehicle.
            make: The make of the vehicle as a string.
            model: The model of the vehicle as a string.
            year: The integral year the vehicle was built.
            sold_on: The date the vehicle was sold.
    """

    __metaclass__ = ABCMeta

    base_sale_price = 0

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """
        :param wheels:
        :param miles:
        :param make:
        :param model:
        :param year:
        :param sold_on:
        :return: Return new Vehicle object.
        """
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """
        :return: Return the sale price for the vehicle as a float amount.
        """
        if self.sold_on is not None:
            return 0.00 # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """
        :return Return the price for which we would pay to purchase the vehicle.
        """
        if self.sold_on is None:
            return 0.0 # Not yet sold
        return self.base_sale_price - (.10 * self.miles)

    @abstractmethod
    def vehicle_type(self):
        """
        :return: Return a string representing the type of vehicle this is.
        """
        pass


class Car(Vehicle):
    """
    A car for sale by Serge U. Dealership.
    """

    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        """
        :return: A string representing the type of vehicle
        """
        return 'car'


class Truck(Vehicle):
    """
    A truck for sale by Serge U. Dealership.
    """

    base_sale_price = 10000
    wheels = 4

    def vehicle_type(self):
        """
        :return: A string representing the type of vehicle.
        """
        return 'truck'


class Motorcycle(Vehicle):
    """
    A motorcycle for sale by Serge U. car dealership.
    """

    base_sale_price = 4000
    wheels = 2

    def vehicle_type(self):
        """
        :return: A string representing vehicle type.
        """
        return 'motorcycle'


bike = Vehicle(4, 40000, "Nissan", "Leaf", 2015, None)

