arr= list(map(int,input().split()))
under_target_arr = []
upper_target_arr = []
for val in arr:
    if val < 500:
        under_target_arr.append(val)
    else: upper_target_arr.append(val)

print(max(under_target_arr) ,min(upper_target_arr))