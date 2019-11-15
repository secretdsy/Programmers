def solution(s):
    answer = 0
    int_s = []
    for i in s.split():
        int_s.append(int(i))
    s_min = min(int_s)
    s_max = max(int_s)
    answer = str(s_min) + ' ' + str(s_max)
    return answer
