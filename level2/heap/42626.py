import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while (1):
        if scoville[0] > K:
            break
        elif len(scoville) == 1:
            answer = -1
            break
        else:
            a = (heapq.heappop(scoville))
            b = (heapq.heappop(scoville))
            heapq.heappush(scoville, (a + 2 * b))
            answer+=1
    return answer
