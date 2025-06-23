# 수열에서 연속 구간을 잡을 때 그 안에 홀수가 K개 이하로만 포함되면, 
# 그 구간에서 홀수를 모두 삭제한 뒤 남는 짝수들의 길이가 최대가 되도록 하는 것
# 투 포인터(슬라이딩 윈도우) 기법
# 구간 내 홀수 개수를 세면서 구간을 확장하거나 줄여가며 최대 길이를 찾는 게 핵심


import sys

N, K = map(int, input().split())
S = list(map(int, input().split()))

left = 0
odd_count = 0
max_length = 0

for right in range(N):
    if S[right] % 2 == 1:
        odd_count += 1

    while odd_count > K:
        if S[left] % 2 == 1:
            odd_count -= 1
        left += 1

    # 현재 구간에서 짝수만 남기는 길이
    max_length = max(max_length, (right - left + 1) - odd_count)

print(max_length)



# left	right	구간	odd_count	남는 짝수 구간	길이
# 0	    2	   1 2 3	2	          2	          1
# 0	    3	   1 2 3 4	2	         2 4	      2
# 1	    5	 2 3 4 5 6	2	        2 4 6	      3
# 3	    7	 4 5 6 7 8	2	        4 6 8	      3
