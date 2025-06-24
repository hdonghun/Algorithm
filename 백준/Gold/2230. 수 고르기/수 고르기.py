## 처음 방법(시간초과)
# n, m = map(int, input().split())
# temp = []
# result = []

# for i in range(n):
    # temp.append(i)

# for j in range(n):
    # for k in range(n):
        # diff = temp[j] - temp[k]
        # if diff >= m:
            # result.append(diff)
# if result:
    # print(min(result))

    
## 방법 2
### 투 포인터 기법
import sys
input = sys.stdin.readline

def solution(n, m, arr):
    start, end = 0, 1
    min_ = sys.maxsize
    
    while start < n and end < n:
        calc = arr[end] - arr[start]
        if calc == m: return m
        if calc < m:
            end += 1
            continue
        start += 1
        min_ = min(min_, calc)
        
    return min_

n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input().rstrip()))

arr.sort()
print(solution(n, m, arr))







