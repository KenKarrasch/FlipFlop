f = open('1.txt').read().split('\n')

ct = 0
for ni in f:
    lct = 0
    i = ni
    if 'ne' not in i:        
        for j in range(len(i)-1):        
            if i[j:j+2] == 'ba' or i[j:j+2] == 'na':            
                lct += 1    
    ct += lct
    
print(ct)
