def solution(phone_number):
    return '*'*(len(phone_number)-4) + phone_number[-4:]
#phone_number.replace(phone_number[0:-4], '*')