import math

def taylor(x):
    r = x*((3.1415)/180)
    tay = 0
    for n in range(5):
        tay += ((-1)**n)*((r**(2*n))/math.factorial(2*n))
   
    quarta_casa = math.trunc(tay*10000) - 10*(math.trunc(tay*1000))

    if quarta_casa > 6:
        tay = round(tay,3)
    else:
        tay = math.trunc(tay*1000) / 1000

    return tay

print('{:.3f}'.format(taylor(float(input()))))