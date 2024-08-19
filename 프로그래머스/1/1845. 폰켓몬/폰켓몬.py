def solution(nums):
    # 중복을 제거한 폰켓몬 종류 수
    unique_pokemon_count = len(set(nums))
    
    # 최대 선택 가능한 폰켓몬 수 (전체의 절반)
    max_selectable = len(nums) // 2
    
    # 가능한 최대 종류의 폰켓몬을 선택할 수 있는 경우의 수
    return min(unique_pokemon_count, max_selectable)
