f = open('3.txt').read().split('\n')

cl = {}

for i in f:
    c = tuple([int(x) for x in i.split(',')])
    if c in cl:
        cl[c] += 1
    else:
        cl[c] = 1

max([y for x,y in cl.items()])

mx = []
for i in cl.items():
    mx.append((i[1],i[0]))
              
mx.sort()
ans = mx[-1]
st = ''
for i in ans[1]:
    st = st + str(i) + ','
print(st)
