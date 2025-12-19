f = open('5.txt').read()

pl = {}

for i,lt in enumerate(f):
    if lt in pl.keys():
        pl[lt].append(i)
    else:
        pl[lt] = [i]
d = 0
tr = 0
seen = [0]
while tr < len(f):
    if f[tr] in pl.keys():
        ptr = tr
        if tr == pl[f[tr]][0]:
            tr = pl[f[tr]][1]            
        else:
            tr = pl[f[tr]][0]        
        d += abs(ptr-tr)        
    seen.append(tr)
    tr += 1
    seen.append(tr)    

st = ''
for i,lt in enumerate(f):
    if i not in seen:
        if lt not in st:
            st = st + lt

print(st)
