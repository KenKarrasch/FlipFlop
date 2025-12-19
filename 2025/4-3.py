f = [tuple(map(int,y.split(','))) for y in open('4.txt').read().split('\n')]

f = [(0,0)] + f

nf = []
for i in f:
    nf.append((i[0]+i[1],i[0],i[1]))

nf.sort()
    
d = 0
for i in range(len(nf)-1):
    dx = abs(nf[i][1] - nf[i+1][1])
    dy = abs(nf[i][2] - nf[i+1][2])    
    df = abs(dx-dy)
    d += min([dx,dy]) + df  

print(d)
