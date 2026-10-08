
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:

    def __init__(self):
        self.root = None
    def create_tree(self):

        self.root = Node('A')
        self.root.left = Node('B')
        self.root.right = Node('C')
        self.root.left.left = Node('D')
        self.root.left.right = Node('E')
        self.root.right.right = Node('F')
    def insert(self, data):

        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]

        while queue:

            node = queue.pop(0)
            if node.left is None:
                node.left = new_node
                return
            else:
                queue.append(node.left)
            if node.right is None:
                node.right = new_node
                return
            else:
                queue.append(node.right)
    def search(self, data):

        if self.root is None:
            return None

        queue = [self.root]

        while queue:

            node = queue.pop(0)

            if node.data == data:
                return node

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return None
    def delete(self, data):

        if self.root is None:
            print("Tree is empty!")
            return
        if (self.root.data == data and
            self.root.left is None and
            self.root.right is None):

            self.root = None
            print(data, "deleted!")
            return

        queue = [self.root]

        target = None
        deepest = None
        parent_of_deepest = None

        while queue:

            node = queue.pop(0)
            if node.data == data:
                target = node
            if node.left is not None:
                parent_of_deepest = node
                deepest = node.left
                queue.append(node.left)

            if node.right is not None:
                parent_of_deepest = node
                deepest = node.right
                queue.append(node.right)
        if target is None:
            print(data, "not found!")
            return
        target.data = deepest.data
        if parent_of_deepest.right == deepest:
            parent_of_deepest.right = None
        else:
            parent_of_deepest.left = None

        print(data, "deleted!")
    def preorder(self, node):

        if node is None:
            return

        print(node.data, end=" ")

        self.preorder(node.left)
        self.preorder(node.right)
    def inorder(self, node):

        if node is None:
            return

        self.inorder(node.left)

        print(node.data, end=" ")

        self.inorder(node.right)
    def postorder(self, node):

        if node is None:
            return

        self.postorder(node.left)
        self.postorder(node.right)

        print(node.data, end=" ")
    def level_order(self):

        if self.root is None:
            return

        queue = [self.root]

        while queue:

            node = queue.pop(0)

            print(node.data, end=" ")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

tree = BinaryTree()
tree.create_tree()
print("Preorder: ", end="")
tree.preorder(tree.root)

print("\nInorder: ", end="")
tree.inorder(tree.root)

print("\nPostorder: ", end="")
tree.postorder(tree.root)

print("\nLevel-order: ", end="")
tree.level_order()
print("\n\nSearching for E:")

result = tree.search('E')

if result is not None:
    print("Element found:", result.data)
else:
    print("Element not found!")

print("\nInsertion:")
tree.insert('G')

print("Level-order after insertion: ", end="")
tree.level_order()

print("\n\nDeletion:")
tree.delete('B')

print("Level-order after deletion: ", end="")
tree.level_order()
print("\n\nFinal Preorder: ", end="")
tree.preorder(tree.root)

print("\nFinal Inorder: ", end="")
tree.inorder(tree.root)

print("\nFinal Postorder: ", end="")
tree.postorder(tree.root)

print("\nFinal Level-order: ", end="")
tree.level_order()
