import time
# Non-Recursive Function
def fibonacci_non_recursive(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

# Recursive Function
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Main Program
n = int(input("Enter the number of terms: "))

# Non-Recursive Method
print("\nNon-Recursive Fibonacci Series:")
fibonacci_non_recursive(n)

print("\nTime Complexity: O(n)")
print("Space Complexity: O(1)")

print("\nRecursive Fibonacci Series:")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")

print("\nTime Complexity: O(2^n)")
print("Space Complexity: O(n)")