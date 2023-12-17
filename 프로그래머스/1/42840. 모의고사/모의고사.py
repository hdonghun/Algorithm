def solution(answers):
    person_1 = [1, 2, 3, 4, 5] * ((len(answers) // 5) + 1)
    person_2 = [2, 1, 2, 3, 2, 4, 2, 5] * ((len(answers) // 8) + 1)
    person_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * ((len(answers) // 10) + 1)

    person1_answer = sum([1 for i in range(len(answers)) if answers[i] == person_1[i]])
    person2_answer = sum([1 for j in range(len(answers)) if answers[j] == person_2[j]])
    person3_answer = sum([1 for k in range(len(answers)) if answers[k] == person_3[k]])

    max_score = max(person1_answer, person2_answer, person3_answer)

    result = []
    if max_score == person1_answer:
        result.append(1)
    if max_score == person2_answer:
        result.append(2)
    if max_score == person3_answer:
        result.append(3)

    return result
