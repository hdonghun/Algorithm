def solution(phone_book):
    phone_book.sort()  # 전화번호를 정렬하여 접두어인 경우가 바로 뒤에 오도록 합니다.
    
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False  # 접두어인 경우가 발견되면 False를 반환합니다.
    
    return True  # 접두어인 경우가 없으면 True를 반환합니다.
