from collections import deque

def aaa(log):
    left = deque()
    right = deque()
    
    for ch in log:
        if ch == '-':
            if left:
                left.pop()
        elif ch == '<':
            if left:
                right.appendleft(left.pop())
        elif ch == '>':
            if right:
                left.append(right.popleft())
        else:
            left.append(ch)
    
    return ''.join(left) + ''.join(right)

ttt = int(input())

for _ in range(ttt):
    print(aaa(input().strip()))
