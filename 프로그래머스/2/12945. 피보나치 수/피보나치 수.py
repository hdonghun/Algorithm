def solution(n):
# 답안 작성 부분 ===============
    answer = 0
    k = n
    a = 0
    b = 1

    for i in range(n-1):
      k = (a) + (b)
      a = b
      b = k

    answer = k % 1234567


# ==============================
    return answer