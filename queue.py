class queue:
    def __init__(self):
        self.queue = []

    #PUSH ELEMENT ONTO QUEUE
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} enqueued to queue")

    #SAFE POP METHOD 
    def safe_dequeue(self):
        if len(self.queue) == 0:
            print("queue is empty, nothing to pop.")
            return None
        else:
            return self.queue.popleft()
        
    #DISPLAY QUEUE
    def display(self):
        print("queue:", self.queue)

    #EXAMPLE USAGE OBJECT CREATED 

q = queue()  

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()    

print("dequeued:", q.safe_dequeue())
print("dequeued", q.safe_dequeue())
print("dequeued:", q.safe_dequeue())
print("dequeued:", q.safe_deque())
    

