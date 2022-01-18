def potencia(n, k):
    j: int = 1
    for _ in range(k):
        j *= n
    return print(j)
if __name__ == '__main__':
    potencia(2,4)