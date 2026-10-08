class BinaryTreeArray:

    def __init__(self, size):
        self.tree = [None] * size
        self.size = size

    
    def set_root(self, data):
        if self.tree[0] is None:
            self.tree[0] = data
        else:
            print("Root already exists!")
    def set_left(self, parent_index, data):
        child_index = 2 * parent_index + 1

        if child_index < self.size:
            self.tree[child_index] = data
        else:
            print("Index out of range!")
    def set_right(self, parent_index, data):
        child_index = 2 * parent_index + 2

        if child_index < self.size:
            self.tree[child_index] = data
        else:
            print("Index out of range!")
    def insert(self, data):

        for i in range(self.size):

            if self.tree[i] is None:
                self.tree[i] = data
                print(data, "inserted at index", i)
                return

        print("Tree is full!")
    def search(self, data):

        for i in range(self.size):

            if self.tree[i] == data:
                return i

        return -1
    def delete(self, data):

        index = self.search(data)

        if index == -1:
            print(data, "not found!")
            return
        last_index = -1

        for i in range(self.size - 1, -1, -1):

            if self.tree[i] is not None:
                last_index = i
                break
        if last_index == index:
            self.tree[index] = None

        else:
            self.tree[index] = self.tree[last_index]
            self.tree[last_index] = None

        print(data, "deleted!")
    def preorder(self, index=0):

        if index >= self.size or self.tree[index] is None:
            return

        print(self.tree[index], end=" ")

        self.preorder(2 * index + 1)
        self.preorder(2 * index + 2)
    def inorder(self, index=0):

        if index >= self.size or self.tree[index] is None:
            return

        self.inorder(2 * index + 1)

        print(self.tree[index], end=" ")

        self.inorder(2 * index + 2)
    def postorder(self, index=0):

        if index >= self.size or self.tree[index] is None:
            return

        self.postorder(2 * index + 1)
        self.postorder(2 * index + 2)

        print(self.tree[index], end=" ")
    def level_order(self):

        for value in self.tree:

            if value is not None:
                print(value, end=" ")
    def display(self):

        print("\nArray Representation:")

        for i in range(self.size):
            print("Index", i, ":", self.tree[i])
tree = BinaryTreeArray(10)
tree.set_root('A')
tree.set_left(0, 'B')
tree.set_right(0, 'C')
tree.set_left(1, 'D')
tree.set_right(1, 'E')


tree.set_right(2, 'F')


tree.display()
print("\nPreorder: ", end="")
tree.preorder()

print("\nInorder: ", end="")
tree.inorder()

print("\nPostorder: ", end="")
tree.postorder()

print("\nLevel-order: ", end="")
tree.level_order()

print("\n\nSearching for E:")

position = tree.search('E')

if position != -1:
    print("Element found at index", position)
else:
    print("Element not found!")

print("\nInsertion:")
tree.insert('G')

tree.display()

print("\nDeletion:")
tree.delete('D')

tree.display()
print("\nPreorder after deletion: ", end="")
tree.preorder()

print("\nInorder after deletion: ", end="")
tree.inorder()

print("\nPostorder after deletion: ", end="")
tree.postorder()

print("\nLevel-order after deletion: ", end="")
tree.level_order()
