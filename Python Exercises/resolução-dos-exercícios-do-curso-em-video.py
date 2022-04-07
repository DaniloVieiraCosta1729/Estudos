"""
n1 = float(input('Digite um número racional razovavelmente pequeno: '))
n2 = float(input('Digite outro número: '))
s = n1 + n2
print('A soma entre {} e {} é {}'.format(n1, n2, s))
"""
"""
a = input('Digite alguma coisa: ')
x = "é alfabético"
y = "é numérico"
z = "é alfanumérico"
if not a.isalpha():
    x = "não é alfabético"
if not a.isnumeric():
    y = "não é numérico"
if not a.isalnum():
    z = "não é alfanumérico"
d = type(a)
print('O que foi digitado é do tipo {}, {}, {} e {}. Boa noite.'.format(d, x, y, z))
"""
"""
def soma(x, y):
    return x + y
a = int(input('Digite um número inteiro: '))
b = int(input('Digite mais um número inteiro: '))
print('A soma entre {} e {} é {}.'.format(a, b, soma(a, b)))
"""
"""
def conversor(z):
    a = input("Deseja converter para quilometros ou milhas? (digite km para quilometros e mi para milhas): ")
    if a == "km":
        print('{} mi = {} km'.format(z, (z*1.60934)))
        return z*1.60934
    else:
        print('{} km = {} mi'.format(z, z*(1/1.60934)))
        return z*(1/1.60934)
z = float(input("Digite a magnitude da distância. Não se preocupe com a unidade: "))
conversor(z)
"""
"""
algo = input('Digite alguma coisa: ')
print('O tipo primitivo do que foi digitado é {};'.format(type(algo)))
if algo.isspace():
    print('É composto inteiramente por espaços;')
else:
    print('Não é composto apenas por espaços;')
if algo.isnumeric():
    print('É numérico;')
else:
    print('Não é numérico;')
if algo.isalpha():
    print('É alfabético;')
else:
    print('Não é alfabético;')
if algo.isalnum():
    print('É alfanumérico;')
else:
    print('Não é alfanumérico;')
if algo.isupper():
    print('Está totalmente esrito em maiusculas;')
elif algo.islower():
    print("Está totalmente escrito em minusculas;")
else:
    print('Não está escrito, totalmente, em maiusculas e nem em minusculas;')
if algo[0].isupper():
    print('A primeira palavra é capitalizada.')
else:
    print("O primeiro caractere não é uma letra maiuscula.")
# a função algo.istitle() diz se é ou não capitalizada. 
"""
"""
import math
a = int(input('Digite o numerador: '))
b = int(input('Digite o denominador: '))
print('{} = {}*{} + {}'.format(a, a//b, b, int(math.fmod(a, b))))
"""
"""
lista = [1]
while len(lista) < 100:
    lista.append(lista[-1] + 1)
s = 0
for n in lista:
    s = s + 1/(n**2)
print(s)
"""
"""
import math
lista = [1 / (i ** 2) for i in range(1, 10000001)]
s = 0
for i in lista:
    s += i
print(s)
print(((math.pi) ** 2) / 6)
"""
"""
antes = "_"*10
depois = "_"*10
nome = input('qual o seu nome? ')
print('{}{:^10}{}'.format(antes,nome,depois))
"""
"""
nome = input('qual o seu nome? ')
print('{:_^100}'.format(nome))
"""
"""
print('Esse scrit informa a soma dos termos de uma progressão aritmética ou geométrica.')
print('Para tanto, é necessário que você informe a o primeiro termo, a razão e o tipo de sequência.')
a0 = float(input("Informe o primeiro termo: "))
r = float(input('A razão é: '))
tipo = input('Digite PG se a sequência for geométrica e PA caso seja aritmética: ')
if tipo == "PG":
    tamanho = input('A soma é infinita ou finita? ')
    if tamanho == "infinita":
        s = a0*(1/(1-r))
        print('soma = {}'.format(s))
    else:
        n = int(input('Deseja somar até que termo? (OBS.: A sequência começa com A0; digite apenas o número inteiro que representa o termo): )'))
        s = a0*((r**(n+1)-1)/(r-1))
        print('soma = {}'.format(s))
elif tipo == "pg":
    tamanho = input('A soma é infinita ou finita? ')
    if tamanho == "infinita":
        s = a0 * (1 / (1 - r))
        print('soma = {}'.format(s))
    else:
        n = int(input('Deseja somar até que termo? (OBS.: A sequência começa com A0; digite apenas o número inteiro que representa o termo): )'))
        s = a0 * ((r ** (n + 1) - 1) / (r - 1))
        print('soma = {}'.format(s))
elif tipo == "PA":
    n = int(input('Deseja somar até que termo? (OBS.: o primeiro é o A1; digite apenas o número inteiro que representa o termo): '))
    s = (n / 2) * ((n - 1) * r + 2 * a0)
    print('soma = {}'.format(s))
elif tipo == "pa":
    n = int(input('Deseja somar até que termo? (OBS.: o primeiro o A1; digite apenas o número inteiro que representa o termo): '))
    s = (n / 2) * ((n - 1) * r + 2 * a0)
    print('soma = {}'.format(s))
else:
    print('Entrada não reconhecida...')
"""
"""
print('Esse scrit informa a soma dos termos de uma progressão aritmética ou geométrica.\nPara tanto, é necessário que você informe a o primeiro termo, a razão e o tipo de sequência.')
a0 = float(input("Informe o primeiro termo: "))
r = float(input('A razão é: '))
tipo = input('Digite PG se a sequência for geométrica e PA caso seja aritmética: ')
if tipo == "PG":
    tamanho = input('A soma é infinita ou finita? ')
    if tamanho == "infinita":
        s = a0*(1/(1-r))
        print('soma = {}'.format(s))
    else:
        n = int(input('Deseja somar até que termo? (OBS.: A sequência começa com A0; digite apenas o número inteiro que representa o termo): )'))
        s = a0*((r**(n+1)-1)/(r-1))
        print('soma = {}'.format(s))
elif tipo == "pg":
    tamanho = input('A soma é infinita ou finita? ')
    if tamanho == "infinita":
        s = a0 * (1 / (1 - r))
        print('soma = {}'.format(s))
    else:
        n = int(input('Deseja somar até que termo? (OBS.: A sequência começa com A0; digite apenas o número inteiro que representa o termo): )'))
        s = a0 * ((r ** (n + 1) - 1) / (r - 1))
        print('soma = {}'.format(s))
elif tipo == "PA":
    n = int(input('Deseja somar até que termo? (OBS.: o primeiro é o A1; digite apenas o número inteiro que representa o termo): '))
    s = (n / 2) * ((n - 1) * r + 2 * a0)
    print('soma = {}'.format(s))
elif tipo == "pa":
    n = int(input('Deseja somar até que termo? (OBS.: o primeiro o A1; digite apenas o número inteiro que representa o termo): '))
    s = (n / 2) * ((n - 1) * r + 2 * a0)
    print('soma = {}'.format(s))
else:
    print('Entrada não reconhecida...')
"""
"""
a = int(input('digite um inteiro: '))
print('O número {} é sucessor de {} e o número {} é antecessor de {}.'.format(a+1,a,a-1,a))
"""
"""
a = float(input('Digite um número: '))
print('O dobro de {} é {}; \nO triplo é {};\nE sua raiz quadrada é {}.'.format(a, a * 2, a * 3, a ** 0.5))
"""
"""
a = float(input('Primeira nota: '))
b = float(input('Segunda nota: '))
print('A média é {}'.format((a+b)/2))
"""
"""
def conversor(z):
    x = input('O seguinte scrit converte metros para centimetros ou de centimetros para metros \nPara converter de '
              'metros para cm digite cm, se não, digite m: ')
    if x == "cm":
        print('{} m = {} cm'.format(z, z * 100))
        return z * 0.01
    elif x == "m":
        print('{} cm = {} m'.format(z, z * 0.01))
        return z * 100
    else:
        print('Unidade não reconhecida...')
        return z
z = float(input('Digite a magnitude da distância, sem se peocupar com a unidade: '))
conversor(z)
"""
"""
taboada1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
taboada = []
z = int(input('Digite uma números natural não nulo: '))
for n in taboada1:
    taboada.append(n*z)
print(taboada)
"""
"""
z = int(input('Digite um número natural não nulo: '))
taboada = [0]
t = []
while len(taboada) < 11:
    taboada.append(taboada[-1]+1)
for n in taboada:
            t.append(n*z)
print(t)
"""
"""
def cambio(z):
    x = input('Para converter dolares para reais, digite X;\nPara converter de Reais para dolares, digite Y.\n[X/Y]: ')
    if x == "X":
        print('US$ {} = R$ {}'.format(z, z * 5.03))
        return z * 5.03
    elif x == "x":
        print('US$ {} = R$ {}'.format(z, z * 5.03))
        return z * 5.03
    else:
        print('R$ {} = US$ {}'.format(z, z * (1/5.03)))
        return z * (1 / 5.03)
z = float(input('Digite o valor em dinheiro, nao se preocupe em específicar a moeda: '))
cambio(z)
"""
"""
import math
lh = []
while len(lh) < 2:
    if len(lh) == 0:
        a = float(input('Digite a largura: '))
        lh.append(a)
    else:
        a = float(input('Digite a altura: '))
        lh.append(a)
if math.fmod(float(lh[0]) * float(lh[1]), 2) == 0:
    print('Essa parede precisa de {} L de tinta.'.format(int(int(lh[0]) * int(lh[1]) * 0.5)))
else:
    print('Essa parede precisa de {}/{} L de tinta para ser pintada. Ou seja, {} L.'.format(int(lh[0])*int(lh[1]), 2, float(lh[0]) * float(lh[1]) * 0.5))
"""
"""
def desconto5(a):
    print('R$ {}'.format(float(a - a * 0.05)))
    return float(a - a * 0.05)
a = float(input('Digite o valor do produto para saber quanto ele custo com o desconto de 5%: '))
desconto5(a)
"""
"""
def desconto15(a):
    print('R$ {}'.format(float(a + a * 0.15)))
    return float(a + a * 0.15)
a = float(input('Digite o salário atual para saber o novo salário com o aumento de 15%: '))
desconto15(a)
"""
"""
n = int(input('Digite um número natural não nulo: '))
taboada = [0]
t = []
while len(taboada) < 11:
    taboada.append(taboada[-1]+1)
for i in taboada:
    t.append(i*n)
for k in taboada:
    print("{:2} X {} = {}".format(int(k), int(n), int(k*n)))
"""
"""
def temperatura(t):
    a = input('Digite a unidade dela. Por exemplo: K, C ou F: ')
    b = input('Digite a escala para qual você deseja converter a temperature informada. Exemplo: C, K, F: ')
    if (a == "C" or a == "c") and (b == "K" or b == "k"):
        print('{} ºC = {} K'.format(t, t + 273.15))
    elif (a == "C" or a == "c") and (b == "F" or b == "f"):
        print('{} ºC = {} ºF'.format(t, (180 / 100) * t + 32))
    elif (a == "F" or a == "f") and (b == "K" or b == "k"):
        print('{} ºF = {} K'.format(t, (100 / 180) * (t - 32) + 273.15))
    elif (a == "F" or a == "f") and (b == "C" or b == "c"):
        print('{} ºF = {} ºC'.format(t, (t - 32) * (100 / 180)))
    elif (a == "K" or a == "f") and (b == "C" or b == "c"):
        print('{} K = {} ºC'.format(t, t - 273.15))
    elif (a == "K" or a == "k") and (b == "F" or b == "f"):
        print('{} K = {} ºF'.format(t, (180 / 100) * (t - 273.15) + 32))
    else:
        print("Unidade não reconhecida...")
    return a
t = float(input('Digite a magnetude da temperatura: '))
temperatura(t)
"""
"""
km = float(input('Quantos km foram rodados? '))
dias = int(input('Quantos dias o carro esteve alugado para este cliente? '))
print('O valor a ser cobrado é R$ {}'.format(60 * dias + km * 0.15))
"""
"""
# Codigo que ignora os espaços, letras etc. e considera apenas os números (o que pode ser usado no exercício de conversão de temperatura).
a = input('digite: ')
lista = []
l = []
i = 0
x = 0
y = 0
for n in a:
    if n.isdigit():
        lista.append(n)
for n in a:
    if n.isdigit() or n == "." or n == ",":
        l.append(n)
for n in lista:
    while len(lista) - i > 0:
        x = (10**(len(lista) - i))*int(lista[i])
        y = y + x
        i = i+1
if "," in l:
    print(y / 10 ** (len(l) - l.index(",")))
elif "." in l:
    print(y / 10 ** (len(l) - l.index(".")))
else:
    print(y/10)
#Proposta: refazer o ex da temperatura, mas usando essas técnicas para entender ter a escala e a magnetude da temperatura informada.
"""
"""
t = input('Digite a temperatura com a unidade: ')
def temperatura(t):
    es = []
    i = 0
    x = 0
    y = 0
    while es == []:
        for n in t:
            if (n.isalpha()) and (n != "º"):
                es.append(n)
        if es == []:
            t = input('Por favor, informe a temperatura com a \033[1:32munidade!\033[m')
    mag = []
    for n in t:
        if n.isdigit():
            mag.append(n)
    cor = []
    for n in t:
        if (n.isnumeric()) or (n == ",") or (n == "."):
            cor.append(n)
    for n in mag:
        while len(mag) - i > 0:
            x = (10 ** (len(mag) - i)) * int(mag[i])
            y = y + x
            i = i + 1
    if ("," in cor):
        m = y / 10 ** (len(mag) - cor.index(",") + 1)
    elif ("." in cor):
        m = y / 10 ** (len(mag) - cor.index(".") + 1)
    else:
        m = y / 10
    a = es[0]
    b = input('Digite a escala para qual você deseja converter a temperature informada. Exemplo: C, K, F: ')
    if (a == "C" or a == "c") and (b == "K" or b == "k"):
        print('{} ºC = {} K'.format(m, m + 273.15))
    elif (a == "C" or a == "c") and (b == "F" or b == "f"):
        print('{} ºC = {} ºF'.format(m, (180 / 100) * m + 32))
    elif (a == "F" or a == "f") and (b == "K" or b == "k"):
        print('{} ºF = {} K'.format(m, (100 / 180) * (m - 32) + 273.15))
    elif (a == "F" or a == "f") and (b == "C" or b == "c"):
        print('{} ºF = {} ºC'.format(m, (m - 32) * (100 / 180)))
    elif (a == "K" or a == "f") and (b == "C" or b == "c"):
        print('{} K = {} ºC'.format(m, m - 273.15))
    elif (a == "K" or a == "k") and (b == "F" or b == "f"):
        print('{} K = {} ºF'.format(m, (180 / 100) * (m - 273.15) + 32))
    else:
        print("Unidade não reconhecida...")
    return a
temperatura(t)
"""
# ceil é a função "teto" da matemática; A floor é a função "piso".
"""
def logaritmonatural(x):
    import math
    l = []
    i = 1
    y = 0
    z = 0
    while len(l) < 100:
        l.append(((-1)**(i + 1)) * (((x - math.e) ** i)/(i * math.exp(i))))
        y = ((-1)**(i + 1)) * (((x - math.e) ** i)/(i * math.exp(i)))
        z = z + y
        i = i + 1
    w = z + 1
    print(w)
    return w
x = float(input('ln(x), informe x: '))
logaritmonatural(x)
"""
"""
from math import log
print(log(2, 2))
"""
"""
import random
print(random.randint(1, 20))
"""
"""
import emoji
print(emoji.emojize('Olá, Mundo! :smiley:', use_aliases=True))
"""
"""
from math import floor
a = floor(float(input('Digite um números racional: ')))
print(a)
"""
"""
from math import sqrt
from math import floor
a = float(input('Digite o valor do cateto oposto: '))
b = float(input('Digite o valor do cateto adjacente: '))
print('A hipotenusa é {}'.format(sqrt(a**2 + b**2)))
if (sqrt(a**2 + b**2))/floor(sqrt(a**2 + b**2)) == 1 and a / floor(a) == 1 and b / floor(b) == 1:
    print('Esse triangulo é pitagórico.')
else:
    pass
"""
"""
# Nesse desafio eu poderia ter usado o método .upper ou o .lower ao ínves de colocar varios casos possíveis de escrever cos, sen etc.
def tri(x):
    from math import cos
    from math import sin
    from math import tan
    from math import pi
    f = []
    arg = []
    corretor = []
    unid = input('Qual a unidade do ângulo? [rad / graus]: ')
    y = 0
    z = 0
    i = 0
    for n in x:
        if n.isdigit():
            arg.append(n)
        elif n.isalpha():
            f.append(n)
        elif n.isalpha() or n == ".":
            corretor.append(n)
    while len(arg) - i > 0:
        z = (10 **(len(arg) - i)) * float(arg[i])
        y = y + z
        i = i + 1
    if "." in corretor:
        argumento = y / 10 ** (len(arg) - corretor.index("."))
    else:
        argumento = y / 10
    funcao = ''.join(f)
    if unid == ("rad" or "radianos" or "radiano" or "Rad" or "RAD"):
        if funcao == ("cos" or "cosseno" or "Cos"):
            print('cos {} = {}'.format(argumento, cos(float(argumento))))
        elif funcao == ("sen" or "sin" or "seno" or "Seno"):
            print('sen {} = {}'.format(argumento, sin(float(argumento))))
        elif funcao == ("tg" or "tag" or "tan" or "tangente"):
            print('tg {} = {}'.format(argumento, tan(float(argumento))))
        else:
            print("Entrada não reconhecida. A entrada deve ser do tipo: sen x, sin x, tg x etc.")
    elif unid == ("graus" or "degree" or "º"):
        if funcao == ("cos" or "cosseno" or "Cos"):
            print('cos {} = {}'.format(argumento, cos((pi / 180) * float(argumento))))
        elif funcao == ("sen" or "sin" or "seno" or "Seno"):
            print('sen {} = {}'.format(argumento, sin((pi / 180) * float(argumento))))
        elif funcao == ("tg" or "tag" or "tan" or "tangente"):
            print('tg {} = {}'.format(argumento, tan((pi / 180) * float(argumento))))
        else:
            print("Entrada não reconhecida. A entrada deve ser do tipo: sen x, sin x, tg x etc.")
    return argumento
x = input(" Essa função calcula seno, cosseno e tengente.\n Por favor, insira o valor que deseja calcular (OBS.: INSIRA O VALOR EM RADIANOS): ")
tri(x)
"""
"""
# O codigo abaixo mostra que não é necessário usar o while para transformar os elementos de uma lista em um número.
# Basta usar o float(''.join(lista))
a = input('digite: ')
st = []
num = []
for n in a:
    if n.isalpha():
        st.append(n)
    elif n.isnumeric():
        num.append(n)
    else:
        pass
print(type(''.join(st)))
print(type(float(''.join(num))))
"""
"""
from random import randint
nomes = []
i = 1
qnt = int(input('Quantos pessoas participarão do sorteio: '))
while len(nomes) < qnt:
    nm = input('Pessoa {}: '.format(i))
    i = i + 1
    nomes.append(nm)
escolhido = randint(0, qnt - 1)
print('O escolhi é {}'.format(nomes[escolhido]))
# Não é necessário fazer uma variável "escolhido", para depois escoher o nomes[escolhido]. 
# Basta usar o random.choice(nomes) = D
"""
"""
from random import randint
nomes = []
ordem = []
i = 1
j = 1
k = 0
qnt = int(input('Quantos alunos apresentarão: '))
while len(nomes) < qnt:
    nm = input('Pessoa {}: '.format(i))
    i = i + 1
    nomes.append(nm)
while len(ordem) < qnt:
    nm = nomes[randint(0,qnt - j)]
    ordem.append(nm)
    nomes.remove(nm)
    j = j + 1
while k < qnt:
    print('{}ª pessoa: {}'.format(k + 1, ordem[k]))
    k = k + 1
# Novamente, não é necessário criar um while para fazer uma nova lista com os nomes dispostos aleatoriamente. 
# Basta usar o módulo .shuffle do random. Ou seja, from random import shuffle. Esse módulo "embaralha os elementos de uma lista".
"""
"""
from playsound import playsound
playsound('pedros theme (final).mp3')
"""
# o método lista.replace(x, y) substitui o x por y em uma lista.
# o método strip remove os espaços da extremidade (pode-se adicionar r ou l antes do strip para indicar direita ou esquerda).
# o método split cria uma nova lista em que cada palavra é jogada em um espaço da lista.
"""
a = input('Digite: ')
b = []
for n in a:
    if not n.isspace():
        b.append(n)
    else:
        pass
print(str(''.join(b)))
"""
"""
nome = input('Seu nome: ')
print('Nome com todas as letras maiusculas: {}\nNome com todas as letras minusculas: {}'. format(nome.strip().upper(), nome.strip().lower()))
print(len(''.join(nome.split())))
print(len(nome.split()[1]))
"""
"""
n = -1
while n == -1:
    n = int(input('Digite um número inteiro entre 0 e 9999: '))
    if ((n < 0) or (n > 9999)):
        n = int(input('O valor digitado não está no intervalo de 0 à 9999, por favor, informe outro: '))
    else:
        pass
st = str(n)
if len(st) == 4:
    print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(st[3], st[2], st[1], st[0]))
elif len(st) == 3:
    print('Unidade: {}\nDezena: {}\nCentena: {}'.format(st[2], st[1], st[0]))
elif len(st) == 2:
    print('Unidade: {}\nDezena: {}'.format(st[1], st[0]))
else:
    print('Unidade: {}'.format(st[0]))
"""
"""
cidade = input('Digite o nome de uma cidade: ')
if cidade.upper().find('SANTO') == 0:
    print('[SIM] O nome da cidade "{}" começa com a palavra "santo".'.format(cidade))
else:
    print('[NÃO] O nome da cidade "{}" não começa com a palavra "santo".'.format(cidade))
"""
"""
nome = input('Diga um nome: ')
if 'SILVA' in nome.upper():
    print('[SIM] há a palavra "Silva" no nome {}.'.format(nome))
else:
    print('[NÃO] Não há a palavra "Silva" no nome {}'.format(nome))
"""
"""
frase = input('Digite alguma frase: ')
qntA = frase.upper().count('A')
p = frase.strip().upper().find('A')
l = []
i = 0
while not 'A' in l:
    if frase.upper()[len(frase) - 1 - i] == "A":
        l.append(frase.upper()[len(frase) - 1 - i])
    else:
        l.append('x')
    i = i + 1
f = len(frase) - len(l)
print('A frase tem {} a(s); o primeiro aparece na {}ª posição e o último na {}ª posição.'.format(qntA, p, f))
# Ao invés de usar o while e o if para encontrar a posição do último "A". É melhor usar o .rfind("A") que procura o A,
# a partir da direita.
"""
"""
nome = input('Digite um nome: ')
l = nome.split()
print('{} {}'.format(l[0], l[-1]))
"""
"""
n = -1
while n == -1:
    n = int(input('Digite um número inteiro entre 0 e 9999: '))
    if ((n < 0) or (n > 9999)):
        n = int(input('O valor digitado não está no intervalo de 0 à 9999, por favor, informe outro: '))
    else:
        pass
st = str(n)
ordem = ['Unidade', 'Dezena', 'Centena', 'Milhar']
w = len(st)
i = 0
while w > 0:
    print('{}: {}'.format(ordem[i], st[w - 1]))
    i = i + 1
    w = w - 1
"""
# Condição simplificada! Ô.Ô: a = P(x) if Q(x) else F(x)
# Exemplo: print('Carro Novo' if tempo < 10 else 'Carro Velho')
"""
from random import randint
u = int(input('__Jogo de Adivinhação__\nDigite um número entre 1 e 5: '))
s = randint(1, 5)
print('O número sorteado foi {}.'.format(s))
print('PARABENS! Você conseguiu' if u == s else 'Infelizmente, você não acertou...')
"""
"""
v = float(input('Qual é a velocidade: '))
if v > 80:
    print('Você foi multado em R$ {} por excesso de velocidade.'.format((v - 80) * 7))
else:
    print('Ok, essa velocidade é permitida.')
"""
"""
from math import fmod
n = int(input('Digite um número inteiro: '))
if fmod(n, 2) == 0:
    print('O número {} é par.'.format(n))
else:
    print('O número {} é ímpar.'.format(n))
"""
"""
from math import ceil
d = float(input('Informe a distância a ser percorrida (em km): '))
if 0 < d <= 200:
    print('O valor da passagem é R$ {}.'.format(ceil(d) * 0.5))
elif d > 200:
    print('O valor da passagem é R$ {}.'.format(ceil(d) * 0.45))
else:
    print('A distância informada não é valída. Por favor, informe um número racional e positivo.')
"""
"""
from math import fmod
ano = int(input('Informe o ano: '))
if fmod(ano, 4) == 0:
    if ((fmod(ano, 100) == 0) and (fmod(ano, 400) != 0)):
        print('O ano {} não é bissexto.'.format(ano))
    else:
        print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
"""
"""
l = []
qnt = int(input('Quantos números você deseja comparar? : '))
while len(l) < qnt:
    if len(l) == 0:
        n = float(input('Digite um número racional: '))
    else:
        n = float(input('Digite outro número racional: '))
    l.append(n)
def maximo(x):
    maior = [0]
    while len(maior) < len(x):
        for n in x:
            if n > maior[0]:
                maior.insert(0, n)
            else:
                pass
    return maior[0]
def minimo(x):
    menor = []
    menor.append(x[0])
    while len(menor) < len(x):
        for n in x:
            if n < menor[0]:
                menor.insert(0, n)
            else:
                pass
    return menor[0]
print('O menor é {}'.format(minimo(l)))
print('O maior é {}'.format(maximo(l)))
"""
"""
numeros = []
qnt = int(input('Digite a quantidade de números que deseja comparar: '))
while len(numeros) < qnt:
    numeros.append(float(input('Digite um número: ')))
print('O maior número digitado foi: {}'.format(max(numeros)))
print('O menor número, entre os digitados, é: {}'.format(min(numeros)))
"""
"""
s = float(input('O salário atual é (em R$): '))
if s > 1250:
    print('O novo salário será R$ {}'.format(s + s * 0.1))
elif 0 < s <= 1250:
    print('O novo salário será R$ {}'.format(s + s * 0.15))
else:
    print('Entrada não reconhecida.')
"""
"""
lados = []
while len(lados) < 3:
    if len(lados) == 0:
        lados.append(float(input('Digite o comprimento de três segmentos de retas.\nPrimeiro:  ')))
    else:
        lados.append(float(input('Próximo: ')))
h = max(lados)
lados.remove(max(lados))

if 0 < h < lados[0] + lados[1]:
    print('Os segmentos informados conseguem formar um triângulo.')
else:
    print('Os segmentos informados não formam um triângulo pois {} > {} + {}'.format(h, lados[0], lados[1]))
if h ** 2 == lados[0] ** 2 + lados[1] ** 2:
    print('[SIM] O triângulos de lados {}, {} e {} é um triângulo retângulo!'.format(h, lados[0], lados[1]))
else:
    print('Os segmentos informados não formam um triângulo retângulo, pois {}² é diferente de {}² + {}²'.format(h, lados[0], lados[1]))
"""
"""
print('\033[1:30:42m Hello, World!\033[m')
print('\033[1:30:41m Hello, World!')
print('\033[0:32:40m Hello, World!')
print('\033[1:30:43m Hello, World!')
print('\033[1:30:44m Hello, World!')
print('Por favor, informe a temperatura com a \033[1:32munidade!\033[m')
"""
# pode-se usar um dicionário:
# Cores = {limpar: '\033[m'; amarelo: '\033[0:33m'; etc} depois, ao ínvés de escrever \033... basta chamar a cor do dicionário!
# Cores[amarelo] = '\033[0:33m'
# Fazer o jogo do quadrado de lado 3 com 8 números!
# Ele deve gerar cada novo jogo de modo aleatório.
"""
import PySimpleGUI as sg
layout = [
    [sg.Text('Esse script permite que você converta um valor de km para mi e de mi para km')],
    [sg.Text('Por favor informe a distância'), (sg.InputText())],
    [sg.Button('km para mi'), sg.Button('mi para km')],
    [sg.Button('Cancelar')]
]
janela_entrada = sg.Window('Conversor de Unidades', layout)
while True:
    events, values = janela_entrada.read()
    a = float(values[0])
    if (events == sg.WIN_CLOSED) or (events == 'Cancelar'):
        break
    elif events == 'km para mi':
        sg.Window('Conversor de Unidades', [[sg.Text(a * (1 / 1.60934)), sg.Text('mi')]]).read()
    elif events == 'mi para km':
        sg.Window('Conversor de Unidades', [[sg.Text(a * (1 / 1.60934)), sg.Text('km')]]).read()
janela_entrada.close()
"""

