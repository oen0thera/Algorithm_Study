# 2024.03.12 타노스는 요세푸스가 밉다

from collections import deque
n, k = map(int, input().split())
# n, k = 1007, 15
deque = deque(range(1, n+1))

while len(deque) != 1: 
    deque.rotate(-1)
    for i in range(1, k):
        deque.popleft()
        if len(deque) == 1:
            break
print(deque[0])