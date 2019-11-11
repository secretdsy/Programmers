def solution(n, words):
    answer = []
    tmp_list = [words[0]] # 앞에서 나온 단어를 저장하는 리스트
    for i in range(1, len(words)):
        if(words[i] in tmp_list): # 앞에서 나왔다면 종료
            break
        
        # 앞 단어의 끝문자와 현재 단어의 첫문자가 다르면 종료
        elif (words[i-1][-1] != words[i][0]):
            break
        tmp_list.append(words[i]) # 통과하면 리스트에 추가

    answer.append(i%n + 1) # 몇번째 사람인지
    answer.append(i//n + 1) # 몇번째 차례에 걸리는지

    if (i + 1) == len(tmp_list): # 처음부터 끝까지 모두 통과했다면 탈락자 없음
        answer = [0, 0]
    return answer

#N=3
#w=["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
#print(solution(N, w))
