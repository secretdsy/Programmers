def solution(arrangement):
    answer = 0
    cnt = 1
    tmp = 0
    for i in range(1, (len(arrangement) - 1)):
        if (arrangement[i-1] == '(') & (arrangement[i] == ')'):
            cnt-=1
            tmp = cnt
            answer += cnt
            if (cnt != tmp):
                answer -= 1
        elif (arrangement[i] == '('):
            cnt+=1
            if (tmp == cnt):
                answer += 1
        elif (cnt == 1) & (arrangement[i] == ')'):
            cnt-=1
            answer += tmp
        else:
            cnt-=1

        print("i", i , "cnt", cnt)
        print("tmp", tmp)
        print("ans", answer)



    return answer


ar = "()(((()())(())()))(())"
print(solution(ar))
