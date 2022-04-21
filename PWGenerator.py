from random import choice

#Nubmer Variable
numbers = '1234567890'
#lower case
lower = 'abcdefghijklmnopqrstuvwxyz'
#upper case
upper = lower.upper();
#other
other = '!"§$%&/()=?.,-_:;'
all = numbers + lower + upper + other
#create the password and print it
for x in range(1):
    print(''.join(choice(all) for x in range(12)))