# 1º Resolver sem o PySimpleGUI
"""
perguntas = ['Qual o valor da casa que deseja comprar? ', 'O seu salário é? ',
             'Quanto tempo o emprestimo levará para ser pago (meses)? ']
respostas = []
i = 0
while len(respostas) < 3:
    print(perguntas[i])
    r = float(input('Digite: '))
    respostas.append(r)
    i = i + 1
prestacao = float(respostas[0]) / float(respostas[2])
if prestacao > 0.3 * float(respostas[1]):
    print('Emprestimo não permitido.')
else:
    print('A prestação será de R${}'.format(prestacao))
"""
# Peça um natural e mostre as opções: converter para a base binária, octal ou hexadecimal.
# Para converter um natural n da base 10 para a base b devemos dividir n / b, anotar o resto e repetir o procedimento para
# o quociente da divisão até que o quociente seja menor que b. O número na nova base é a concatenação dos restos, porém
# de trás para frente.
"""
from math import fmod
n = int(input('Digite um número natural: '))
base = input('Deseja converter o número para a base binário, octal ou hexadecimal?\nDigite:')
if (base == 'binário') or (base == 'binário') or (base == 'Binário') or (base == 'Binario'):
    algarismos = []
    q = n
    while q >= 2:
        algarismos.insert(0, str(int(fmod(q, 2))))
        q = q // 2
    algarismos.insert(0, str(q))
    print(''.join(algarismos))
elif (base == 'octal') or (base == 'Octal') or (base == 'OCTAL'):
    algarismos = []
    q = n
    while q >= 8:
        algarismos.insert(0, str(int(fmod(q, 8))))
        q = q // 8
    algarismos.insert(0, str(q))
    print(''.join(algarismos))
elif (base == 'Hexadecimal') or (base == 'hexadecimal') or (base == 'hexa'):
    hexa = {15: 'F', 14: 'E', 13: 'D', 12: 'C', 11: 'B', 10: 'A', 9: 9, 8: 8, 7: 7, 6: 6, 5: 5, 4: 4, 3: 3, 2: 2, 1: 1, 0: 0}
    algarismos = []
    q = n
    while q >= 16:
        algarismos.insert(0, str(hexa[int(fmod(q, 16))]))
        q = q // 16
    algarismos.insert(0, str(hexa[q]))
    print(''.join(algarismos))
"""
"""
def hexa_deci(n):
    hexa = {'F': 15, 'E': 14, 'D': 13, 'C': 12, 'B': 11, 'A': 10, 9: 9, 8: 8, 7: 7, 6: 6, 5: 5, 4: 4, 3: 3, 2: 2, 1: 1,
            0: 0}
    mag = []
    i = 0
    j = 0
    for k in n:
        if k.isnumeric():
            mag.append(hexa[int(k)])
        else:
            mag.append(hexa[k])
    while len(mag) - i > 0:
        x = (16 ** (len(mag) - i)) * int(mag[i])
        j = j + x
        i = i + 1
    return int(j / 16)
print(hexa_deci(str('AE2')))
"""
# numqd[i] = QD.index(abc[i]) + 1, para todo numqd[i] diferente de ' '.
# auxiliar = [' ']; auxiliar.append(x),
# entrada = (x), j = numqd.find(x), k = numqd.find(' '), numqd.remove(j), numqd.remove(' ')
# numqd.insert(j, ' ') and numqd.insert(k, x)
"""
from random import choice
cores = {'limpar': '\033[m', 'amarelo': '\033[1:33m', 'vermelho': '\033[1:31m', 'verde': '\033[1:32m', 'azul': '\033[1:34m'}
indices = {'l1': 1, 'l2': 2, 'l3': 3, 'c1': 1, 'c2': 2, 'c3': 3}
linhas = ['l1', 'l2', 'l3']
colunas = ['c1', 'c2', 'c3']
QD = []
abc = [['l1', 'c1'], ['l1', 'c2'], ['l1', 'c3'], ['l2', 'c1'], ['l2', 'c2'], ['l2', 'c3'], ['l3', 'c1'], ['l3', 'c2'], ['l3', 'c3']]
numqd = []
while len(QD) < 9:
    v = [choice(linhas), choice(colunas)]
    if v not in QD:
        QD.append(v)
    else:
        pass
while len(numqd) < 9:
    for n in abc:
        if QD.index(n) != 8:
            numqd.append(1 + QD.index(n))
        else:
            numqd.append(' ')
def trocar(x, numqd):
    auxiliar = [' ']
    auxiliar.append(x)
    numqd[numqd.index(x)] = auxiliar[0]
    numqd[numqd.index(' ')] = auxiliar[1]
    return numqd
i = 1
while i < 7:
    print(numqd)
    print(trocar(i, numqd))
    i = i + 1
"""
"""
            if abs((numqd.index((int(events))) - numqd.index(' '))) == 1 or abs((numqd.index((int(events))) - numqd.index(' '))) == 3:
                if numqd.index(int(events)) > numqd.index(' '):
                    trocarXmaior(int(events), numqd)
                    janela.close()
                else:
                    trocarXmenor(int(events), numqd)
                    janela.close()
            else:
                janela.close()
                pass
"""
# Faça um programa que leia a altura e a massa de uma pessoa e, com isso, informe o IMC (indece de massa corporia).
# IMC < 18.5 (abaixo do peso) ; 18.5 <= IMC <= 25 (ideal) ; 25 < IMC <= 30 (sobre peso) ; 30 < IMC <= 40 (obesidade)
# 40 < IMC (obesidade morbida)
"""
import PySimpleGUI as sg
layout = [
    [sg.Text('Por favor, informe o seu peso e sua altura.')],
    [sg.Text('Peso [kg]'), sg.InputText()],
    [sg.Text('Altura [m]'), sg.InputText()],
    [sg.Button('Próximo'), sg.Button('Cancelar')]
]
janela = sg.Window('IMC', layout)
while True:
    events, values = janela.read()
    p = float(values[0])
    h = float(values[1])
    IMC = str(round(p/(h ** 2), 2))
    if (events == 'Cancelar') or (events == sg.WIN_CLOSED):
        break
    elif p/(h ** 2) < 18.5:
        sg.Window('IMC',[[sg.Text(IMC), sg.Text(' Abaixo do peso')]]).read()
    elif 18.5 <=p/(h ** 2) <= 25:
        sg.Window('IMC',[[sg.Text(IMC), sg.Text(' Peso dentro do Ideal')]]).read()
    elif 25 < p/(h ** 2) <= 30:
        sg.Window('IMC',[[sg.Text(IMC), sg.Text(' Sobre Peso')]]).read()
    elif 30 < p/(h ** 2) <= 40:
        sg.Window('IMC',[[sg.Text(IMC), sg.Text(' Obesidade')]]).read()
    elif p/(h ** 2) < 40:
        sg.Window('IMC',[[sg.Text(IMC), sg.Text(' Obesidade morbida')]]).read()
    else:
        sg.Window('IMC',[[sg.Text('Não foi possível calcular o IMC. Por favor, verifique o valor informado')]]).read()
janela.close()
"""
"""
from tkinter import * #importa toda a biblioteca
janela = Tk() #define uma janela
janela.title('Janela') #Dá um nome a janela
janela.geometry('500x400+200+200') #método que permite dimensionar a janela e informar onde ela abrirá
janela.resizable(True, True) #True diz que é permitido redimensionar a janela usando o mouse. (false torna o tamanho fixo)
#janela.minsize(500, 400) #define o tamanho mínimo que a janela pode ter
#janela.maxsize(600, 600) #define o tamanho máximo que a janela pode ter
janela.state('zoomed') #começa com a janela no máximizada (obs.: se trocarmos zoomed por iconic, a janela começa minimizada)
janela.iconbitmap('icone.ico')
janela['bg'] = 'red'
botao = Button(janela, text = 'Próximo') # botão
botao.pack() # necessário para que o botao apareça
janela.mainloop() #mantem a janela principal aberta
"""
"""
from tkinter import *
janela = Tk()
janela.title('Título da Janela =D')
janela.iconbitmap('icosaedro.ico')
janela.geometry('500x350')
def funcao():
    return print('Olá, Mundo!')
botao = Button(janela, text = 'Botão', command = lambda: funcao())
botao.pack()
janela.mainloop()
"""
"""
from tkinter import *
janela = Tk()
janela.title('Janela')
#tamanho da janela
largura = 500
altura = 300
#resolução do nosso sistema
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
#posição da janela
x = largura_tela/2 - largura/2
y = altura_tela/2 - altura/2
janela.geometry('%dx%d+%d+%d'% (largura, altura, x, y))
janela.mainloop()
"""
"""
x = 1
y = 2
print('%d é igual à %d/%d'% (x, y, y))
"""
"""
from tkinter import *
janela = Tk()
janela.title('Janela...')
janela.iconbitmap('dados3.ico')
janela.state('zoomed')
label_1 = Label(janela, text = 'Este é o label_1')
label_1.pack()
label_2 = Label(janela, text = 'Este é o label_2')
label_2.pack()
botao = Button(janela, text = 'Executar')
botao.pack()
botao2 = Button(janela, text = 'Cancelar')
botao2.pack()
# IMPORTANTE, a ordem em que eu coloco os ___.pack() indica a ordem em que eles apareceram na janela
# Por exemplo, se eu colocar o botao2.pack() antes do label_1.pack(), então, o botao2 aparece antes (é necessário que o
# batao2 esteja definido em alguma linha acima da linha do .pack()
janela.mainloop()
"""
"""
from tkinter import *
janela = Tk()
janela.title('Título!')
janela.iconbitmap('dados3.ico')
largura = 500
altura = 300
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
x = largura_tela / 2 - largura / 2
y = altura_tela / 2 - altura / 2
janela.geometry('%dx%d+%d+%d'% (largura, altura, x, y))
label_1 = Label(janela,
                text = 'Este é o label 1',
                bg = 'red',
                fg = 'black',
                font = 'Times 20 bold')
#CODIGO HEXADECIMAL DE CORES: sempre é #__(red) __(green) __(blue), mas sem os espaços e sem os nomes das cores... 
#Exemplo, o vermelho: #FF0000, ou seja F que no hexadecimal é 16, temos 255 (na base 10) para o vermelho, 0 para o verde
#e 0 para o azul. 
label_1.pack()
# Testando o código hexadecimal de cores:
label_2 = Label(janela,
                text = 'Este é o label 2',
                bg = '#0000FF',
                fg = '#CCCCCC',
                font = 'Arial 10 italic')
label_2.pack()
janela.mainloop()
"""
"""
from tkinter import *
janela = Tk()
janela.title('Aprendendo Tkinter')
janela.iconbitmap('dados3.ico')
label_1 = Label(janela, text = 'Este é o Label 1',
                bg = 'red',
                font = 'Arial 20')
label_1.pack()
janela.mainloop()
"""
"""
for i in range(0,3):
    print('Passo; Pula')
print('Passo\nPega.')
"""
"""
for i in range(7, 0, -2):
    print(int((1/((5) ** 0.5)) * ((((1 + (5 ** 0.5)) / 2) ** i) - ((1 - (5 ** 0.5)) / 2) ** i)))
"""
"""
n = int(input('Digite um número: '))
for i in range(0, 11):
    print('{:2} x {:2} = {}'.format(n, i, n * i))
"""
"""
i = int(input('Início: '))
f = int(input('Final: '))
p = int(input('Passo (ou razão): '))
if p >= 0:
    for j in range(i, f + 1, p):
        print(j)
else:
    for j in range(i, f - 1, p):
        print(j)
"""
"""
from time import sleep
import emoji

for i in range(10, -1, -1):
    sleep(1)
    print(i)
print(emoji.emojize(':boom::boom::boom::boom::boom:', use_aliases=True))
"""
"""
for i in range(2, 51, 2):
    print(i)
"""
"""
from math import fmod
s = 0
for i in range(3, 501, 3):
    if fmod(i, 2) == 0:
        pass
    else:
        s = s + i
print(s)
"""
"""
from math import fmod
qtd = int(input('Quantos números você irá digitar? '))
numeros = []
for i in range(1, qtd + 1):
    numeros.append(int(input('Digite o {}º número: '.format(i))))
s = 0
for i in numeros:
    if fmod(i, 2) == 0:
        s += i
    else:
        pass
print(s)
"""
"""
n = float(input('Digite o primeiro termo: '))
r = float(input('Digite a razão: '))
for i in range(0, 11):
    print(n + i * r)
"""
"""
from math import fmod
verificador = [1]
n = int(input('Digite um número inteiro: '))
for i in range(2, n):
    if fmod(n, i) == 0:
        verificador.append(i)
    else:
        pass
if (verificador == [1]) and (n != 1):
    print('Sim! o número {} é primo.'.format(n))
else:
    print('Não, o número {} não é primo...'.format(n))
verificador.append(n)
print('\nOs divisores de {} são:'.format(n))
print(verificador)
"""
"""
frase = input('Digite uma frase: ')
elementos1 = []
elementos2 = []
for i in frase.upper():
    if not i.isspace():
        elementos1.insert(0, i)
for i in frase.upper():
    if not i.isspace():
        elementos2.append(i)
if elementos1 == elementos2:
    print('Sim! a frase é um palíndromo!')
else:
    print('Não, a frase não é um palíndromo...')
"""
"""
qtd = int(input('Quantas pessoas serão analisadas? '))
maiores = []
for i in range(1, qtd + 1):
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i)))
    if idade >= 18:
        maiores.append(idade)
print('Dessas pessoas, {} são maiores de idade e {} são menores.'.format(len(maiores), abs(len(maiores) - qtd)))
"""
"""
qtd = int(input("Quantas pessoas partiparam da pesquisa? "))
maior = [0]
menor = [1000000000]
for i in range(1, qtd + 1):
    p = int(input('Digite o peso da {}ª pessoa: '.format(i)))
    if p > maior[0]:
        maior.insert(0, p)
    elif p < menor[0]:
        menor.insert(0, p)
print('O maior peso foi {}\nO menor peso é {}'.format(maior[0], menor[0]))
"""
"""
from math import fsum
qtd = int(input('Quantas pessoas participaram da pesquisa: '))
idades = []
oveio = [0]
idadedoveio = [0]
m_maiorde20 = []
for i in range(1, qtd + 1):
    idade = int(input('Sobre a {}ª pessoa, digite...\nIdade: '.format(i)))
    nome = input('Nome: ')
    genero = input('sexo [h / m]: ')
    if genero == 'h':
        if idade > int(idadedoveio[0]):
            oveio.insert(0, nome)
            idadedoveio.insert(0, idade)
    elif genero == 'm':
        if idade >= 10:
            m_maiorde20.append(nome)
    idades.append(idade)
print('O homem mais velho é {};'
      '\nentre as mulheres da lista, {} são tem mais de 20 anos;'
      '\ne a média das idade é {}'.format(oveio[0], len(m_maiorde20), fsum(idades)/len(idades)))
"""
"""
m = 0
h = 0
r = ''
contador = 1
print('Digite SAIR, para finalizar.')
while r.upper() != 'SAIR':
    r = input('{:2}º Genero: '.format(contador))
    if r.upper() == 'MULHER':
        m = m + 1
    elif r.upper() == 'HOMEM':
        h = h + 1
    elif r.upper() == 'SAIR':
        pass
    else:
        print('O valor digitado não é aceitado. Por favor digite o genero da pessoa ou dê o comando para sair.')
        contador = contador - 1
    contador = contador + 1
print('Há {} homens e {} mulheres.'.format(h, m))
"""
"""
from random import randint
m = -1
n = -2
while n != m:
    n = randint(0, 10)
    m = int(input('Informe um inteiro de 0 a 10: '))
    if m == n:
        print('Parabéns! Você acertou!')
        break
    else:
        print('Você errou. O valor correto é {}.'.format(n))
"""
"""
from math import fsum
numeros = []
i = 1
r = 'oi'
print('Digite S para terminar de adicionar números.')
while r.upper() != 'S':
    r = input('Digite o {}º número (ou S, para terminar): '.format(i))
    if r.isnumeric():
        numeros.append(float(r))
    i = i + 1
i = i + 1
j = -1
print('[1] SOMA\n[2] MULTIPLICAR\n[3] MAIOR\n[4]ADICIONAR MAIS NÚMEROS\n[5] SAIR')
while j != 5:
    k = int(input('Digte o número da fução que deseja realizar: '))
    if k == 1:
        print(fsum(numeros))
    elif k == 2:
        m = 1
        for i in numeros:
            m = m * i
        print(m)
    elif k == 3:
        print(max(numeros))
    elif k == 4:
        r = 'oi'
        while r.upper() != 'S':
            r = input('Digite o {}º número (ou S, para terminar): '.format(i))
            if r.isnumeric():
                numeros.append(float(r))
            i = i + 1
    elif k == 5:
        break
"""
"""
from math import fmod
n = int(input('Você deseja ver até que termo da sequência de Fibonacci? '))
for i in range(0, n):
    if fmod(i, 10) != 0:
        print(int((1 / ((5) ** 0.5)) * ((((1 + (5 ** 0.5)) / 2) ** i) - ((1 - (5 ** 0.5)) / 2) ** i)), end='   ')
    else:
        print('\n', int((1 / ((5) ** 0.5)) * ((((1 + (5 ** 0.5)) / 2) ** i) - ((1 - (5 ** 0.5)) / 2) ** i)), end='   ')
"""
"""
import PySimpleGUI as sg
from math import fsum
numeros = []
i = 0
layout = [
    [sg.Text('Para adicionar um novo número você deve apagar o anterior.')],
    [sg.Text('... é, eu sei, é uma merda mesmo... Mas se não for assim, não será.')],
    [sg.InputText()],
    [sg.Button('Adicionar'), sg.Button('Media'), sg.Button('Maior'), sg.Button('Menor')],
    [sg.Button('Fechar')]
]
janela = sg.Window('Média, Máximo e Mínimo', layout)
while True:
    events, values = janela.read()
    if (events == 'Fechar') or (events == sg.WIN_CLOSED):
        break
    elif events == 'Adicionar':
        numeros.append(float(values[i]))
    elif events == 'Media':
        print(fsum(numeros)/len(numeros))
    elif events == 'Maior':
        print(max(numeros))
    elif events == 'Menor':
        print(min(numeros))
janela.close()
"""
"""
print('Esse código mostra a taboada de qualquer número racional.'
      ' \nPara sair do programa, digite Sair')
while True:
    n = input('Digite um número para ver a sua taboada: ')
    if n.upper() == 'SAIR':
        break
    elif n.isnumeric():
        for i in range(0, 11):
            print(f'{int(n):2} x {i:2} = {int(n) * i}')
"""
"""
import PySimpleGUI as sg
qth = 0
qtm_menor20 = 0
qt_maior18 = 0
layout = [
    [sg.Text('Digite abaixo, o que se pede.')],
    [sg.Text('Gênero [m / h]'), sg.InputText()],
    [sg.Text('Idade'), sg.InputText()],
    [sg.Button('Adicionar'), sg.Button('Resultado')],
    [sg.Button('Fechar')]
]
janela = sg.Window('Mostra um monte de coisa', layout)
while True:
    events, values = janela.read()
    if events == 'Fechar':
        break
    elif events == 'Adicionar':
        if values[0] == 'h':
            qth += 1
            print(f'{values[0]} e {values[1]} {qth}')
            if int(values[1]) >= 18:
                qt_maior18 += 1
                print(f'{values[0]} e {values[1]} {qt_maior18}')
        else:
            if (values[0] == 'm') and int(values[1]) < 20:
                qtm_menor20 += 1
                print(f'{values[0]} e {values[1]} {qtm_menor20}')
            if int(values[1]) >= 18:
                qt_maior18 += 1
                print(f'{values[0]} e {values[1]} {qt_maior18}')
    elif events == 'Resultado':
        print(f'A quantidade de mulheres com menos de 20 anos é {qtm_menor20}'
              f'\nA quantidade de homens é {qth}\nE a quantidade de pessoas maiores de idade é {qt_maior18}')
        break
janela.close()
"""
"""
# array = ('comida', 'lanche', 'bebida')
# for i, b in enumerate(array):
#     print(f'{i} e {b}')    
# Nova função: enumerate(array), no for, o i mostra a posição e o b, o objeto.
"""
"""
# a = (1, 2, 3, 4)
# b = (8, 5, 3, 2, 1, 1)
# print(a + b, b + a)
"""
"""
# Fração continua 1 + (1/ 1 + (1/ 1 + (1/ ...))) -> x = 1 + 1 / x
from random import random, randint

x = randint(-100, 100) * random()
print(f'f(x) = 1 + 1 / x\nx = {x}')
x = 1 + 1 / x
print(f'f(x) = 1 + 1/x = {x}')

while True:
    c = input('Precione I para iterar, ou S para finalizar: ')
    if c.upper() == 'I':
        x = 1 + 1 / x
        print(f'f(x) = 1 + 1/x = {x}')
    else:
        break
"""
"""
# Exercícios Tuples
from math import fmod
tupla = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
              'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta',
              'oitenta', 'noventa', 'centi', 'dozentos', 'trezentos', 'quatrocentos', 'quinhentos', 'ceicentos', 'setecentos',
         'oitocentos', 'novecentos', 'mil')

fechar = [0]

while fechar[0] == 0:
    n = int(input('Digite um número inteiro de 1 à 1000: '))
    digitos = [int(fmod(n - fmod(n, 100), 1000)), int(fmod(n - fmod(n, 10), 100)), int(fmod(n, 10))]
    nomenum = []

    if 0 < n <= 20:
        print(tupla[n - 1])
        fechar.insert(0, 1)
    elif 20 < n <= 1000:
        if n != 1000:
            for i in digitos:
                if i != 0:
                    if (i == digitos[0]) and (digitos[0] == 100) and (digitos[1] == 0) and (digitos[2] == 0):
                        nomenum.insert(0, 'cem')
                    elif (i == digitos[0]):
                        nomenum.insert(0, tupla[26 + (i // 100)])
                    elif i == digitos[1]:
                        if (i == 10) and (digitos[2] != 0):
                            nomenum.insert(1, tupla[9 + int(digitos[2])])
                        elif (i == 10) and (digitos[2] == 0):
                            nomenum.insert(1, tupla[9])
                        else:
                            nomenum.insert(1, tupla[17 + (i // 10)])
                    elif (i == digitos[2]) and (digitos[1] != 10):
                        nomenum.append(tupla[i - 1])
            print(' e '.join(nomenum))

            fechar.insert(0, 1)
        elif n == 1000:
            print('mil')
            fechar.insert(0, 1)
    elif not (0 < n <= 1000):
        print(f'O  valor {n} não é reconhecido é um número entre 1 e 1000.\nPor favor, tente novamente.')
"""
# cod = dict({})
# valorcod = dict({})
# for i in range(1, 27):
#    e = input(f'Digite o {1 + len(cod)}º elemento: ')
#    cod[len(cod)] = e
#    valorcod[e] = len(cod) - 1
# print(valorcod)
# print(cod)
# """
# import PySimpleGUI as sg
#
# valorcod = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13,
#             'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, ' ': '--'}
#
# cod = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n',
#        14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z', '-': '', '--': ' '}
#
# layout = [
#     [sg.InputText()],
#     [sg.Button('[código] / [palavra]'), sg.Button('[palavra / código]')],
#     [sg.Button('Fechar')]
# ]
# janela = sg.Window('Tradução', layout)
#
# while True:
#     events, values = janela.read()
#     if events == 'Fechar':
#         break
#     elif events == '[código] / [palavra]':
#         for i in values:
#             for k in i:
#                 codpala = []
#                 codpala.append(valorcod[k])
#         sg.Window('[código] / [palavra]', [[sg.Text(''.join(codpala))]]).read()
#     elif events == '[palavra / código]':
#         for i in values:
#             for k in i:
#                 codpala = []
#                 codpala.append(cod[k])
#         sg.Window('[palavra / código]', [[sg.Text(''.join(codpala))]]).read()
# janela.close()
# """

