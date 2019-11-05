def solution(name):    
    answer = 0
    cnt_front = 0
    cnt_back = 0
    name_len = len(name)
    half_len = (name_len - 1)//2
    for i in range(name_len):
        if (ord(name[i]) - ord("A") > 13) & (name[i] != "A"):
            answer += 26 - (ord(name[i]) - ord("A"))
            answer += 1
        elif (ord(name[i]) - ord("A") <= 13) & (name[i] != "A"):
            answer += ord(name[i]) - ord("A")
            answer += 1

    for i in range(0, half_len):
        if name[i] == "A":
            break
        cnt_front += 1
    for i in range(half_len, name_len, -1):
        if name[i] == "A":
            break
        cnt_back += 1

    return answer -1 + min(cnt_front, cnt_back)


na = "JEROEN"
na2 = "JAN"
print(solution(na))

