def solution(arr):
    answer = 0 
    cnt = 1 
    for i in range(1, len(arr)): # 무조건 '('로 시작
        if (arr[i] == '('):
            cnt+=1
        elif (arr[i] == ')'):
            cnt-=1
            if (arr[i-1] == '('): # 직전이 '('인 경우 레이저
                answer += cnt
            else: # 연속으로 ')'가 나오는 경우 
                answer += 1 # 중간에 끊기거나 막대기의 끝

    return answer
