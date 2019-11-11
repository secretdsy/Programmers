def solution(clothes):
    answer = 1 
    uni_list = []
    
    for i in range(0, len(clothes)):
        uni_list.append(clothes[i][1]) # 옷의 종류만 uni_list에 추가
    
    set_list = list(set(uni_list)) # 중복을 제거
    
    if (len(set_list) == 1): # 가진 옷의 종류가 1가지라면 전체 옷의 갯수 리턴
        return len(clothes)
    else:
        for val in set_list:
            # 각 종류의 갯수 + 안입는 경우를 모두 곱해주고, 모두 안입는 경우만 빼서 리턴
            answer *= (uni_list.count(val) + 1)    
        return answer-1


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))
