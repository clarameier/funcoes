#opção 1
def contador(*num):
    print(num) #printa todos os números exatamente como escrito

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

print('='*100)

#opção 2
def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('fim!')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

print('='*100)

#opção 3
def contador(*num):
    qnt = len(num)
    print(f'Recebi os valores {num} e são ao todo {qnt} números')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

