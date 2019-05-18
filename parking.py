temin = 100000
tsmax = -1

for n in range(int(input())):
    he, me, hs, ms = map(int,input().split())
    te = (he*60)+me
    ts = (hs*60)+ms
    if te < temin:
        temin = te
    if ts > tsmax:
        tsmax = ts

print(tsmax-temin)