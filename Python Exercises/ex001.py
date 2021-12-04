print('Esse código recebe uma lista e a devolve sem itens duplicados. \nPor favor, digite abaixo a quantidade de elemetos que deseja adicionar a lista.')

n = int(input('Digite Aqui: '))

lista = []

while len(lista) < n:
    k = input(f'Digite o {len(lista) + 1}° termo da lista: ')
    lista.append(k)

resultado = ', '.join(set(lista))

print(f'Os termos não repetidos são: {resultado}')