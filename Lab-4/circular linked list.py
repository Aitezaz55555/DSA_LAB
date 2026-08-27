class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class CircularLinkedList:
	def __init__(self):
		self.tail = None

	def create_list(self, values):
		self.tail = None
		for value in values:
			self.insert_at_end(value, show_message=False)
		print("Circular linked list created.")

	def insert_at_beginning(self, data, show_message=True):
		new_node = Node(data)
		if self.tail is None:
			self.tail = new_node
			new_node.next = new_node
		else:
			new_node.next = self.tail.next
			self.tail.next = new_node
		if show_message:
			print(f"Inserted {data} at the beginning.")

	def insert_at_end(self, data, show_message=True):
		new_node = Node(data)
		if self.tail is None:
			self.tail = new_node
			new_node.next = new_node
		else:
			new_node.next = self.tail.next
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

		if self.tail is None:
			print("Index out of bounds.")
			return

		current = self.tail.next
		for _ in range(index - 1):
			current = current.next
			if current == self.tail.next:
				print("Index out of bounds.")
				return

		if current == self.tail:
			self.insert_at_end(data)
			return

		new_node = Node(data)
		new_node.next = current.next
		current.next = new_node
		print(f"Inserted {data} at index {index}.")

	def delete_at_beginning(self):
		if self.tail is None:
			print("List is empty.")
			return
		data = self.tail.next.data
		if self.tail.next == self.tail:
			self.tail = None
		else:
			self.tail.next = self.tail.next.next
		print(f"Deleted {data} from the beginning.")

	def delete_at_last(self):
		if self.tail is None:
			print("List is empty.")
			return

		data = self.tail.data
		if self.tail.next == self.tail:
			self.tail = None
		else:
			current = self.tail.next
			while current.next != self.tail:
				current = current.next
			current.next = self.tail.next
			self.tail = current
		print(f"Deleted {data} from the last position.")

	def delete_at_index(self, index):
		if index < 0 or self.tail is None:
			print("Invalid index or empty list.")
			return
		if index == 0:
			self.delete_at_beginning()
			return

		previous = self.tail.next
		current = previous.next
		for _ in range(1, index):
			previous = current
			current = current.next
			if current == self.tail.next:
				print("Index out of bounds.")
				return

		if current == self.tail.next:
			print("Index out of bounds.")
			return
		if current == self.tail:
			self.delete_at_last()
			return

		previous.next = current.next
		print(f"Deleted {current.data} from index {index}.")

	def count_nodes(self):
		if self.tail is None:
			print("Number of nodes: 0")
			return

		count = 1
		current = self.tail.next
		while current != self.tail:
			count += 1
			current = current.next
		print(f"Number of nodes: {count}")

	def display(self):
		if self.tail is None:
			print("List is empty.")
			return

		elements = []
		current = self.tail.next
		while True:
			elements.append(str(current.data))
			current = current.next
			if current == self.tail.next:
				break
		print(" -> ".join(elements) + " -> head")

	def display_tail_to_head(self):
		if self.tail is None:
			print("List is empty.")
			return

		elements = []
		current = self.tail.next
		while True:
			elements.append(str(current.data))
			current = current.next
			if current == self.tail.next:
				break
		print(" <- ".join(reversed(elements)))

	def display_head_and_tail(self):
		if self.tail is None:
			print("List is empty.")
			return
		print(f"Head: {self.tail.next.data}")
		print(f"Tail: {self.tail.data}")


def main():
	linked_list = CircularLinkedList()

	while True:
		print("\n--- Circular Linked List Menu ---")
		print("1. Create a circular linked list")
		print("2. Insert at beginning")
		print("3. Insert at end")
		print("4. Insert at specific index")
		print("5. Delete at beginning")
		print("6. Delete at last")
		print("7. Delete at specific index")
		print("8. Count the number of nodes")
		print("9. Traverse and display")
		print("10. Print data from tail to head")
		print("11. Display head and tail")
		print("12. Exit")

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
			linked_list.display_tail_to_head()
		elif choice == "11":
			linked_list.display_head_and_tail()
		elif choice == "12":
			print("Exiting program.")
			break
		else:
			print("Invalid choice.")


if __name__ == "__main__":
	main()
