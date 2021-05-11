from collections import deque
import sys
input = sys.stdin.readline
queue = deque([])

def push_front(x):
    queue.appendleft(x)
def push_back(x):
    queue.append(x)
def pop_front():
    if len(queue) <= 0:
        print(-1)
    else:
        print(queue.popleft())
def pop_back():
    if len(queue) <= 0:
        print(-1)
    else:
        print(queue.pop())
def size():
    print(len(queue))
def empty():
    if len(queue) > 0 :
        print(0)
    else:
        print(1)
def front():
    if len(queue) <= 0 :
        print(-1)
    else:
        print(queue[0])
def back():
    if len(queue) <= 0 :
        print(-1)
    else:
        print(queue[-1])

N = int(input())

for _ in range(N):
    input_data = input().split()
    if len(input_data) > 1 :
        a,b = input_data[0], input_data[1]
    else:
        a = input_data[0]
    if a == 'push_back':
        push_back(b)
    elif a == 'push_front':
        push_front(b)
    elif a == 'pop_front':
        pop_front()
    elif a == 'pop_back':
        pop_back()
    elif a == 'front':
        front()
    elif a == 'back':
        back()
    elif a == 'size':
        size()
    elif a == 'empty':
        empty()