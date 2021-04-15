class  Car:
    def __init__(self,make,model):
        self.make = make
        self.model=model
    def __str__(self):
        return '__str__ for Car'
    def __repr__(self):
        return '__repr__ for Car'

car=Car('Tesla','Model S')
print(car)
'{}'.format(car)
print(car)
