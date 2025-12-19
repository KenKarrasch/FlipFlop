f = open('5-1.txt').read()

pl = {}

for i,lt in enumerate(f):
    if lt in pl.keys():
        pl[lt].append(i)
    else:
        pl[lt] = [i]

d = 0
tr = 0
while tr < len(f):
    if f[tr] in pl.keys():
        ptr = tr
        if tr == pl[f[tr]][0]:
            tr = pl[f[tr]][1]            
        else:
            tr = pl[f[tr]][0]        
        if ord(f[tr]) > ord('Z'):
            d += abs(ptr-tr)
        else:
            d -= abs(ptr-tr)
    tr += 1    
print(d)
