num = [6,10,2]
num = [str(num[i]) for i in range(len(num))]
num = sorted(num, reverse=True)
print(num)
#['99', '94', '9', '55', '5', '47', '44', '42', '34', '310', '30', '3', '10']

ans = []
max_num = 0
for idx, val in enumerate(num):
    if len(val) == 1:
        ans.append(val)
        num.remove(val)
k=0
for i in range(len(num)):
    #print("ans", (ans[0]))
    #print("num", (num[i][0]))
    try:
        if num[i][0] == ans[0]:
            num.insert(i, ans[0])
            del ans[0]
            print(ans)
            k+=1
    except IndexError:
        continue

    else:
        num.in

print(''.join(num))
#print(max_num)
#print(ans)
#print(num)
