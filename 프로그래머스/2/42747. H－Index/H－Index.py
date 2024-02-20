def solution(citations):
    citations.sort()  # 논문 인용 횟수를 오름차순으로 정렬
    n = len(citations)
    
    h_index = 0
    for i in range(n):
        if citations[i] >= n - i:  
            print('citations[i]',citations[i])
        # 현재 논문의 인용 횟수가 나머지 논문의 개수보다 크거나 같으면
            h_index = n - i  # h_index를 갱신
            break
    
    return h_index
