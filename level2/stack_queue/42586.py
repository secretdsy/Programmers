import math


def solution(progresses, speeds):
    day_list = [] #각 기능마다 완료까지 걸리는 기간 리스트
    answer = []
    cnt = 1
    for i in range(0,len(progresses)):
        day = math.ceil((100-progresses[i])/speeds[i]) #i번째 기능의 걸리는 기간
        if len(day_list) == 0:
            day_list.append(day)
        elif max(day_list) >= day:
            cnt += 1
            day_list.append(day)
        else: #max(day_list) < day
            answer.append(cnt)
            cnt = 1
            day_list = []
            day_list.append(day)
    answer.append(cnt)
    return answer

#progresses = [93,30,55]
#speeds = [1,30,5]
#print(solution(progresses, speeds))
