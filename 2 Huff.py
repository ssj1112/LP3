import heapq

freq = {'a':5, 'b':9, 'c':12, 'd':13, 'e':16, 'f':45}

heap = [[v, [k, ""]] for k, v in freq.items()]
heapq.heapify(heap)

while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)

    for x in left[1:]:
        x[1] = '0' + x[1]

    for x in right[1:]:
        x[1] = '1' + x[1]

    heapq.heappush(heap, [left[0]+right[0]] + left[1:] + right[1:])

print("Huffman Codes:")
for char, code in sorted(heap[0][1:], key=lambda x: x[0]):
    print(char, ":", code)

