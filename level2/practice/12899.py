def solution(n):
    answer = []
    if n == 1:
        return '1'
    while(n != 0):
        b = (n-1)%3
        n = (n-1)//3
        answer.append(b)
    answer.reverse()
    answer = list(map(str, answer))
    answer = ''.join(answer)
    answer = answer.replace('2','4')
    answer = answer.replace('1','2')
    answer = answer.replace('0','1')
    return answer
