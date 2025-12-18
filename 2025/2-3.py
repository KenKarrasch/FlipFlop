f = open('2.txt').read()

f =  f + 'e'

fb = []

def fib(n):
    nm = 1
    sq = [0,1]
    while nm < n:
        sq.append(sq[-1]+sq[-2])
        nm += 1
    return sq[-1]

ht = [0]
fc = 0
bc = 0
for ri in range(len(f)-1):
    i = f[ri]
    if i=='^':
        if fc > 0:
            fc += 1                
        else:
            fc = 1
        bc = 0
    if i=='v':
        if bc > 0:
            bc += 1                
        else:
            bc = 1
        fc = 0
    if i != f[ri+1]:
        if fc > 0:
            ht.append(ht[-1]+fib(fc))
        if bc > 0:
            ht.append(ht[-1]-fib(bc))        
print(max(ht))