# Bibliotecas

import PySimpleGUI as sg
import numpy as np

# Tabelas de singularidades e diâmetros nominais.

CompEqRosq = [1.1, 1.34, 1.58, 2, 2.25, 2.6, 2.8, 3.4, 3.7, 34, 0, 0, 0, 0, 0.67, 0.7, 0.83, 0.98, 1, 1.1,
              1.1, 1.2, 1.3, 1.4, 0, 0, 0, 0, 0.21, 0.28, 0.39, 0.52, 0.64, 0.83, 0.97, 1.2, 1.45, 1.7, 0, 0, 0, 0,
              1.1, 1.3, 1.6, 2, 2.3, 2.6, 2.8, 3.4, 3.7, 4, 0, 0, 0, 0, 0.52, 0.73, 0.99, 1.4, 1.7, 2.3, 2.8, 3.7, 4.45,
              5.2, 0, 0, 0, 0, 1.3, 1.6, 2, 2.7, 3, 3.7, 3.9, 5.2, 5.8, 6.4, 0, 0, 0, 0, 0.17, 0.2, 0.25, 0.34, 0.37,
              0.46,
              0.52, 0.58, 0.67, 0.76, 0, 0, 0, 0, 6.7, 7.3, 8.8, 11.3, 12.8, 16.5, 18.9, 24, 27.25, 33.5, 0, 0, 0, 0,
              4.6, 4.6,
              5.2, 5.5, 5.5, 5.55, 5.55, 5.55, 5.55, 5.55, 0, 0, 0, 0, 2.4, 2.7, 3.4, 4, 4.6, 5.8, 6.7, 8.2, 9.7, 11.6,
              0, 0, 0,
              0, 0.07, 0.07, 0.08, 0.11, 0.12, 0.14, 0.14, 0.16, 0.175, 0.19, 0, 0, 0, 0]
