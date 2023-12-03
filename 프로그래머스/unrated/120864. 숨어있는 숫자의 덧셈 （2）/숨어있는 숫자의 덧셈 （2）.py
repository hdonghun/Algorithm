import re
def solution(my_string):
    answer = 0
    result = ''
    
    result = re.sub(r"[^0-9]", " ",my_string) #re.sub으로 숫자만 남기기
    numbers = re.findall(r'\d+', result)
    for i in range(len(numbers)):
        answer += int(numbers[i])

    print(numbers)
            
    return answer