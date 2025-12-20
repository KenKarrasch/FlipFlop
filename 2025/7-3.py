from functools import cache
f = [[int(r) for r in y.split()] for y in open('7-1.txt').read().split('\n')]

@cache
def score(pl,ed):    
    if pl == ed:
        return 1
    tly = 0
    for d in range(len(ed)):
        np = []
        for i in range(len(pl)):
            if i != d:
                np.append(pl[i])
            else:
                np.append(pl[i]+1)
        npp = tuple(np)        
        gd = True
        for d in range(len(ed)):            
            if not(0 <= npp[d] <= ed[d]):    
                gd = False
        if gd:
            tly += score(npp,ed)
    return tly
    
t = 0
for i in f:        
    t += score((1,)*i[0],(i[1],)*i[0])
print(t)