CER = np.array(CompEqRosq).reshape(11, 14)
# o elemnto C1,3 = CER[0][2]

CompEqFlan = [0.3, 0.37, 0.5, 0.62, 0.73, 0.95, 1.1, 1.3, 1.55, 1.8, 2.2, 2.7, 3.7, 4.3,
              0.33, 0.4, 0.49, 0.61, 0.7, 0.83, 0.88, 1, 1.15, 1.3, 1.5, 1.7, 2.1, 2.4,
              0.14, 0.18, 0.25, 0.34, 0.4, 0.52, 0.61, 0.8, 0.95, 1.1, 1.4, 1.7, 2.3, 2.7,
              0.34, 0.4, 0.49, 0.61, 0.7, 0.83, 0.88, 1, 1.15, 1.3, 1.5, 1.7, 2.1, 2.4,
              0.21, 0.25, 0.3, 0.4, 0.45, 0.55, 0.58, 0.67, 0.74, 0.85, 1, 1.2, 1.4, 1.6,
              0.61, 0.8, 1, 1.3, 1.6, 2, 2.3, 2.9, 3.3, 3.7, 4.6, 5.5, 7.3, 9.1, 0, 0, 0,
              0, 0, 0.8, 0.83, 0.85, 0.86, 0.88, 0.95, 0.98, 0.98, 0.98, 11.6, 12.2, 13.7,
              16.5, 18, 21.4, 23.5, 28.7, 32.65, 36.6, 45.7, 47.9, 49.3, 94.5, 4.6, 4.6, 5.2,
              5.5, 5.5, 6.4, 6.7, 8.5, 10.05, 11.6, 15.2, 19.2, 27.4, 36.6,
              1.2, 1.6, 2.2, 3, 3.7, 5.2, 6.4, 8.3, 9.6, 11.6, 15.2,
              19.2, 27.4, 36.6, 1.5, 2, 2.3, 5.5,
              8.1, 8.3, 8.8, 10.4, 11.6, 12.8, 16.2, 18.6, 0, 0]
