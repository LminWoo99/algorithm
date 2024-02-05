from collections import deque
a=[1,2,3,4,5]
dq_right=deque(a)
dq_left=deque(a)
dq_right.rotate(1)
dq_left.rotate(-1)
print(dq_right)
print(dq_left)
