import math


def solution(n):
    answer = 1 # 한자리로 표현 가능한 경우
    k = math.ceil(n/2)

    # 입력된 수의 절반 이상의 수로는 표현 불가능하기 때문에 절반까지만 반복
    for i in range(1, k):
        sum = 0
        # 입력된 수가 홀수라면 (k-1)+k 는 항상 정답이기 때문에 k까지 반복
        for j in range(i, k+1):
            sum+=j
            if(sum > n):
                break
            elif(sum == n):
                answer+=1
                break            
    return answer

print(solution(15))
