import random
import time

# Deterministic Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


# Randomized Quick Sort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    p = random.randint(0, len(arr)-1)
    arr[0], arr[p] = arr[p], arr[0]

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return randomized_quick_sort(left) + [pivot] + randomized_quick_sort(right)


# Main Program
arr = list(map(int, input("Enter numbers: ").split()))

start = time.time()
a = quick_sort(arr.copy())
t1 = time.time() - start

start = time.time()
b = randomized_quick_sort(arr.copy())
t2 = time.time() - start

print("\nDeterministic Quick Sort:", a)
print("Time:", t1)

print("\nRandomized Quick Sort:", b)
print("Time:", t2)