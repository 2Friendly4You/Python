import os
with open('deutsch.txt') as f:
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
    lines[i] = line#

# open file in write mode
with open(r'C:/Programmieren/Python/deutsch_besser.txt', 'w') as fp:
    for item in lines:
        # write each item on a new line
        if len(item) < 18:
            fp.write("%s" % item)
    print('Done')