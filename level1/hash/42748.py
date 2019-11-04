def solution(array, commands):
    answer = []
    tmp_arr = []
    com_len = len(commands)
    
    for i in range(0, com_len):
        tmp_arr = array[commands[i][0]-1:commands[i][1]]
        tmp_arr.sort()
        answer.append(tmp_arr[commands[i][2]-1])
    return answer


arr = [1, 5, 2, 6, 3, 7, 4]
com = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(arr, com))

#[1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. 
#[2, 3, 5, 6]의 세 번째 숫자는 5입니다.
#[1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. 
#[6]의 첫 번째 숫자는 6입니다.
#[1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. 
#[1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.
