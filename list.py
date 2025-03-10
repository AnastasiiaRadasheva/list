from random import *
sõne = 'Programmeerimine'
print(sõne)
sõne_list = list(sõne)
print(sõne_list)
sõne_list.reverse()
print(sõne_list)
print(sõne_list.index('P'))
print(len(sõne_list))
print(len(sõne))
count = sõne_list.count('m')
for m in range(count):
    sõne_list.remove('m')
tähed = (randint(1,5))
for i in range(tähed):
    while 1:
        try:
            t=(input('sisesta täht: '))
            print(sõne_list)
            if t.isalpha(): break
        except: 
            
            dprint('oh vaja täht')
    sõne_list.append(t)


print(sõne_list)

for i in range(tähed):
    while 1:
        try:
            t = (input('sisesta täht: '))
            print(sõne_list)
            if t.isalpha(): break
        except: 
            print('oh vaja täht')
    while 1:
        try:
            ind = int((input('sisesta index: ')))
            if ind.isnumeric() & int(ind) < len(sõne_list):
                break
        except: 
            print('oh vaja index')
    sõne_list.insert(ind, t)



print(sõne_list)
sõne_list.sort(reverse=True)
