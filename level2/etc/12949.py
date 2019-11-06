def solution(arr1, arr2):
    #tmp = [0 for _ in range(len(arr2[0]))]
    #answer = [tmp for _ in range(len(arr1))]
    answer = [([0 for _ in range(len(arr2[0]))]) for _ in range(len(arr1))]
    print(answer)
    for k in range(len(arr1[0])): #2
        for i in range(len(arr1)): #3
            for j in range(len(arr2[0])):#3
                answer[i][j] += (arr1[i][k] * arr2[k][j])
    
    
    return answer



arr1=[[1, 4], [3, 2], [4, 1]]
arr2=[[1, 2], [3, 4]]
#arr1=[[2, 3, 2], [4, 2, 4], [3, 1, 4]]
#arr2=[[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr1,arr2))
