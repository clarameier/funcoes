#opção 1
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

print('='*100)

#opção 2
def soma(a,b):
    s = a + b
    print(s)

soma(4, 5)
soma(8, 9)
soma(2, 1)

print('='*100)

#opção 3
def soma(a,b):
    print(f'A = {a} e B = {b}.')
    s = a + b
    print(f'A soma de A+B = {s}')

soma(a=4, b=1)
soma(7, 7)
