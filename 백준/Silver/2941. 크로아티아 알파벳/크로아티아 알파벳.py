x = input()

temp = ['c=','c-','dz=','d-','lj','nj','s=','z=']
count = 0
i = 0

while i < len(x):
    if x[i:i+3] == 'dz=':  # "dz=" 우선 처리 (3글자)
        count += 1
        i += 3
    elif x[i:i+2] in temp:  # 나머지 2글자 크로아티아 알파벳 처리
        count += 1
        i += 2
    else:  # 일반 문자
        count += 1
        i += 1

print(count)
