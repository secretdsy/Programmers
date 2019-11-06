def solution(people, limit):
    answer = 0 
    i = 0 
    j = len(people) - 1
    people.sort()

    while(i<=j):
        if(people[i] + people[j] > limit):
            answer += 1
            j-=1
        elif(people[i] + people[j] <= limit):
            answer += 1
            i+=1
            j-=1
        else:
            answer +=1 
    return answer


peo =[100,100,40,40,55,50,90,40,60,50]
li = 100
print(solution(peo, li))
