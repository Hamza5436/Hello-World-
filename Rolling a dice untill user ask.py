import random


a=random.randint(1,6)
print(a)
print('-----------------------------------------')
print('if you want to roll a dice again press y ')
print('If you want to stop press n')
print('-----------------------------------------')
c=(input('Enter y/n: '))

while c=='y':
    d=random.randint(1,6)
    print(d)
    c=input('Enter y/n: ')




