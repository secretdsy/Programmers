def solution(budgets, M):
    answer = 0
    budgets.sort
    N = len(budgets)
    sum_bg = sum(budgets)
    under_sum = 0 # 평균이하 합
    
    if(sum_bg <= M):
        return budgets[-1]
    elif(budgets[0] > M//N):
        return M//N
    else:
        i=0
        n = N # 남은 사람의 수
        while(i<=N):
            if (i==N):
                # print("if", i)
                return min(M, budget[-1])
            
            if (budgets[i] <= M//n):
                M-=budgets[i]
                n-=1
                i+=1
                # print("con", M, n ,i)
                
            elif (budgets[i] > M//n):
                # print("elif", M//n, budgets[i], i)
                return min(M//n, budgets[i])
                
    return answer
