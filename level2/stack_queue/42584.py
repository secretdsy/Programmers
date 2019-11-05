def solution(prices):
    answer = []
    
    for i in range(len(prices)-1): # 처음부터 마지막 직전까지
        for j in range(i+1, len(prices)): # 다음 시간의 가격과 비교하기위해 i+1부터 마지막까지
            if(prices[i] > prices[j]): # 기준가격보다 이후의 가격이 작으면
                answer.append(j - i) # 비교한 가격의 인덱스 - 기준 가격의 인덱스
                break
                
            # 모든 값들이 기준가격보다 작지 않아서 마지막 인덱스까지 오게 된 경우
            elif(j == (len(prices)-1)):
                answer.append(len(prices)-(i+1)) # 전체 길이에서 시작한 위치만큼 빼줌
    answer.append(0) # 마지막 인덱스는 비교할 가격이 없으므로 0
    return answer


pr = [1, 2, 3, 4, 5]
print(solution(pr))


# 효율성 통과못한 코드
# def solution(prices):
#     answer = []
    
#     for i in range(len(prices)-1):
#     # for idx, pr in enumerate(prices):
#         if min(prices[i+1:]) >= prices[i]:
#             answer.append(len(prices) - (i + 1))
#         else:
#             k = i + 1
#             while(prices[i] <= prices[k]):
#                 k+=1
#             answer.append(k - i)
#     answer.append(0)
#     return answer
