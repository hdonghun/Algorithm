from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    # 한 글자 차이인지 확인하는 함수
    def one_letter_diff(word1, word2):
        return sum([c1 != c2 for c1, c2 in zip(word1, word2)]) == 1
    
    # BFS 초기화
    queue = deque([(begin, 0)])
    visited = set([begin])
    
    while queue:
        current_word, steps = queue.popleft()
        
        # target에 도달하면 현재까지의 변환 횟수 반환
        if current_word == target:
            return steps
        
        # 현재 단어에서 한 글자만 다른 단어들을 찾아 큐에 추가
        for word in words:
            if word not in visited and one_letter_diff(current_word, word):
                visited.add(word)
                queue.append((word, steps + 1))
    
    # target에 도달하지 못하면 변환 불가
    return 0