def solution(answers):
    answer = [] # 최종 리턴 리스트
    ans_list = [] # 1~3번 수포자가 각각 맞춘 갯수
    ans_dict = [{0:1,1:2,2:3,3:4,4:5},
                {0:2, 1:1, 2:2, 3:3, 4:2, 5:4, 6:2, 7:5},
                {0:3, 1:3, 2:1, 3:1, 4:2, 5:2, 6:4, 7:4, 8:5, 9:5}]
    for i in range(3):
        sub_list = [] # 리스트의 차이가 0이면 정답
        for j in range(len(answers)):
            len_ans = len(ans_dict[i])
            sub_list.append(ans_dict[i][j%len_ans])
            sub_list[j] = sub_list[j] - answers[j]
        ans_list.append(sub_list.count(0)) # 정답의 갯수를 ans_list에 삽입
    
    max_score = max(ans_list) # 가장 많이 맞힌 사람의 점수
    max_len = ans_list.count(max_score) # 최고득점이면서 동점자의 수


    #단독 1등이 아닌 경우
    if max_len != 1:
        #동점자의 수만큼 ans_list에서 index 확인
        for i in range(max_len):
            #반복할때마다 remove하므로 remove한 횟수를 더해줌
            answer.append(ans_list.index(max_score)+i+1)
            #list.index(i)는 가장 첫번째 index를 반환하므로 위에서 append한 index는 삭제
            ans_list.remove(max_score) 
    else:
        answer.append(ans_list.index(max_score)+1)
    
    return answer

ans = [1,2,3,4,5]
print(solution(ans))
