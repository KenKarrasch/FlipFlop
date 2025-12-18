f = open('3.txt').read().split('\n')

cl = []

for i in f:
    c = tuple([int(x) for x in i.split(',')])
    cl.append(c)

rd = 0
gr = 0
bl = 0
sp = 0

for i in cl:
    if len(set(i)) != len(i):
        sp += 1         
    if i[0] > i[1] and i[0] > i[2] and len(set(i)) == len(i):
        rd += 1        
    if i[1] > i[0] and i[1] > i[2] and len(set(i)) == len(i):
        gr += 1        
    if i[2] > i[0] and i[2] > i[1] and len(set(i)) == len(i):
        bl += 1

print(gr)
