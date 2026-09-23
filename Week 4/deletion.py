from linkedlist import linkedlist
from node import Node

def deleteFromBeginning(self):
    if self.head is not None:
        self.head = self.head.next
    else:
        return

def deleteFromEnd(self):
    if self.head is None:
        return
    elif self.head.next is None:
        self.head = None
        return
    else:
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

def deleteAtIndex(self, index):
    if self.head is None:
        return

    if index == 0:
        self.head = self.head.next
        return

    temp = self.head

    for i in range(index - 1):
        if temp.next is None:
            return
        temp = temp.next

    if temp.next is None:
        return

    temp.next = temp.next.next

linkedlist.deleteFromBeginning = deleteFromBeginning
linkedlist.deleteFromEnd = deleteFromEnd
linkedlist.deleteAtIndex = deleteAtIndex