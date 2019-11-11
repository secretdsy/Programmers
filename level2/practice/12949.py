def solution(arr1, arr2):
    # 결과 리스트를 0으로 초기화
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    # matrix_size = (i,k) * (k,j) = (i,j)
    for k in range(len(arr1[0])):
        for i in range(len(arr1)):
            for j in range(len(arr2[0])):
                answer[i][j] += (arr1[i][k] * arr2[k][j])
    
    return answer


ar1=[[1, 4], [3, 2], [4, 1]]
ar2=[[1, 2], [3, 4]]
#ar1=[[2, 3, 2], [4, 2, 4], [3, 1, 4]]
#ar2=[[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(ar1, ar2))
