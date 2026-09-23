from linkedlist import linkedlist

def displayElements(self):
    temp = self.head

    while temp:
        print(temp.data, end=" --> ")
        temp = temp.next

    print("None")

def count(self):
    temp = self.head
    i = 0

    while temp:
        i += 1
        temp = temp.next
    return i

linkedlist.displayElements = display
linkedlist.count = count