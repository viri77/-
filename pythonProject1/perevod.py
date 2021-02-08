n = '1AF2'
k=[]
s = 0
p = [n[i] for i in range(len(n))]
print(p)
for i in range(len(p)):
    if p[i] =='A':
        k.append('10')
    elif p[i]=='F':

         k.append('15')
    else:
        k.append(p[i])
print(*k)

for i in range (len(k)):
    s +=int(k[i])*16**(len(n)-1-i)

print(s)


