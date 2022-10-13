from time import sleep

def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}: ')
    sleep(2.5)
    print('-'*100)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += passo
        print('fim')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= passo
        print('fim')

print('='*100)

#contagem 1
contador(1, 10, 1)
print('='*100)

#contagem 2
contador(10, 0, 2)
print('='*100)

#contagem 3
contador(199, 240, 30)
print('='*100)

#contagem pessoal
print('Agora é a sua vez de tentar!')
print('-'*100)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)