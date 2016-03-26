class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model
    @staticmethod
    def make_car_sound():
        print 'Vroom'
    @classmethod
    def is_motorcylce(cls):
        return cls.wheels == 2


mustang = Car('Ford', 'Mustang')
print mustang.wheels
print Car.wheels
print mustang.make_car_sound()
print Car.make_car_sound()
print Car.is_motorcylce()

