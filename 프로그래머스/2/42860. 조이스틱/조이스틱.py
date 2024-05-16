def solution(name):
    # 알파벳 별로 상하 조이스틱 조작 횟수 계산
    def get_move_count(char):
        return min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
    
    # 상하 이동 횟수의 총합 계산
    total_up_down = sum(get_move_count(char) for char in name)
    
    # 좌우 이동 횟수 계산
    length = len(name)
    min_move = length - 1
    for i in range(length):
        next_char_index = i + 1
        while next_char_index < length and name[next_char_index] == 'A':
            next_char_index += 1
        distance = min(i, length - next_char_index)
        min_move = min(min_move, i + length - next_char_index + distance)
    
    return total_up_down + min_move