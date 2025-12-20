from functools import cache
f = [[int(r) for r in y.split()] for y in open('7.txt').read().split('\n')]

dr = [[1,0],[0,1]]

@cache
def score(pl,ed):    
    if pl == ed:
        return 1
    tly = 0
    for d in dr:
        np = (pl[0]+d[0],pl[1]+d[1]) 
        if 0 <= np[0] <= ed[0]:
            if 0 <= np[1] <= ed[1]:                
                tly += score(np,ed)
    return tly
    
t = 0
for i in f:    
    t += score((1,1),(i[0],i[1]))
print(t)
