def solution(nums):
    answer = 0
    result = []
    # 0. 고르는 개수, 리스트 길이의 / 2 
      # 1. 가장 많은 원소가 어떤 건지 고르기
        # 2. 중복이 되지 않게, 최대한 다양한 포켓몬 고르기
    max_number = max(set(nums), key= nums.count)
    print("max_number", max_number)
    result = list(set(nums))
    print('result', result)
    
    if len(nums)/2 < len(result):
        answer = len(nums)/2
    else:
        answer = len(result)
    
    
    return answer