def solution(heights):
    answer = []
    for i in range(len(heights)-1, 0, -1):

        for j in range(i, 0, -1):
            if heights[i] < heights[j-1]:
                answer.append(j)
                break

            elif j==1:
                answer.append(0)

    answer.append(0)
    answer.reverse()

    return answer
