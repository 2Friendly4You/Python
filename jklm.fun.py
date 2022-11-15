import os
with open('deutsch_besser.txt') as f:
    lines = f.readlines()

lines = list(map(lambda x: x.lower(), lines))

for i in range(len(lines)):
    line = lines[i]
    if "oe" in line:
        line = line.replace("oe", "ö")
    if "ae" in line:
        line = line.replace("ae", "ä")
    if "ue" in line:
        line = line.replace("ue", "ü")
    lines[i] = line

print(lines)

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

while True:
    liste = []
    char = input()
    for line in lines:
        if char in line:
            liste.append(line)
    liste.sort(reverse=True, key=len)
    addToClipBoard(liste[0])
    hoch = 0
    for x in liste:
        if hoch < 10:
            print(x)
            hoch+=1