def isitPrime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False
    return True

primeList = []

for i in range(1, 10000000):
    if isitPrime(i):
        primeList.append(i)
        print(i)

print(primeList)