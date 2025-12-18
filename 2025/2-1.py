f = open('2.txt').read()

ht = [0]
for i in f:
    if i=='^':
        ht.append(ht[-1]+1)    
    if i=='v':
        ht.append(ht[-1]-1)

print(max(ht))
