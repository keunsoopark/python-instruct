from collections import deque

q = deque(["buffy", "gender", "willo"])
print(q)

q.append("xylis")
print(q)

print(q.popleft())
print(q.pop())
print(q)

q.appendleft("angel")
print(q)

# shift to right
q.rotate(1)
print(q)

q.rotate(4)
print(q)

# shift to left
q.rotate(-1)
print(q)


