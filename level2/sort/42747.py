def solution(citations):
    answer = 0
    citations.sort()
    list_len = len(citations)
    for idx, val in enumerate(citations):
        # 남은 idx 개수보다 val값이 더 크면 val보다 큰 값은 검사할 필요가 없음
        if val > list_len - idx:
            return max(answer, list_len - idx)
        else:
            answer = val
    return answer

cit = [3, 0, 6, 1, 5]
print(solution(cit))
