def solution(s):
    answer = 0
    if s[0] == '-':
        return -int(s[1:])
    else:
        return int(s)