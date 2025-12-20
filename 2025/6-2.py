f = [[int(r) for r in y.split(',')] for y in open('6.txt').read().split('\n')]

sky = 1000

p = []
tly = 0
for i in range(len(f)):
    p.append([0,0])
for i in range(1000):  
    for i,ps in enumerate(f):
        p[i][0] += 3600*ps[0]
        p[i][1] += 3600*ps[1]          
    for i in p:
        if sky//4 <= i[0]%sky < 3*sky//4:
            if sky//4 <= i[1]%sky < 3*sky//4:
                tly += 1

print(tly)
