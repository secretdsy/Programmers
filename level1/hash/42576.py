def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(0, len(completion)):
        if completion[-1] == participant[-1]:
            participant.pop()
            completion.pop()
        else:
            return participant[-1]
        
    answer = participant[0]
    return answer


#part = ["leo", "kiki", "eden"]
#comp = ["eden", "kiki"]
#print(solution(part, comp))
