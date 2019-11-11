def solution(budgets, M):
    answer = 0
    budgets.sort()
    N = len(budgets)
    
    if(sum(budgets) <= M):
        return budgets[-1]
    
    elif(budgets[0] > M//N):
        return M//N
    
    else:
        i=0
        n = N # 남은 사람의 수
        while(i<=N):
            if (i==N):
                # 모든 예산이 남은 예산의 평균보다 작아서 가장 큰 예산을 요구하는 도시까지 온 경우
                return M
            
            elif (budgets[i] < M//n):
                # 남은 예산의 평균값보다 작으면 전체 예산에서 요청한 예산 빼고 평균 값 구하기
                M-=budgets[i]
                n-=1
                i+=1
                
            elif (budgets[i] >= M//n):
                # 평균값보다 예산이 크거나 같으면 상한액은 평균값
                return M//n
                
    return answer



bg = [120,110,140,150]
m = 485
print(solution(bg, m))
