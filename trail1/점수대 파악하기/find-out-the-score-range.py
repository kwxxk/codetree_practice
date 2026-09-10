arr = list(map(int,input().split()))
cnt_arr = [0] * 11
for val in arr:
    if val == 0:
        break
    idx = val // 10
    cnt_arr[idx] +=1
for i in range(10,0,-1):
    print(f"{10*i} - {cnt_arr[i]}")
