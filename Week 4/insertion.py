from node import Node
from linkedlist import linkedlist
from traversal import count

def insertAtBeginning(self, data):
    new = Node(data)
    new.next = self.head
    self.head = new

def insertAtEnd(self, data):
    if self.head is None:
        new = Node(data)
        self.head = new
        return
    
    temp = self.head
    while temp.next is not None:
        temp = temp.next
    new = Node(data)
    temp.next = new
    new.next = None

def insertAtIndex(self, index, data):
    if index == 0:
        self.insertAtBeginning(data)
        return
    elif index < 0 or index > self.count():
        print("Invalid Index entered")
        return
    else:
        new = Node(data)
        temp = self.head
        for i in range(0, index - 1):
            temp = temp.next
        new.next = temp.next
        temp.next = new

linkedlist.insertAtBeginning = insertAtBeginning
linkedlist.insertAtEnd = insertAtEnd
linkedlist.insertAtIndex = insertAtIndex