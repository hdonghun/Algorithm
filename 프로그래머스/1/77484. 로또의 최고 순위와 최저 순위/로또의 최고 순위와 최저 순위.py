def solution(lottos, win_nums):
    answer = []
    count = 0
    temp_count = 0
    
    for i in lottos:
        if i in win_nums:
            count += 1
    
    for j in lottos:
        if j == 0:
            temp_count += 1
    
    #return [7-(count+temp_count),7-count]
        # 최고 순위와 최저 순위 계산
    highest_rank = min(6,7 - (count + temp_count))
    lowest_rank =  min(6,7 - count)
    
    return [highest_rank, lowest_rank]