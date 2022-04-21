n = int(input('Fakultät von n = '))
f = 1
for i in range(1, n + 1):
    f *= i
    pr = round((i/n)*100, 2)
    if pr - round(pr) == 0:
        print("{:.0f}%".format((i/n)*100))
print(f'{n}! = {f}')