def solution(s):
    answer = True
    i = 0
    j = 0
    for val in s:
        if i < j:
            return False
        elif val == '(':
            i+=1
        # elif val == ')':
        else:
            j+=1
    if i != j:
        answer = False
        
    return answer
