
import pprint
import pyperclip
import random


l = '''a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z
1
2
3
4
5
6
7
8
9
_
_
$
#
_
&
11
12
39
100
28
48
'''

alphabet = l.split()
password = []
current_letter = ''


def generate_password(alphabet, number):
    global password
    for x in range(number):
        current_letter = random.choice(alphabet)

        if x % 2 == 0:
             password.append(current_letter.upper())
        else:
             password.append(current_letter.lower())
    
    password = ''.join(password)
    pyperclip.copy(password)
    






generate_password(alphabet, 25)
print('Password Generated:\t ' + password)