def solution(scoville, K):
    answer = 0
    while(1):
        scoville.sort(reverse=True)
        if(scoville[-1] > K):
            return answer
        elif(len(scoville) == 1):
            return -1
        else:
            a=scoville.pop()
            b=scoville.pop()
            scoville.append(a + 2 * b)
            answer+=1
            
    return -1

# 효율성 0
