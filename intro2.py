a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a & b)
print(a | b)
print(a - b)
print(b - a)
print(a ^ b)

a.remove(1)
print(a)

a.discard(1) #ne baca exception

c = {10, 5.5, True, 'abcd', (2, 3)}
print(c)

#c.add([1, 2, 3])
#c.add({'abcd' : 123})
#c.add({1, 2, 3})

#torke sa 0 ili jednim elementom
d = ()
print(d)
e = (5,)
print(e)

x = 10
y = 12

x, y = y, x

l1 = [2*i for i in range(5)]
for el in l1:
    print(el, end = ' ')

print()

for el in a:
    print(el, end = ' ')
print()

for idx, el in enumerate(l1[2:], start = 2):
    print(idx, el)

l2 = [5*i for i in range(5)]
print(l1)
print(l2)

for el1, el2 in zip(l1, l2):
    print(el1 + el2)

