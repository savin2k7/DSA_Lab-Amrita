class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.top = -1
        self.rear = -1

    def enqueue(self, data):
        if self.rear < self.size - 1:
            if self.rear == -1:
                self.top = 0
                self.rear = 0
                self.queue[self.rear] = data
                print(data, "Added to queue")
                return
            self.rear += 1
            self.queue[self.rear] = data
            print(data, "Added to queue")
        else:
            print("Queue overflow err - Queue is full")
            return

    def dequeue(self):
        if self.rear == -1:
            print("Underflow err -- Queue is empty")
        else:
            data = self.queue[self.top]
            self.queue[self.top] = None
            self.top += 1

    def display(self):
        if self.top == -1:
            print("Queue is empty")
        else:
            for i in range(self.top, self.rear+1):
                print(self.queue[i], end = " ")

q1 = Queue(5)
q1.enqueue(5)
q1.enqueue(10)
q1.enqueue(10)
q1.enqueue(10)
q1.dequeue()
q1.dequeue()
q1.display()