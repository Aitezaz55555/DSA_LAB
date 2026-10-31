SIZE = 11
EMPTY = None
DELETED = "DELETED"

print("HASH FUNCTIONS")
print("1. Index Mapping")
print("2. Division Method")
print("3. Mid-Square Method")
print("4. Digit Folding Method")
print("5. Multiplication Method")

hf = int(input("Select hash function: "))
print("\nCOLLISION RESOLUTION")
print("1. Separate Chaining")
print("2. Linear Probing")
print("3. Quadratic Probing")
print("4. Double Hashing")

cr = int(input("Select collision method: "))

table = [[] for i in range(SIZE)] if cr == 1 else [EMPTY] * SIZE

def hash_function(key):
    if hf == 1:
        return key % SIZE

    elif hf == 2:
        return key % SIZE

    elif hf == 3:
        square = str(key * key)
        width = len(str(SIZE - 1))
        start = max(0, (len(square) - width) // 2)
        return int(square[start:start + width]) % SIZE

    elif hf == 4:
        s = str(key)
        parts = [int(s[i:i + 3]) for i in range(0, len(s), 3)]
        return sum(parts) % SIZE

    elif hf == 5:
        c = 0.618
        product = key * c
        fraction = product - int(product)
        return int(SIZE * fraction)


def second_hash(key):
    return 7 - (key % 7)

def find_index(key):
    index = hash_function(key)

    for i in range(SIZE):
        if cr == 1:
            return index

        elif cr == 2:
            pos = (index + i) % SIZE

        elif cr == 3:
            pos = (index + i * i) % SIZE

        else:
            pos = (index + i * second_hash(key)) % SIZE

        if table[pos] is EMPTY:
            return pos

        if table[pos] == DELETED:
            continue

        if table[pos][0] == key:
            return pos

    return -1

def insert(key, value):
    index = hash_function(key)

    if cr == 1:
        for i in range(len(table[index])):
            if table[index][i][0] == key:
                table[index][i] = (key, value)
                print("Value updated.")
                return

        table[index].append((key, value))
        print("Element inserted.")

    else:
        pos = find_index(key)

        if pos == -1:
            print("Hash table is full.")
            return

        if table[pos] is not EMPTY and table[pos] != DELETED:
            table[pos] = (key, value)
            print("Value updated.")
        else:
            table[pos] = (key, value)
            print("Element inserted.")

    if load_factor() > 0.7:
        rehash()

def search(key):
    index = hash_function(key)

    if cr == 1:
        for k, v in table[index]:
            if k == key:
                print("Key found. Value:", v)
                return

    else:
        for i in range(SIZE):
            if cr == 2:
                pos = (index + i) % SIZE
            elif cr == 3:
                pos = (index + i * i) % SIZE
            else:
                pos = (index + i * second_hash(key)) % SIZE

            if table[pos] is EMPTY:
                break

            if table[pos] != DELETED and table[pos][0] == key:
                print("Key found. Value:", table[pos][1])
                return

    print("Key not found.")

def delete(key):
    index = hash_function(key)

    if cr == 1:
        for i in range(len(table[index])):
            if table[index][i][0] == key:
                table[index].pop(i)
                print("Element deleted.")
                return

    else:
        for i in range(SIZE):
            if cr == 2:
                pos = (index + i) % SIZE
            elif cr == 3:
                pos = (index + i * i) % SIZE
            else:
                pos = (index + i * second_hash(key)) % SIZE

            if table[pos] is EMPTY:
                break

            if table[pos] != DELETED and table[pos][0] == key:
                table[pos] = DELETED
                print("Element deleted.")
                return

    print("Key not found.")

def display():
    print("\nHASH TABLE")

    for i in range(SIZE):
        print(i, ":", table[i])

def load_factor():
    if cr == 1:
        count = sum(len(bucket) for bucket in table)
    else:
        count = sum(
            1 for item in table
            if item is not EMPTY and item != DELETED
        )

    return count / SIZE
def rehash():
    global SIZE, table

    old_table = table

    SIZE = SIZE * 2 + 1

    if cr == 1:
        table = [[] for i in range(SIZE)]
    else:
        table = [EMPTY] * SIZE

    if cr == 1:
        for bucket in old_table:
            for key, value in bucket:
                insert_without_rehash(key, value)
    else:
        for item in old_table:
            if item is not EMPTY and item != DELETED:
                insert_without_rehash(item[0], item[1])

    print("Hash table rehashed. New size:", SIZE)
def insert_without_rehash(key, value):
    index = hash_function(key)

    if cr == 1:
        table[index].append((key, value))

    else:
        for i in range(SIZE):
            if cr == 2:
                pos = (index + i) % SIZE
            elif cr == 3:
                pos = (index + i * i) % SIZE
            else:
                pos = (index + i * second_hash(key)) % SIZE

            if table[pos] is EMPTY:
                table[pos] = (key, value)
                return
while True:
    print("\n===== HASH TABLE OPERATIONS =====")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Load Factor")
    print("6. Rehash")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        value = input("Enter value: ")
        insert(key, value)

    elif choice == 2:
        key = int(input("Enter key to search: "))
        search(key)

    elif choice == 3:
        key = int(input("Enter key to delete: "))
        delete(key)

    elif choice == 4:
        display()

    elif choice == 5:
        print("Load Factor:", load_factor())

    elif choice == 6:
        rehash()

    elif choice == 7:
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")
