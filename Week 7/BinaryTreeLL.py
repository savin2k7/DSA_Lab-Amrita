class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_root(self, value):
        if self.root is None:
            self.root = Node(value)
            print(value, "Added as root")
        else:
            print("Root already exists")

    def find_node(self, value):
        if self.root is None:
            return None

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.value == value:
                return current

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        return None

    def insert_left(self, value, parentValue):
        parent = self.find_node(parentValue)

        if parent is None:
            print("Invalid parent")
            return

        if parent.left is not None:
            print("Left child already exists")
            return

        parent.left = Node(value)
        print(value, "Added to left")

    def insert_right(self, value, parentValue):
        parent = self.find_node(parentValue)

        if parent is None:
            print("Invalid parent")
            return

        if parent.right is not None:
            print("Right child already exists")
            return

        parent.right = Node(value)
        print(value, "Added to right")

    def remove(self, value):
        if self.root is None:
            print("Tree is empty")
            return

        if self.root.value == value:
            self.root = None
            print("Node removed")
            return

        queue = [(self.root, None)]

        while queue:
            current, parent = queue.pop(0)

            if current.value == value:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None

                print("Node removed")
                return

            if current.left is not None:
                queue.append((current.left, current))

            if current.right is not None:
                queue.append((current.right, current))

        print("Value not found")

    def traverse_inorder(self, node):
        if node is not None:
            self.traverse_inorder(node.left)
            print(node.value, end=" ")
            self.traverse_inorder(node.right)

    def traverse_preorder(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.traverse_preorder(node.left)
            self.traverse_preorder(node.right)

    def traverse_postorder(self, node):
        if node is not None:
            self.traverse_postorder(node.left)
            self.traverse_postorder(node.right)
            print(node.value, end=" ")


b = BinaryTree()

b.insert_root(10)
b.insert_left(20, 10)
b.insert_right(30, 10)
b.insert_left(40, 20)
b.insert_right(50, 20)

print("Inorder Traversal:")
b.traverse_inorder(b.root)
print()

print("Preorder Traversal:")
b.traverse_preorder(b.root)
print()

print("Postorder Traversal:")
b.traverse_postorder(b.root)
print()

b.remove(20)

print("After removing:")
b.traverse_inorder(b.root)
print()