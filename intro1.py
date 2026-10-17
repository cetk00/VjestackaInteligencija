#kol 12.11
#popravni 19.11


x = 25
if 25 % 2 == 0:
    print(x, 'je paran broj')
else:
    print(x, 'je neparan broj')

i = 1
while i < 10:
    print(i, end= ' ')
    i += 1
print()

for i in range(1, 10):
    print(i, end= ' ')
print()

def kvadrat(x):
    return x ** 2

print(kvadrat(4))

#lista, torka, rjecnik, skup
#red, heap/priority q, counter, deque, ... 

#nije ulancana lista, vec dinamicki niz
a = [9, 12, 8, 27, 30, 16] #lista - uglaste zagrade
print(a[0], a[1], a[5])
a[0] = 5
print(a[0])
print(a[-1], a[-2])

#slicing
print(a[2:5])
print(a[:4], a[3:])
print(a[:]) #kopija liste
print(a[-2:])
print(a[1: :2]) #samo neparni indexi
print(a[-1:-3:-1]) 
print(a[::-1])

#preko slicing moze da ide i dodjela vrijednosti
#a je objekat klase list

a.append(10)
print(a)
a.pop()
print(a)
print(a.count(20), a.count(30))
print(a.index(27)) #ako ne postoji baci exception

#List comprehension
b = [x * 2 for x in a] #transformacija postojece liste
print(b)
c = [x for x in a if x % 2 == 0]
print(c)
d = [ [1, 2, 3], [4, 5, 6] ]
print(d)
print([['_' for j in range(3)]for i in range(3)])

#torke - imutable liste

e =  (1, 2, 3)
print(e, e[0], e[-1], e[1:])

#razlozi za imutabilnost se tice rjecnika, skupova...

def kvadrat_i_kub(x):
    return x ** 2, x ** 3

#raspakivanje

x2, x3 = kvadrat_i_kub(3)
print(x2, x3)

# konvencija: liste treba da budu homogene, a ako imamo potrebu da mijesamo tipove, preporucuju se torke

#rjecnik - kao mapa iz cpp
f = {'abc' : 123, 'xyz' : 555}

#kljuc moze da bude:int, float, boolean,...
#moze biti i imutable struktura: torke, string(preporuceno)

print(f['abc'])
f['abc'] = 125
print(f['abc'])

if 'aaa' in f:
    print(f['abc'])

#skupovi

g = {1, 2, 3, 4, 5}
print(g)

if 3 in g:
    print('postoji')
else:
    print('ne postoji')


g.add(6)
g.add(4) #ignorise jer je vec u skupu
print(g)

#skupovne operacije

#prolazi po strukturama

