f = open('2.txt').read()

ht = [0]
ic = 0
for i in f:
    if i=='^':
        if ic > 0:
            ic += 1
        else:
            ic = 1
        ht.append(ht[-1]+ic)                    
    if i=='v':
        if ic < 0:
            ic += -1
        else:
            ic = -1
        ht.append(ht[-1]+ic)
    
print(max(ht))
