from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = set()
    
    while queue:
        word, level = queue.popleft()
        if word == target:
            return level
        
        for next_word in words:
            if next_word not in visited and sum(char1 != char2 for char1, char2 in zip(word, next_word)) == 1:
                visited.add(next_word)
                queue.append((next_word, level + 1))
                
    return 0