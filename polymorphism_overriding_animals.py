class Animal:
    def sound(self):
        return"Some generic sound"
    
class DogOverride(Animal):
    def sound(self):
        return"Bark!"
    
#overriding
animal = Animal()
dog = DogOverride()
print("Animal sound:", animal.sound())
print("Dog sound:", dog.sound())

