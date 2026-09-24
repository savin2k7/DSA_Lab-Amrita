class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.top = None
        self.rear = None

    def enqueue(self, data):
        new = Node(data)
        if self.rear == None:
            self.top = new
            self.rear = new
            return("Added")

        self.rear.next = new
        self.rear = new
        return("Added")

    def dequeue(self):
        if self.top == None:
            print("Queue is empty")
            return
        store = self.top.data
        temp = self.top.next
        self.top.next = None
        self.top = temp

        if self.top == None:
            self.rear = None

        return store

    def display(self):
        if self.top == None:
            print("Queue is empty")
            return

        temp = self.top
        while temp is not None:
            print(temp.data, end = " --> ")
            temp = temp.next
        print("None\n")
        return

q1 = Queue()
print(q1.enqueue(5))
print(q1.enqueue(10))
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.enqueue(10))
print(q1.enqueue(10))
print(q1.enqueue(10))
print(q1.enqueue(10))
q1.display()