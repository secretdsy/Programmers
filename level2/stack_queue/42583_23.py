def solution(bridge_length, weight, truck_weights):
    # answer = 0
    
    cnt = 0
    sum = 0
    # for i in range(1, len(truck_weights)):
    i = 0
    while(i<len(truck_weights)):
        if (sum+truck_weights[i] <= weight):
            # print('if', i)
            sum += truck_weights[i]
            cnt += 1
            # print('tr_wei', truck_weights[i])
            # print('ifcnt', cnt)
        else:
            # print('else', i)
            cnt += bridge_length
            sum = truck_weights[i]
            # print('tr_wei', truck_weights[i])
            # print('elsecnt', cnt)
        i+=1
    cnt+= bridge_length
            
            
    return cnt
