def solution(skill, skill_tree):
    answer = len(skill_tree) # 모든 스킬트리 갯수에서 안되는 스킬 트리를 빼는 방식
    for sk_tr in skill_tree: # 스킬트리 갯수만큼
        for i in range(len(skill)-1): # 스킬 길이의 -1만큼
            # 앞에 스킬이 선행되지않고 뒤에 스킬이 있으면 불가능한 스킬트리(-1)
            if (skill[i] not in sk_tr) & (skill[i+1] in sk_tr): 
                answer -= 1
                break

            try:
                # 선행되어야 할 스킬 인덱스가 더 크다면 (뒤에있다면) 불가능
                if sk_tr.index(sk[i]) > sk_tr.index(sk[i+1]):
                    answer -= 1
                    break
            except ValueError: # list.index(a) --> list에 a가 존재하지 않으면 error발생
                continue
    return answer


sk = "CBD"
st = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(sk, st))
