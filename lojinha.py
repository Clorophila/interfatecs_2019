total = 0

for n in range(int(input())):
    q, p = map(float,input().split())
    total += q*p

print('{:.2f}'.format(total))