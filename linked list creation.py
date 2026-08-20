class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create_list(self, values):
        self.head = None
        for val in values:
            self.insert_end(val)
        print("Linked list created.")

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning.")

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Inserted {data} at the end.")

    def insert_at_index(self, index, data):
        if index < 0:
            print("Invalid index.")
            return
        if index == 0:
            self.insert_beginning(data)
            return
            
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            if not current:
                print("Index out of bounds.")
                return
            current = current.next
            
        new_node.next = current.next
        current.next = new_node
        print(f"Inserted {data} at index {index}.")

    def delete_by_value(self, value):
        if not self.head:
            print("List is empty.")
            return

        if self.head.data == value:
            self.head = self.head.next
            print(f"Deleted {value} from the list.")
            return

        current = self.head
        while current.next and current.next.data != value:
            current = current.next

        if current.next:
            current.next = current.next.next
            print(f"Deleted {value} from the list.")
        else:
            print(f"Value {value} not found.")

    def delete_first(self):
        """6. Deletes the first node."""
        if not self.head:
            print("List is already empty.")
            return
        self.head = self.head.next
        print("Deleted the first node.")

    def delete_last(self):
        if not self.head:
            print("List is already empty.")
            return
        if not self.head.next:
            self.head = None
            print("Deleted the last node.")
            return
            
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        print("Deleted the last node.")

    def count_nodes(self):
        """8. Counts the number of nodes."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print(f"Total number of nodes: {count}")

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")


def main():
    ll = LinkedList()
    
    while True:
        print("\n--- Linked List Operations Menu ---")
        print("1. Create linked list")
        print("2. Insert beginning")
        print("3. Insert end")
        print("4. Insert at specific index")
        print("5. Delete by value")
        print("6. Delete first node")
        print("7. Delete last node")
        print("8. Count number of nodes")
        print("9. Display / Traverse")
        print("10. Exit")
        
        choice = input("Enter your choice (1-10): ")
        
        if choice == '1':
            user_input = input("Enter numbers separated by spaces: ")
            values = [int(x) for x in user_input.split()]
            ll.create_list(values)
        elif choice == '2':
            data = int(input("Enter data to insert at beginning: "))
            ll.insert_beginning(data)
        elif choice == '3':
            data = int(input("Enter data to insert at end: "))
            ll.insert_end(data)
        elif choice == '4':
            index = int(input("Enter index (starts at 0): "))
            data = int(input("Enter data to insert: "))
            ll.insert_at_index(index, data)
        elif choice == '5':
            val = int(input("Enter value to delete: "))
            ll.delete_by_value(val)
        elif choice == '6':
            ll.delete_first()
        elif choice == '7':
            ll.delete_last()
        elif choice == '8':
            ll.count_nodes()
        elif choice == '9':
            ll.display()
        elif choice == '10':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")

if __name__ == "__main__":
    main()
