def fak(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
        pr = round((i/n)*100, 2)
    return f

def binominal(n, k):
    return fak(n)/(fak(k)*fak(n-k))

def gc(correctNumber, fromNumber):
    return 1/(binominal(correctNumber, correctNumber)/binominal(fromNumber, correctNumber))

print(gc(5, 50)+gc(5, 45)+gc(5,30)+gc(6,30)+gc(4,60)+gc(4,40)+gc(4,35)+gc(6,20)+gc(3,20)+gc(3,12)+gc(2,10)+gc(2,8))
print(gc(6,49)-gc(6,45)-gc(6,40)-gc(6,30)-gc(6,29)-gc(6,25)-gc(6,16)-gc(6,15)-gc(6,13)-gc(6,10)-gc(6,9)+3)