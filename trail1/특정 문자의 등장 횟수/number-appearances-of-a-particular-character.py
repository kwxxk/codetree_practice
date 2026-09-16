word = input()
ee_cnt = 0
eb_cnt = 0

for i in range(len(word)-1):
    if word[i]+word[i+1] == 'ee':
        ee_cnt+=1
    if word[i]+word[i+1] == 'eb':
        eb_cnt+=1

print(ee_cnt,eb_cnt)