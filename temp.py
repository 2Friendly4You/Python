def fak(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
        pr = round((i/n)*100, 2)
    return f



erg = 0
for i in range(0, 1001):
    erg+=1/fak(i)
print(erg)