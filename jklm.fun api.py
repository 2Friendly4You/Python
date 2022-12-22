import os
from flask import Flask, request, abort

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

#print(lines)
print('Done')

app = Flask(__name__)

@app.route('/word')
def word():
    chars = request.args.get('contains')
    try:
        number = int(request.args.get('number'))
    except:
        number = 1
    print(number)
    if not chars:
        abort(400, {'error': 'Missing contains parameter'})
    if number < 1:
        abort(400, {'error': 'Number must be bigger or equal to 1'})
    chars = chars.lower()
    liste = []
    for line in lines:
        if chars in line:
            liste.append(line)
    liste.sort(reverse=True, key=len)
    if len(liste) >= number:
        print(liste[number-1])
        return f'{liste[number-1]}'
    abort(400, {'error': 'No word was found'})

if __name__ == '__main__':
    app.run()
