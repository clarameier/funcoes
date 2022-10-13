def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2 #vai multiplicar todos os valores codados por 2
        pos += 1

valores = [6, 3, 9, 1 , 0, 2] #valores codados
dobra(valores) #valores dobrados
print(valores) #print dos valores dobrados

print('='*100)

#ex2
def soma(* valor):
    s = 0
    for num in valor:
        s += num
    print(f'Somando os valores {valor} temos {s}')

soma(5,2)
soma(2, 9, 4)