CEF = np.array(CompEqFlan).reshape(11, 14)

ComponenteSIG = {'90° Cotovelo comum': 0, 'Curva 90° raio longo': 1, 'Curva 45°': 2, 'Curva 180° raio longo': 3,
                 'Tê fluxo em linha': 4, 'Tê fluxo pelo ramal': 5, 'Válvula gaveta': 6, 'Válvula globo': 7,
                 'Válvula angular': 8, 'Válvula de retenção portinhola': 9, 'União filtroY': 10}
DiametroSIG = {0.5: 0, 0.75: 1, 1: 2, 1.25: 3, 1.5: 4, 2: 5, 2.5: 6, 3: 7, 3.5: 8, 4: 9, 5: 10, 6: 11, 8: 12, 10: 13}

A = ['90° Cotovelo comum', 'Curva 90° raio longo', 'Curva 45°', 'Curva 180° raio longo',
     'Tê fluxo em linha', 'Tê fluxo pelo ramal', 'Válvula gaveta', 'Válvula globo',
     'Válvula angular', 'Válvula de retenção portinhola', 'União filtroY']


# Funções

# Conversão para Bar
def bar(m, u):
    equivalentes = {'Pa': 10 ** (-5), 'kPa': 10 ** (-2), 'Psi': 0.0689476, 'atm': 1.01325, 'Torr': 0.00133322, 'Bar': 1,
                    'kgf/cm²': 0.980665}

    return m * equivalentes[u]


