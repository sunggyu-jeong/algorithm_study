basketLength, count = input().split(" ")
basket = [0 for i in range(int(basketLength))]

for _ in range(int(count)):
  start, end, number = map(int,input().split(" ")) 
  basket[start-1:end] = [number] * (end - start + 1)

print(' '.join(map(str, basket)))
