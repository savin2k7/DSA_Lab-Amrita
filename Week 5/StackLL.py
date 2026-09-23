class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "added to stack")

    def pop(self):
        if self.top is None:
            print("Stack Underflow Err -- Stack is empty")
        else:
            store = self.top.data
            self.top = self.top.next
            print(store, "removed from stack")
            return store

    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)
            return self.top.data

    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            current = self.top
            while current is not None:
                print(current.data, end=" ")
                current = current.next
            print()


print("---------------------------------------------------------------------")
print("Creating stack using linked list")
s1 = Stack()

print("1 -- Add to stack\n2 -- Remove from stack\n3 -- View top\n4 -- Display full stack\n5 -- Exit")

while True:
    choice = int(input("Enter a choice: "))

    if choice == 1:
        data = int(input("Enter the number: "))
        s1.push(data)

    elif choice == 2:
        s1.pop()

    elif choice == 3:
        s1.peek()

    elif choice == 4:
        s1.display()

    elif choice == 5:
        break

    else:
        print("Select a valid choice.")
