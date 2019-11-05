def prime(n):
    if (n < 2):
        return False
    if (n == 2) or (n == 3):
        return True
    if (n % 2 == 0) or (n % 3 == 0):
        return False
    if (n < 9):
        return True
    
    k = 5
    l = n**0.5
    
    while(k<=l):
        if (n % k == 0) or (n % (k + 2) == 0):
            return False
        k+=6
    return True
    
def solution(numbers):
    answer = 0
    return answer



