#function overloading using default arguments 
def add(a=0, b=0, c=0):
    return a + b + c 

print(add(5,10))            #adds two numbers
print(add(2,3,4))           #adds three numbers
print(add(3,4))             #adds two numbers
