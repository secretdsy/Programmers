def solution(people, limit):
    answer = 0
    i=1
    tmp=0
    print(peo)

    while(len(people)!=0):
        if (len(people) == 1):
            answer += 1
            print("remove", people)
            return answer

        if (limit - people[0] < 40):
            print("p0", people[0])
            people.remove(people[0])
            print("remove", people)
            i=1
            answer += 1
            continue
        print(i)
        max_limit = people[0] + people[i]
        if (max_limit == limit):
            print("pi, p0", people[0],people[i])
            p0=people[0]
            p1=max_limit-p0
            people.remove(p0)
            people.remove(p1)
            print("remove", people)
            i=1
            answer += 1
            continue

        if (max_limit < limit):
            i+=1
            tmp = max(max_limit, tmp)
            
            if (i==len(people)):
                p0=people[0]
                p1=tmp-p0
                print("p0, p1", p0,p1)
                people.remove(p0)
                people.remove(p1)
                answer += 1
                print("remove", people)
                i=1
            continue

        elif (max_limit > limit):
            i+=1
            if (i==len(people)):
                print("p0", people[0])
                people.remove(people[0])
                answer += 1
                print("remove", people)
                i=1
            continue

    return answer

#peo = [70,40,50,60]
#peo = [70,80,50]
#peo = [40,40 ,50,60,40,80,90,80,100,60,50]
peo =[100,100,40,40,55,50,90,40,60,50]
li = 100
print(solution(peo, li))
