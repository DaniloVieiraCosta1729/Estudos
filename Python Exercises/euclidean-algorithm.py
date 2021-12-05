# MDC entre dois inteiros positivos.
from math import floor

a = int(input('Digite um inteiro: '))
b = int(input('Digite outro inteiro: '))
r = max(a, b) + 1
mdc = f'mdc({a},{b})'
print(f'{a} = {b} x {floor(a / b)} + {a - b * (floor(a / b))}')

while r != 0:
    q = b
    b = a - b * (floor(a / b))
    a = q
    r = a - b * (floor(a / b))
    print(f'{a} = {b} x {floor(a / b)} + {a - b * (floor(a / b))}')
print(f'Assim, concluímos que {mdc} = mdc({b},{r}) = {b}')