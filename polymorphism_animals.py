class Dog:
    def speak(self):
        return"Woof!"
    
class Cat:
    def speak(self):
        return"Meow!"
    
#using polymorphism
def make_animal_speak(animal):
    print(animal.speak())

#create objects
d1 = Dog()
c1 = Cat()

make_animal_speak(d1)
make_animal_speak(c1)

        


    


