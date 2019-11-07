def solution(n):
    answer = 1
    k = (n//2) + n%2
    if (n%2 == 0):
        answer += 1
    
    for i in range(1, k):
        a = max((n-2*i), i)
        b = min((n-2*i), i)
        answer += (a+1)*b
        
    
    
    return answer

for i in range (3, 10):
    print("i =", i)
    print("re=",solution(i))
