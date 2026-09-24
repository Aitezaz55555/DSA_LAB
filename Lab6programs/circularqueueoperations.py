class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
        self.size = size

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue Underflow")
        else:
            print("Deleted:", self.queue[self.front])
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size

    def peek(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[self.front])

    def display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print()
q = CircularQueue(5)

while True:
    print("\n1.Enqueue 2.Dequeue 3.Peek 4.Display 5.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        x = int(input("Value: "))
        q.enqueue(x)
    elif ch == 2:
        q.dequeue()
    elif ch == 3:
        q.peek()
    elif ch == 4:
        q.display()
    elif ch == 5:
        break
'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueueLL:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, data):
        new = Node(data)

        if self.front is None:
            self.front = self.rear = new
            self.rear.next = self.front
        else:
            self.rear.next = new
            self.rear = new
            self.rear.next = self.front

        print("Inserted:", data)
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return

        if self.front == self.rear:
            print("Deleted:", self.front.data)
            self.front = self.rear = None
        else:
            temp = self.front
            print("Deleted:", temp.data)
            self.front = self.front.next
            self.rear.next = self.front
    def peek(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Front element:", self.front.data)
    def display(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.front:
                break
        print("(front)")

q = CircularQueueLL()

while True:
    print("\n1.Enqueue 2.Dequeue 3.Peek 4.Display 5.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        x = int(input("Value: "))
        q.enqueue(x)
    elif ch == 2:
        q.dequeue()
    elif ch == 3:
        q.peek()
    elif ch == 4:
        q.display()
    elif ch == 5:
        break
    else:
        print("Invalid choice")'''
