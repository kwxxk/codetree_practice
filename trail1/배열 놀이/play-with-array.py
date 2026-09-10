n , q = map(int,input().split())
n_arr = list(map(int,input().split()))
for test_case in range(q):
    q_arr = list(map(int,input().split()))
    if q_arr[0] == 1:
        print(n_arr[q_arr[-1]-1])
    elif q_arr[0] == 2:
        idx = 0
        for i in range(n):
            if n_arr[i] == q_arr[-1]:
                idx = i +1
                break
        
        print(idx)
    else:
        print(*n_arr[q_arr[1]-1:q_arr[-1]])