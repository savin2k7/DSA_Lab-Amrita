class BinaryTree:
    def __init__(self):
        self.tree = [None] * 20

    def insert(self, value):
        for i in range(len(self.tree)):
            if self.tree[i] == None:
                if i == 0 or self.tree[(i - 1) // 2] != None:
                    self.tree[i] = value
                    print(value, "Added to tree")
                    return

        print("Tree is full")

    def insert_left(self, value, parentIndex):
        if parentIndex < 0 or parentIndex >= len(self.tree) or self.tree[parentIndex] == None:
            print("Invalid parent")
            return

        left_index = 2 * parentIndex + 1

        if left_index >= len(self.tree):
            self.tree.extend([None] * (left_index - len(self.tree) + 1))

        self.tree[left_index] = value
        print(value, "Added to left")

    def insert_right(self, value, parentIndex):
        if parentIndex < 0 or parentIndex >= len(self.tree) or self.tree[parentIndex] == None:
            print("Invalid parent")
            return

        right_index = 2 * parentIndex + 2

        if right_index >= len(self.tree):
            self.tree.extend([None] * (right_index - len(self.tree) + 1))

        self.tree[right_index] = value
        print(value, "Added to right")

    def remove_index(self, index):
        if index < 0 or index >= len(self.tree) or self.tree[index] == None:
            print("Invalid index")
            return

        self.tree[index] = None
        print("Node removed")

    def traverse_inorder(self, index=0):
        if index < len(self.tree) and self.tree[index] != None:
            self.traverse_inorder(2 * index + 1)
            print(self.tree[index], end=" ")
            self.traverse_inorder(2 * index + 2)

    def traverse_preorder(self, index=0):
        if index < len(self.tree) and self.tree[index] != None:
            print(self.tree[index], end=" ")
            self.traverse_preorder(2 * index + 1)
            self.traverse_preorder(2 * index + 2)

    def traverse_postorder(self, index=0):
        if index < len(self.tree) and self.tree[index] != None:
            self.traverse_postorder(2 * index + 1)
            self.traverse_postorder(2 * index + 2)
            print(self.tree[index], end=" ")


b = BinaryTree()

b.insert(10)
b.insert_left(20, 0)
b.insert_right(30, 0)
b.insert_left(40, 1)
b.insert_right(50, 1)

print("Inorder Traversal:")
b.traverse_inorder()
print()

print("Preorder Traversal:")
b.traverse_preorder()
print()

print("Postorder Traversal:")
b.traverse_postorder()
print()

b.remove_index(4)

print("After removing:")
b.traverse_inorder()
print()