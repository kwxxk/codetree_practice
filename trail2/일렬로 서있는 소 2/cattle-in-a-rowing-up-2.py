n = int(input())
A = list(map(int, input().split()))
cnt=0
# Please write your code here.
for a1 in range(n-2):
    for a2 in range(a1+1,n):
        for a3 in range(a2+1,n):
            if A[a1] <= A[a2] and A[a2] <= A[a3]:
                cnt+=1

print(cnt)