'''def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

a = []
while True:
    elem = input("Enter an element (or enter stop to finish):- ")
    if elem.lower() == "stop":
        break
    a.append(int(elem))

print("Original List:", a)
sorted_list = bubble_sort(a)
print("Sorted List:  ", sorted_list)'''
'''def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

a = []
while True:
    elem = input("Enter an element (or enter stop to finish):- ")
    if elem.lower() == "stop":
        break
    a.append(int(elem))

print("Original List:", a)
sorted_list = insertion_sort(a)
print("Sorted List:  ", sorted_list)'''
'''def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

a = []
while True:
    elem = input("Enter an element (or enter stop to finish):- ")
    if elem.lower() == "stop":
        break
    a.append(int(elem))

print("Original List:", a)
sorted_list = selection_sort(a)
print("Sorted List:  ", sorted_list)'''
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

a = []
while True:
    elem = input("Enter an element (or enter stop to finish):- ")
    if elem.lower() == "stop":
        break
    a.append(int(elem))

print("Original List:", a)
sorted_list = merge_sort(a)
print("Sorted List:  ", sorted_list)



