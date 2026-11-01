class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new = Node(data)

        if self.root is None:
            self.root = new
            print(data, "Added to tree")
            return

        temp = self.root

        while True:
            if data == temp.value:
                print("Duplicate value")
                return

            if data < temp.value:
                if temp.left is None:
                    temp.left = new
                    print(data, "Added to tree")
                    return
                temp = temp.left

            else:
                if temp.right is None:
                    temp.right = new
                    print(data, "Added to tree")
                    return
                temp = temp.right

    def search(self, data):
        temp = self.root

        while temp is not None:
            if temp.value == data:
                return True

            if data < temp.value:
                temp = temp.left
            else:
                temp = temp.right

        return False

    def delete_node(self, root, data):
        if root is None:
            return None

        if data < root.value:
            root.left = self.delete_node(root.left, data)

        elif data > root.value:
            root.right = self.delete_node(root.right, data)

        else:
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            temp = root.right

            while temp.left is not None:
                temp = temp.left

            root.value = temp.value
            root.right = self.delete_node(root.right, temp.value)

        return root

    def delete(self, data):
        if self.search(data) == False:
            print("Value not found")
            return

        self.root = self.delete_node(self.root, data)
        print(data, "Removed from tree")

    def display_inorder(self, node):
        if node is not None:
            self.display_inorder(node.left)
            print(node.value, end=" ")
            self.display_inorder(node.right)

    def display(self):
        if self.root is None:
            print("Tree is empty")
            return

        self.display_inorder(self.root)
        print()


b = BinarySearchTree()

b.insert(50)
b.insert(30)
b.insert(70)
b.insert(20)
b.insert(40)
b.insert(60)
b.insert(80)

print("Inorder Traversal:")
b.display()

print("Search 40:", b.search(40))

b.delete(30)

print("After deleting:")
b.display()