import math

def solution(n, s):
    answer = []
    k = s/n
    r = s%n
    
    if (s<n):
        answer = [-1]
        return answer
    
    for i in range(0, n-r):
        answer.append(math.floor(k))
    
    for i in range(0, r):
        answer.append(math.ceil(k))
    
    return answer
