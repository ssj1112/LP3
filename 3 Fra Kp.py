n = int(input("Enter number of items: "))

items = []
for i in range(n):
    p = int(input("Enter profit: "))
    w = int(input("Enter weight: "))
    items.append((p, w, p/w))

items.sort(key=lambda x: x[2], reverse=True)

capacity = int(input("Enter knapsack capacity: "))
total = 0

for p, w, r in items:
    if capacity >= w:
        total += p
        capacity -= w
    else:
        total += r * capacity
        break

print("Maximum Profit:", total)