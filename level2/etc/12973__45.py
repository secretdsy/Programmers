def solution(string):
    answer = 0 
    s = []
    for i in string:
        s.append(i)

    while(len(s) > 0): 
        i = 0            
        while(i < len(s)-1):
            if (s[i] == s[i+1]):
                del s[i+1]
                del s[i]
                continue

            if (i==len(s)-2):
                break
            i+=1

        if (len(s) == 0):
            return 1

        if (len(s) == 2): 
            if (s[0] == s[1]):
                return 1

        if (len(s)-1 == i):
            return 0
        else:
            break

    return answer

print('----')
print(solution('safjbhdskjafhsd'))
print('----')
print(solution('a'))
print('----')
print(solution('baabaa'))
print('----')
print(solution('abc'))
print('----')
print(solution('aaaa'))
print('----')
print(solution('abbaaa'))
