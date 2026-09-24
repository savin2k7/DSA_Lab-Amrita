class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.top = -1
        self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.top:
            print("Queue overflow err - Queue is full")
            return
        
        if self.top == -1:
            self.top = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
            
        self.queue[self.rear] = data
        print(data, "Added to queue")

    def dequeue(self):
        if self.top == -1:
            print("Underflow err -- Queue is empty")
            return None
        
        temp = self.queue[self.top]
        
        if self.top == self.rear:
            self.top = -1
            self.rear = -1
        else:
            self.top = (self.top + 1) % self.size
        return temp

    def display(self):
        if self.top == -1:
            print("Queue is empty")
            return
        
        i = self.top
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()
q1 = CircularQueue(5) 
q1.enqueue(5) 
q1.enqueue(10) 
q1.enqueue(10) 
q1.enqueue(10) 
q1.enqueue(10) 
q1.enqueue(10) 
q1.dequeue() 
q1.enqueue(8) 
q1.display()