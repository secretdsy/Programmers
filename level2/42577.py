def solution(phone_book):
    p_len = 0 #번호의 길이
    for val in phone_book:
        cnt = 0
        for cmp_val in phone_book: #cmp_val -> val과 비교하고자 하는 번호
            p_len = len(val)
            if val == cmp_val[:p_len]: #맨 앞에서 val의 길이만큼만 비교
                cnt+=1
                if (cnt>1): #자기 번호 한 번은 검사하기 때문에 1보다 클 때 다른 번호의 접두어
                    answer = False
                    return answer
    answer = True
    return answer


#접두어가 있는 경우 False
phone = ["119", "97674223", "1195524421"]
print(solution(phone))