def vazao(m, u):
    equivalentes = {'m³/h': 1, 'L/s': 3.6, 'L/min': 0.06}

    return m * equivalentes[u]


# Diâmetro
def diametro(V, c, s, deltap, p):
    d = 10 * ((1.663785 * (10 ** -3) * (V ** 1.85) * (c + s)) / (deltap * p)) ** (1 / 5)  # em mm.

    return d


def diametronominal(V, c, deltap, p):
    k = 10 * ((1.663785 * (10 ** -3) * (V ** 1.85) * c) / (deltap * p)) ** (1 / 5) * 0.0393701

    diametronominal = [0.5, 0.75, 1, 1.25, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 8, 10]

    d = list(filter(lambda i: i > k, diametronominal))[0]  # em polegadas.

    return d


# Pesquisa do comprimento equivalente
def singularidade(nome, diametro, RoF):
    if RoF == 'F':
        return CEF[nome][DiametroSIG[diametro]]
    else:
        return CER[nome][DiametroSIG[diametro]]


def multiplicaçaolista(a, b):
    k = 0

    for i in a:
        k = k + i * b[a.index(i)]
    return k


# Layout

sg.theme('LightBrown3')

aba1 = [
    [sg.Text('Esse programa tem o propósito de dimensionar uma tubulação de ar comprimido.')],
    [sg.Text('As unidades padrão desse software são:')],
    [sg.Text('Vazão: m³/h')],
    [sg.Text('Pressão: Bar')],
    [sg.Text('Comprimento: m')],
    [sg.Text('Sinta-se livre para alterar as unidade de entrada de acordo com a sua preferência.')],
    [sg.Text('As unidades escolhidas aqui serão usadas em todas as entradas.')],
    [sg.Text('Vazão', size=(9, 1)),
     sg.Combo(['m³/h', 'L/min', 'L/s'], size=(9, 1), default_value='m³/h', key='unidadevazao')],
    [sg.Text('Pressão', size=(9, 1)),
     sg.Combo(['Pa', 'kPa', 'psi', 'atm', 'Torr', 'Bar', 'kgf/cm²'], size=(9, 1), default_value='Bar',
              key='unidadepressao')]
]

