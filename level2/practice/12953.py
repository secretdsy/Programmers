def gcd(a,b):
    r = a%b
    while r > 0:
        a = b
        b = r
        r = a%b
    return b


def lcm(a,b):
    return a*b//gcd(a,b)


def solution(arr):
    arr.sort()
    k = lcm(arr[0],arr[1])
    i = 2
    
    while (i < len(arr)):
        k = lcm(k, arr[i])
        i+=1
    
    return k
