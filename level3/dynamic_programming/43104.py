def solution(N):
    answer = 0
    tile_list = [0 for _ in range(N)]
    tile_list[0] = 1
    tile_list[1] = 1
    for i in range(2, N): # 각 정사각형 타일 길이 리스트
        tile_list[i] = tile_list[i-2] + tile_list[i-1]
        
    answer = (tile_list[N-1] * 2 + tile_list[N-2]) * 2
    return answer


print(solution(5))
