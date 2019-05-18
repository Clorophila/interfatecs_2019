d = 0
s = 0
e = 0

dan = []
sil = []

n = int(input())

for i in range(n):
    ca,cb,cc,cd = map(int,input().split())
    k = cd+1000*cc+1000000*cb+1000000000*ca
    
for i in range(n):
    ca,cb,cc,cd = map(int,input().split())
    k = cd+1000*cc+1000000*cb+1000000000*ca
    sil.append(k)
    sil.sort()

for i in range(n):
    if dan[i]>sil[i]:
        d += 1
    elif sil[i]>dan[i]:
        s += 1
    else:
        e += 1

print('danette venceu: {}'.format(d))
print('silvio venceu: {}'.format(s))
print('empates: {}'.format(e))