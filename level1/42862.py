def solution(n, lost, reserve):
    lost_list =[]
    #여벌이 있지만 도난 당한 사람 lost_list에 추가
    for val in lost: 
        if val in reserve:
            reserve.remove(val)
            lost_list.append(val)
               
    #여벌이 있는 사람이 도난 당했다면 한 벌만 있기 때문에 여벌 목록에서 제거
    for val in lost_list:
        lost.remove(val)
        
    n -= len(lost) #수업 참가 가능한 학생은 (전체학생-도난당한 학생)
    
    for val in lost:
        if (val-1) in reserve: #앞 번호 학생이 여벌이 있는 경우
            reserve.remove(val-1)
            n+=1
        elif (val+1) in reserve:#뒷 번호 학생이 여벌이 있는 경우
            reserve.remove(val+1)
            n+=1
    answer = n      
    return answer

N = 5
lo = [2, 4]
res = [1, 3, 5]
print(solution(N, lo, res))