aba2 = [
    [sg.Text('Vazão Nominal', size=(50, 1)), sg.InputText(size=(10, 1), key='V')],
    [sg.Text('Expetativa de expansão', size=(50, 1)), sg.InputText(size=(10, 1), key='ExpExp')],
    [sg.Text('Pressão de Trabalho', size=(50, 1)), sg.InputText(size=(10, 1), key='p')],
    [sg.Text('Perdas admissíveis na linha Tronco', size=(50, 1)), sg.InputText(size=(10, 1), key='dpT')],
    [sg.Text('Perdas admissíveis na linha Secundária', size=(50, 1)), sg.InputText(size=(10, 1), key='dpS')],
    [sg.Text('Perdas admissíveis na linha Alimentação', size=(50, 1)), sg.InputText(size=(10, 1), key='dpA')],
    [sg.Text('Núm. linhas de rede secundária', size=(50, 1)), sg.InputText(size=(10, 1), key='Ns')],
    [sg.Text('Núm. linhas de rede de alimentação', size=(50, 1)), sg.InputText(size=(10, 1), key='Na')],
    [sg.Text('Comprimento Tronco', size=(50, 1)), sg.InputText(size=(10, 1), key='ComprT')],
    [sg.Text('Comprimento Secundária', size=(50, 1)), sg.InputText(size=(10, 1), key='ComprS')],
    [sg.Text('Comprimento Alimentação', size=(50, 1)), sg.InputText(size=(10, 1), key='ComprA')]
]

