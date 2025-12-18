f = open('1.txt').read().split('\n')

ct = 0
for i in f:
    lct = 0
    for j in range(len(i)-1):
        if i[j:j+2] == 'ba' or i[j:j+2] == 'na'or i[j:j+2] == 'ne':
            ct += 1
            lct += 1
   
print(ct)
