arr = input()
ee_exist = 'No'
ab_exist = 'No'
for i in range(len(arr)-1):
    if arr[i] +arr[i+1] == 'ee':
        ee_exist = 'Yes'
    if arr[i] + arr[i+1] == 'ab':
        ab_exist = 'Yes'

print(ee_exist,ab_exist, sep=' ')
