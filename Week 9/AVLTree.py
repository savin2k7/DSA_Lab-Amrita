class AVLTree:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.left = [-1] * size
        self.right = [-1] * size
        self.height = [0] * size
        self.root = -1
        self.count = 0

    def get_height(self, index):
        if index == -1:
            return 0
        return self.height[index]

    def update_height(self, index):
        l = self.get_height(self.left[index])
        r = self.get_height(self.right[index])

        if l > r:
            self.height[index] = l + 1
        else:
            self.height[index] = r + 1

    def get_balance(self, index):
        return self.get_height(self.left[index]) - self.get_height(self.right[index])

    def rotate_right(self, y):
        x = self.left[y]
        temp = self.right[x]

        self.right[x] = y
        self.left[y] = temp

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = self.right[x]
        temp = self.left[y]

        self.left[y] = x
        self.right[x] = temp

        self.update_height(x)
        self.update_height(y)

        return y

    def insert_node(self, index, data):
        if index == -1:
            index = self.count
            self.data[index] = data
            self.height[index] = 1
            self.count += 1
            return index

        if data < self.data[index]:
            self.left[index] = self.insert_node(self.left[index], data)

        elif data > self.data[index]:
            self.right[index] = self.insert_node(self.right[index], data)

        self.update_height(index)

        balance = self.get_balance(index)

        if balance > 1:
            if data < self.data[self.left[index]]:
                return self.rotate_right(index)
            else:
                self.left[index] = self.rotate_left(self.left[index])
                return self.rotate_right(index)

        if balance < -1:
            if data > self.data[self.right[index]]:
                return self.rotate_left(index)
            else:
                self.right[index] = self.rotate_right(self.right[index])
                return self.rotate_left(index)

        return index

    def insert(self, data):
        if self.count == self.size:
            print("Tree overflow err - Tree is full")
            return

        if self.search(data) != -1:
            print("Duplicate value")
            return

        self.root = self.insert_node(self.root, data)
        print(data, "Added to tree")

    def search(self, data):
        temp = self.root

        while temp != -1:
            if data == self.data[temp]:
                return temp
            elif data < self.data[temp]:
                temp = self.left[temp]
            else:
                temp = self.right[temp]

        return -1

    def display(self, index):
        if index == -1:
            return

        print(self.data[index], end=" ")
        self.display(self.left[index])
        self.display(self.right[index])


t1 = AVLTree(5)

t1.insert(30)
t1.insert(20)
t1.insert(40)
t1.insert(10)
t1.insert(25)

print("AVL Tree:")
t1.display(t1.root)
print()