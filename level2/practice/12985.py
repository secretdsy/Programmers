def solution(n,a,b):
    answer = 1

    while(1):
        if (abs(a-b) == 1) & (max(a,b)%2 == 0):
            break
        else:
            answer+=1
            a = (a+1)//2
            b = (b+1)//2
    return answer

print(solution(8,4,7))
# 2017 팁스타운
