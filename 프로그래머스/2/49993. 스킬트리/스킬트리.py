def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        idx = 0
        flag = True  # 올바른 순서로 배웠는지 확인하는 플래그
        for s in tree:
            if s in skill:
                if s != skill[idx]:  # 올바른 순서가 아니라면
                    flag = False
                    break
                else:
                    idx += 1
        if flag:  # 올바른 순서로 배웠다면
            answer += 1

    return answer
