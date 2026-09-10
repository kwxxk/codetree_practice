cnt_arr = [0] * 5
for i in range(3):
    cold, tem = input().split()
    if cold == 'Y' and int(tem) >= 37:
        cnt_arr[0] += 1
    elif cold == 'N' and int(tem) >= 37:
        cnt_arr[1] += 1
    elif cold == 'Y' and int(tem) < 37:
        cnt_arr[2] += 1
    else:
        cnt_arr[3] += 1
    if cnt_arr[0] >= 2:
        cnt_arr[-1] = 'E'
if cnt_arr[-1] == 0:
    cnt_arr.pop()
print(*cnt_arr)