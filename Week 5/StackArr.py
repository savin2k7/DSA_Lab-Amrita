class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def push(self, data):
        if self.top < self.size - 1:
            self.top += 1
            self.stack[self.top] = data
            print(data, "added to stack")
        else:
            print("Stack Overflow Err -- Stack is full")

    def pop(self):
        if self.top == -1:
            print("Stack Underflow Err -- Stack is empty")
        else:
            store = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            print(store, "removed from stack")
            return store

    def peek(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Top element: ", self.stack[self.top])
            return self.stack[self.top]

    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            for i in range(self.top, -1, -1):
                print(self.stack[i], end=" ")
            print("")
            return

print("---------------------------------------------------------------------")
stack_size = int(input("Initialize stack length: "))
print("Creating stack of length", stack_size)
s1 = Stack(stack_size)

print("1 -- Add to stack \n2 -- Remove from stack \n3 -- View top \n4 -- Display full stack \n5 -- Exit")

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