aba3 = [
    [sg.Text('Singularidades Tronco', size=(52, 1)), sg.Text('Quantidade')],
    [sg.Checkbox('90° Cotovelo comum', size=(50, 1), default=False, key='90° Cotovelo comum Tronco1'),
     sg.InputText(size=(10, 1), key='90° Cotovelo comum Tronco12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='90° Cotovelo comum Tronco13')],
    [sg.Checkbox('Curva 90° raio longo', size=(50, 1), default=False, key='Curva 90° raio longo Tronco1'),
     sg.InputText(size=(10, 1), key='Curva 90° raio longo Tronco12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Curva 90° raio longo Tronco13')],
    [sg.Checkbox('Curva 45°', size=(50, 1), default=False, key='Curva 45° Tronco1'),
     sg.InputText(size=(10, 1), key='Curva 45° Tronco12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Curva 45° Tronco13')],
    [sg.Checkbox('Curva 180° raio longo', size=(50, 1), default=False, key='Curva 180° raio longo Tronco1'),
     sg.InputText(size=(10, 1), key='Curva 180° raio longo Tronco12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Curva 180° raio longo Tronco13')],
    [sg.Checkbox('Tê fluxo em linha', size=(50, 1), default=False, key='Tê fluxo em linha Tronco1'),
     sg.InputText(size=(10, 1), key='Tê fluxo em linha Tronco12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Tê fluxo em linha Tronco13')],
    [sg.Checkbox('Tê fluxo pelo ramal', size=(50, 1), default=False, key='Tê fluxo pelo ramal Tronco1'),
     sg.InputText(size=(10, 1), key='Tê fluxo pelo ramal Tronco12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Tê fluxo pelo ramal Tronco13')],
    [sg.Checkbox('Válvula gaveta', size=(50, 1), default=False, key='Válvula gaveta Tronco1'),
     sg.InputText(size=(10, 1), key='Válvula gaveta Tronco12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Válvula gaveta Tronco13')],
    [sg.Checkbox('Válvula globo', size=(50, 1), default=False, key='Válvula globo Tronco1'),
     sg.InputText(size=(10, 1), key='Válvula globo Tronco12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Válvula globo Tronco13')],
    [sg.Checkbox('Válvula angular', size=(50, 1), default=False, key='Válvula angular Tronco1'),
     sg.InputText(size=(10, 1), key='Válvula angular Tronco12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Válvula angular Tronco13')],
    [sg.Checkbox('Válvula de retenção portinhola', size=(50, 1), default=False,
                 key='Válvula de retenção portinhola Tronco1'),
     sg.InputText(size=(10, 1), key='Válvula de retenção portinhola Tronco12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Válvula de retenção portinhola Tronco13')],
    [sg.Checkbox('União filtroY', size=(50, 1), default=False, key='União filtroY Tronco1'),
     sg.InputText(size=(10, 1), key='União filtroY Tronco12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='União filtroY Tronco13')]
]

aba4 = [
    [sg.Text('Singularidades Secundário', size=(52, 1)), sg.Text('Quantidade')],
    [sg.Checkbox('90° Cotovelo comum', size=(50, 1), default=False, key='90° Cotovelo comum Secundário1'),
     sg.InputText(size=(10, 1), key='90° Cotovelo comum Secundário12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='90° Cotovelo comum Secundário13')],
    [sg.Checkbox('Curva 90° raio longo', size=(50, 1), default=False, key='Curva 90° raio longo Secundário1'),
     sg.InputText(size=(10, 1), key='Curva 90° raio longo Secundário12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Curva 90° raio longo Secundário13')],
    [sg.Checkbox('Curva 45°', size=(50, 1), default=False, key='Curva 45° Secundário1'),
     sg.InputText(size=(10, 1), key='Curva 45° Secundário12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Curva 45° Secundário13')],
    [sg.Checkbox('Curva 180° raio longo', size=(50, 1), default=False, key='Curva 180° raio longo Secundário1'),
     sg.InputText(size=(10, 1), key='Curva 180° raio longo Secundário12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Curva 180° raio longo Secundário13')],
    [sg.Checkbox('Tê fluxo em linha', size=(50, 1), default=False, key='Tê fluxo em linha Secundário1'),
     sg.InputText(size=(10, 1), key='Tê fluxo em linha Secundário12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Tê fluxo em linha Secundário13')],
    [sg.Checkbox('Tê fluxo pelo ramal', size=(50, 1), default=False, key='Tê fluxo pelo ramal Secundário1'),
     sg.InputText(size=(10, 1), key='Tê fluxo pelo ramal Secundário12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Tê fluxo pelo ramal Secundário13')],
    [sg.Checkbox('Válvula gaveta', size=(50, 1), default=False, key='Válvula gaveta Secundário1'),
     sg.InputText(size=(10, 1), key='Válvula gaveta Secundário12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Válvula gaveta Secundário13')],
    [sg.Checkbox('Válvula globo', size=(50, 1), default=False, key='Válvula globo Secundário1'),
     sg.InputText(size=(10, 1), key='Válvula globo Secundário12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Válvula globo Secundário3')],
    [sg.Checkbox('Válvula angular', size=(50, 1), default=False, key='Válvula angular Secundário1'),
     sg.InputText(size=(10, 1), key='Válvula angular Secundário12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Válvula angular Secundário13')],
    [sg.Checkbox('Válvula de retenção portinhola', size=(50, 1), default=False,
                 key='Válvula de retenção portinhola Secundário1'),
     sg.InputText(size=(10, 1), key='Válvula de retenção portinhola Secundário12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Válvula de retenção portinhola Secundário13')],
    [sg.Checkbox('União filtroY', size=(50, 1), default=False, key='União filtroY Secundário1'),
     sg.InputText(size=(10, 1), key='União filtroY Secundário12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='União filtroY Secundário13')]
]

aba5 = [
    [sg.Text('Singularidades Alimentação', size=(52, 1)), sg.Text('Quantidade')],
    [sg.Checkbox('90° Cotovelo comum', size=(50, 1), default=False, key='90° Cotovelo comum Alimentação1'),
     sg.InputText(size=(10, 1), key='90° Cotovelo comum Alimentação12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='90° Cotovelo comum Alimentação13')],
    [sg.Checkbox('Curva 90° raio longo', size=(50, 1), default=False, key='Curva 90° raio longo Alimentação1'),
     sg.InputText(size=(10, 1), key='Curva 90° raio longo Alimentação12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Curva 90° raio longo Alimentação13')],
    [sg.Checkbox('Curva 45°', size=(50, 1), default=False, key='Curva 45° Alimentação1'),
     sg.InputText(size=(10, 1), key='Curva 45° Alimentação12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Curva 45° Alimentação13')],
    [sg.Checkbox('Curva 180° raio longo', size=(50, 1), default=False, key='Curva 180° raio longo Alimentação1'),
     sg.InputText(size=(10, 1), key='Curva 180° raio longo Alimentação12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Curva 180° raio longo Alimentação13')],
    [sg.Checkbox('Tê fluxo em linha', size=(50, 1), default=False, key='Tê fluxo em linha Alimentação1'),
     sg.InputText(size=(10, 1), key='Tê fluxo em linha Alimentação12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Tê fluxo em linha Alimentação13')],
    [sg.Checkbox('Tê fluxo pelo ramal', size=(50, 1), default=False, key='Tê fluxo pelo ramal Alimentação1'),
     sg.InputText(size=(10, 1), key='Tê fluxo pelo ramal Alimentação12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Tê fluxo pelo ramal Alimentação13')],
    [sg.Checkbox('Válvula gaveta', size=(50, 1), default=False, key='Válvula gaveta Alimentação1'),
     sg.InputText(size=(10, 1), key='Válvula gaveta Alimentação12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Válvula gaveta Alimentação13')],
    [sg.Checkbox('Válvula globo', size=(50, 1), default=False, key='Válvula globo Alimentação1'),
     sg.InputText(size=(10, 1), key='Válvula globo Alimentação12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Válvula globo Alimentação13')],
    [sg.Checkbox('Válvula angular', size=(50, 1), default=False, key='Válvula angular Alimentação1'),
     sg.InputText(size=(10, 1), key='Válvula angular Alimentação12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='Válvula angular Alimentação13')],
    [sg.Checkbox('Válvula de retenção portinhola', size=(50, 1), default=False,
                 key='Válvula de retenção portinhola Alimentação1'),
     sg.InputText(size=(10, 1), key='Válvula de retenção portinhola Alimentação12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ',
              key='Válvula de retenção portinhola Alimentação13')],
    [sg.Checkbox('União filtroY', size=(50, 1), default=False, key='União filtroY Alimentação1'),
     sg.InputText(size=(10, 1), key='União filtroY Alimentação12'),
     sg.Combo(['ROSQ', 'FLAN'], size=(10, 1), default_value='ROSQ', key='União filtroY Alimentação13')]
]

layout = [
    [sg.TabGroup([
        [sg.Tab('Introdução', aba1), sg.Tab('Variáveis Básicas', aba2), sg.Tab('Singularidade Tronco', aba3),
         sg.Tab('Singularidade Segundário', aba4), sg.Tab('Singularidade Alimentação', aba5)]
    ])],
    [sg.Button('Calcular'), sg.Button('Cancelar')]
]

# Janela e Solução

janela = sg.Window('Dimensionador de Tubulação de ar comprimido', layout)

while True:
    events, values = janela.read()

    if events in ('Cancelar', sg.WIN_CLOSED):

        break
    elif events == 'Calcular':

        # Vazão Real
        vazaoT = vazao(float(values['V']) * (1 + float(values['ExpExp'])), values['unidadevazao'])

        # Diametro nominal para pesquisar as singularidades
        diametronominalT = diametronominal(vazaoT, float(values['ComprT']),
                                           bar(float(values['dpT']), values['unidadepressao']),
                                           bar(float(values['p']), values['unidadepressao']))

        # Teste para a lista de singularidades selecionadas
        # s tronco
        nomesT = ['90° Cotovelo comum Tronco1', 'Curva 90° raio longo Tronco1', 'Curva 45° Tronco1',
                  'Curva 180° raio longo Tronco1',
                  'Tê fluxo em linha Tronco1', 'Tê fluxo pelo ramal Tronco1', 'Válvula gaveta Tronco1',
                  'Válvula globo Tronco1',
                  'Válvula angular Tronco1', 'Válvula de retenção portinhola Tronco1', 'União filtroY Tronco1']

        NOMETRONCO = []
        RoFTronco = []
        QtdTronco = []

        for i in nomesT:

            if values[i] == True:
                NOMETRONCO.append(nomesT.index(i))
                j = i + '3'
                RoFTronco.append(values[j])
                j = i + '2'
                QtdTronco.append(float(values[j]))

        CompEquiT = [singularidade(i, diametronominalT, RoFTronco[NOMETRONCO.index(i)]) for i in NOMETRONCO]

        sTronco = multiplicaçaolista(CompEquiT, QtdTronco)
        print(multiplicaçaolista(CompEquiT, QtdTronco))

        print(diametronominalT)
        print(CompEquiT)
        print(NOMETRONCO)
        print(RoFTronco)
        print(QtdTronco)
        Dtronco = diametro(vazaoT, float(values['ComprT']), sTronco,
                           bar(float(values['dpT']), values['unidadepressao']),
                           bar(float(values['p']), values['unidadepressao']))

        # s secundário
        if float(values['Ns']) != 0:

            vazaoS = vazaoT / float(values['Ns'])

            diametronominalS = diametronominal(vazaoS, float(values['ComprS']),
                                               bar(float(values['dpS']), values['unidadepressao']),
                                               bar(float(values['p']), values['unidadepressao']))

            nomesS = ['90° Cotovelo comum Secundário1', 'Curva 90° raio longo Secundário1', 'Curva 45° Secundário1',
                      'Curva 180° raio longo Secundário1',
                      'Tê fluxo em linha Secundário1', 'Tê fluxo pelo ramal Secundário1', 'Válvula gaveta Secundário1',
                      'Válvula globo Secundário1',
                      'Válvula angular Secundário1', 'Válvula de retenção portinhola Secundário1',
                      'União filtroY Secundário1']

            NOMESECUNDARIO = []
            RoFSecundario = []
            QtdSecundario = []

            for i in nomesS:

                if values[i] == True:
                    NOMESECUNDARIO.append(nomesS.index(i))
                    j = i + '3'
                    RoFSecundario.append(values[j])
                    j = i + '2'
                    QtdSecundario.append(float(values[j]))

            CompEquiS = [singularidade(i, diametronominalS, RoFSecundario[NOMESECUNDARIO.index(i)]) for i in
                         NOMESECUNDARIO]

            sSecundario = multiplicaçaolista(CompEquiS, QtdSecundario)

            # Problema na pesquisa de comprimento equivalente???

            print(multiplicaçaolista(CompEquiS, QtdSecundario))
            print(diametronominalS)
            print(CompEquiS)
            print(NOMESECUNDARIO)
            print(RoFSecundario)
            print(QtdSecundario)
            Dsecundario = diametro(vazaoS, float(values['ComprS']), sSecundario,
                                   bar(float(values['dpS']), values['unidadepressao']),
                                   bar(float(values['p']), values['unidadepressao']))
            sg.Window('Diametro', [[sg.Text('Diâmetro da linha Secundária em mm:'), sg.Text(Dsecundario)]]).read()

        # s alimentação

        if float(values['Na']) != 0:

            vazaoA = vazaoS / float(values['Na'])

            diametronominalA = diametronominal(vazaoA, float(values['ComprA']),
                                               bar(float(values['dpA']), values['unidadepressao']),
                                               bar(float(values['p']), values['unidadepressao']))

            nomesA = ['90° Cotovelo comum Alimentação1', 'Curva 90° raio longo Alimentação1', 'Curva 45° Alimentação1',
                      'Curva 180° raio longo Alimentação1',
                      'Tê fluxo em linha Alimentação1', 'Tê fluxo pelo ramal Alimentação1',
                      'Válvula gaveta Alimentação1', 'Válvula globo Alimentação1',
                      'Válvula angular Alimentação1', 'Válvula de retenção portinhola Alimentação1',
                      'União filtroY Alimentação1']

            NOMEALIMENTAÇAO = []
            RoFAlimentaçao = []
            QtdAlimentaçao = []

            for i in nomesA:

                if values[i] == True:
                    NOMEALIMENTAÇAO.append(nomesA.index(i))
                    j = i + '3'
                    RoFAlimentaçao.append(values[j])
                    j = i + '2'
                    QtdAlimentaçao.append(float(values[j]))

            CompEquiA = [singularidade(i, diametronominalA, RoFAlimentaçao[NOMEALIMENTAÇAO.index(i)]) for i in
                         NOMEALIMENTAÇAO]

            sAlimentaçao = multiplicaçaolista(CompEquiA, QtdAlimentaçao)

            # Problema na pesquisa de comprimento equivalente???

            print(multiplicaçaolista(CompEquiA, QtdAlimentaçao))
            print(diametronominalA)
            print(CompEquiA)
            print(NOMEALIMENTAÇAO)
            print(RoFAlimentaçao)
            print(QtdAlimentaçao)
            Dalimentaçao = diametro(vazaoA, float(values['ComprA']), sAlimentaçao,
                                    bar(float(values['dpA']), values['unidadepressao']),
                                    bar(float(values['p']), values['unidadepressao']))
            sg.Window('Diametro', [[sg.Text('Diâmetro da linha de Alimentação em mm:'), sg.Text(Dalimentaçao)]]).read()

        # Diametro real em mm

        sg.Window('Diametro', [[sg.Text('Diâmetro do Tronco em mm:'), sg.Text(Dtronco)]]).read()

janela.close()
'''
'''
from Classes import Vetor

v = Vetor(10, -4, 0)
u = Vetor(1, 273, 0)

v.vetorial(u)
v.escalar(u)
'''
'''
a = input('Digite: ')
b = []
for n in a:
    if not n.isspace():
        b.append(n)
    else:
        pass
print(str(''.join(b)))
'''
# 'alguma coisa'.join(lista) junta todos os elementos da lista em um único elemento, e coloca 'alguma coisa' entre
# eles. Exemplo:
'''
lista = ['a', 'b', 'c', 'd', 'e']
print(str('Alguma coisa'.join(lista)))
lista1 = [1, 2, 3, 4, 5]
lista1 = list(map(lambda i: str(i), lista1))
print(str('A'.join(lista1)))
'''
'''
# lista de pares
k = int(input('Deseja ver a lista de pares até que número? '))
pares = list(filter(lambda i: i % 2 == 0, [i for i in range(0, k + 1)]))
print(pares)
'''
