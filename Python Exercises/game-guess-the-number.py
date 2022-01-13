# Neste jogo o usuário fornece dois números inteiros distintos, x e y.
# Em seguida o computador escolhe um número entre x e y e o usuário
# deve adivinhar qual número o computador escolheu.
from random import randint

def main():

    print('----------Jogo de Adivinha----------')
    x = int(input('Escolha um número: '))
    y = int(input('Escolha outro número: '))
    escolhas = [x, y]
    n = randint(min(escolhas), max(escolhas))
    print(f'Eu escolhi um número entre {min(escolhas)} e {max(escolhas)}. Consegue adivinhar qual foi?')
    cont = 0
    while True:
        k = int(input('Digite a sua sugestão: '))
        cont += 1
        if k == n:
            print(f'Parabéns! Você descobriu em {cont} tentativas.')
            break
        else:
            if k < n:
                print(f'Não, o número que escolhi é maior do que {k}.')
            else:
                print(f'Não, o número que escolhi é menor do que {k}.')
            pass
        
        # Esse caso permite o uso do elif. Da próxima vez eu implemento ele, porque sempre é bom evitar
        #  o aninhamento de if.

if __name__ == '__main__':
    main()