def solution(skill, skill_tree):
    answer = len(skill_tree) # 모든 스킬트리 갯수에서 안되는 스킬 트리를 빼는 방식
    for sk_tr in skill_tree: # 스킬트리 갯수만큼
        for i in range(len(skill)-1): # 스킬 길이의 -1만큼
            # 앞에 스킬이 선행되지않고 뒤에 스킬이 있으면 불가능
            if (skill[i] not in sk_tr) & (skill[i+1] in sk_tr): 
                answer -= 1
                break

            # 선행되어야 할 스킬 인덱스가 더 크다면 불가능
            elif (skill[i] in sk_tr) & (skill[i+1] in sk_tr):
                if sk_tr.index(skill[i]) > sk_tr.index(skill[i+1]):
                    answer -= 1
                    break
            # 스킬트리에 스킬이 존재하지 않거나 선행 스킬만 있는 경우에는 가능
    return answer


sk = "CBD"
st = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(sk, st))
