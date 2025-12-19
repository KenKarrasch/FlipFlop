f = [tuple(map(int,y.split(','))) for y in open('4.txt').read().split('\n')]

f = [(0,0)] + f

d = 0
for i in range(len(f)-1):
    dx = abs(f[i][0] - f[i+1][0])
    dy = abs(f[i][1] - f[i+1][1])    
    df = abs(dx-dy)
    d += min([dx,dy]) + df

print(d)
