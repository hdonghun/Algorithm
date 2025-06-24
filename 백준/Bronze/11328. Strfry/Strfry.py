from collections import Counter
import sys

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])  # 테스트 케이스 개수

for i in range(1, n + 1):
    a, b = data[i].split()
    if Counter(a) == Counter(b):
        print("Possible")
    else:
        print("Impossible")
