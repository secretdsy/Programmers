def solution(A, B):
    A.sort(reverse=True) # 내림차순으로 정렬
    B.sort(reverse=True)
    answer = 0
    i = 0 # A의 인덱스
    j = 0 # B의 인덱스
    while(i < len(A)):
        if (A[i] < B[j]): # B의 값이 더 크면 승리, 각각 다음 인덱스 비교
            answer+=1
            i+=1
            j+=1
        else: # B의 값이 작거나 같으면 A의 인덱스만 증가시켜서 못이긴 인덱스는 더이상 안봄
            i+=1
    return answer


a = [5,1,3,7]
b = [2,2,6,8]
print(solution(a,b))
# 2018 서머코딩
