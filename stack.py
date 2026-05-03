class Stack:
    def __init__(self):
        self.stack = []

    #PUSH ELEMENT ONTO STACK
    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed to stack")

    #SAFE POP METHOD 
    def safe_pop(self):
        if len(self.stack) == 0:
            print("Stack is empty, nothing to pop.")
            return None
        else:
            return self.stack.pop()
        
    #DISPLAY STACK
    def display(self):
        print("Stack:", self.stack)

    #EXAMPLE USAGE OBJECT CREATED 
s = Stack()  

s.push(10)
s.push(20)
s.push(30)

s.display()    

print("Popped:", s.safe_pop())
print("Popped", s.safe_pop())
print("Popped:", s.safe_pop())

    #TRYING TO POP FROM EMPTY STACK
print("Popped:", s.safe_pop())

