#Base class
class Vehicle:
    def move(self):
        return"vehicle is moving"
    
#Subclass car
class Car:
    def move (self):
        return"driving on the road"
    
#Subclass bicycle
class Bicycle:
    def move(self):
        return"pedaling on the road"
    
#using polymorphism
def make_vehicle_move(vehicle):
    print(vehicle.move())

#create object 
c1 = Car()
b1 = Bicycle()

make_vehicle_move(c1)
make_vehicle_move(b1)


    
