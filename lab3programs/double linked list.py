class Node:
	def __init__(self, data):
		self.data = data
		self.previous = None
		self.next = None


class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def create_list(self, values):
		self.head = None
		self.tail = None
		for value in values:
			self.insert_at_end(value, show_message=False)
		print("Doubly linked list created.")

	def insert_at_beginning(self, data, show_message=True):
		new_node = Node(data)
		if self.head is None:
			self.head = self.tail = new_node
		else:
			new_node.next = self.head
			self.head.previous = new_node
			self.head = new_node
		if show_message:
			print(f"Inserted {data} at the beginning.")

	def insert_at_end(self, data, show_message=True):
		new_node = Node(data)
		if self.tail is None:
			self.head = self.tail = new_node
		else:
			new_node.previous = self.tail
			self.tail.next = new_node
			self.tail = new_node
		if show_message:
			print(f"Inserted {data} at the end.")

	def insert_at_index(self, index, data):
		if index < 0:
			print("Invalid index.")
			return
		if index == 0:
			self.insert_at_beginning(data)
			return

		current = self.head
		for _ in range(index - 1):
			if current is None:
				print("Index out of bounds.")
				return
			current = current.next

		if current is None:
			print("Index out of bounds.")
			return
		if current.next is None:
			self.insert_at_end(data)
			return

		new_node = Node(data)
		new_node.previous = current
		new_node.next = current.next
		current.next.previous = new_node
		current.next = new_node
		print(f"Inserted {data} at index {index}.")

	def delete_at_beginning(self):
		if self.head is None:
			print("List is empty.")
			return
		data = self.head.data
		if self.head == self.tail:
			self.head = self.tail = None
		else:
			self.head = self.head.next
			self.head.previous = None
		print(f"Deleted {data} from the beginning.")

	def delete_at_last(self):
		if self.tail is None:
			print("List is empty.")
			return
		data = self.tail.data
		if self.head == self.tail:
			self.head = self.tail = None
		else:
			self.tail = self.tail.previous
			self.tail.next = None
		print(f"Deleted {data} from the last position.")

	def delete_at_index(self, index):
		if index < 0 or self.head is None:
			print("Invalid index or empty list.")
			return
		if index == 0:
			self.delete_at_beginning()
			return

		current = self.head
		for _ in range(index):
			if current is None:
				print("Index out of bounds.")
				return
			current = current.next

		if current is None:
			print("Index out of bounds.")
			return
		if current == self.tail:
			self.delete_at_last()
			return

		current.previous.next = current.next
		current.next.previous = current.previous
		print(f"Deleted {current.data} from index {index}.")

	def count_nodes(self):
		count = 0
		current = self.head
		while current is not None:
			count += 1
			current = current.next
		print(f"Number of nodes: {count}")

	def display(self):
		if self.head is None:
			print("List is empty.")
			return
		elements = []
		current = self.head
		while current is not None:
			elements.append(str(current.data))
			current = current.next
		print(" <-> ".join(elements))


def main():
	linked_list = DoublyLinkedList()

	while True:
		print("\n--- Doubly Linked List Menu ---")
		print("1. Create a doubly linked list")
		print("2. Insert at beginning")
		print("3. Insert at end")
		print("4. Insert at specific index")
		print("5. Delete at beginning")
		print("6. Delete at last")
		print("7. Delete at specific index")
		print("8. Count the number of nodes")
		print("9. Traverse and display")
		print("10. Exit")

		choice = input("Enter your choice: ")

		if choice == "1":
			values = input("Enter elements separated by spaces: ").split()
			linked_list.create_list(values)
		elif choice == "2":
			linked_list.insert_at_beginning(input("Enter data: "))
		elif choice == "3":
			linked_list.insert_at_end(input("Enter data: "))
		elif choice == "4":
			index = int(input("Enter index: "))
			data = input("Enter data: ")
			linked_list.insert_at_index(index, data)
		elif choice == "5":
			linked_list.delete_at_beginning()
		elif choice == "6":
			linked_list.delete_at_last()
		elif choice == "7":
			linked_list.delete_at_index(int(input("Enter index: ")))
		elif choice == "8":
			linked_list.count_nodes()
		elif choice == "9":
			linked_list.display()
		elif choice == "10":
			print("Exiting program.")
			break
		else:
			print("Invalid choice.")


if __name__ == "__main__":
	main()
