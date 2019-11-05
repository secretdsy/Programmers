def solution(brown, red):
    answer = []
    i = 3 # 가로, 세로는 최소(3, 3)
    j = 3
    while(i<brown): # 전체 카펫의 크기가 될 수 있는 (i, j) 중 i 오름차순
        if (brown+red) % i == 0: # 나누어 떨어질 때
            j = (brown+red)//i # ex: i=3 -> j=8 이고 red의 크기는 (i-2)*(j-2)
            if ((i-2)*(j-2) == red): # ex: (3-1)*(8-2) = 6 != 24
                answer.append(i)
                answer.append(j)
                break
        i+=1

    answer.reverse()

    return answer


br = 24
re = 24
print(solution(br,re))
