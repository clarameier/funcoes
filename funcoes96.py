larg = float(input('Qual o valor da largura do seu terreno, em metros? '))
comp = float(input('Qual o valor da altura do seu terreno, em metros? '))

def mult(larg, comp):
    m = larg * comp
    print(f'A área de um terreno é de {larg} x {comp}, que é igual a {m}m²!')

mult(larg, comp)