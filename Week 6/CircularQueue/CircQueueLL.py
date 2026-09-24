class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.current_size = 0
        self.front = None
        self.rear = None

    def enqueue(self, data):
        if self.current_size == self.size:
            print("Queue overflow err - Queue is full")
            return

        new_node = Node(data)
        
        if self.front is None:
            self.front = new_node
            self.rear = new_node
            self.rear.next = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front
            
        self.current_size += 1
        print(data, "Added to queue")

    def dequeue(self):
        if self.front is None:
            print("Underflow err -- Queue is empty")
            return None

        temp_data = self.front.data

        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

        self.current_size -= 1
        return temp_data

    def display(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.front:
                break
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
