from unicodedata import name

# class Computador():
#     def __init__(self, codigo, nome, aquisicao, vida, marca):
#         self.codigo = codigo
#         self.nome = nome
#         self.aquisicao = aquisicao
#         self.vida = vida
#         self.marca = marca
    
#     def alerta_manutencao(self):
#         #   Calcula todo o período de manutenção.
#         pass

# class Marca():
#     def __init__(self, codigo, nome):
#         self.codigo = codigo
#         self.nome = nome

# if __name__ == '__main__':
#     # instancias (objetos) de Marca.
#     dall = Marca(1, 'Dall')
#     lp = Marca(2, 'LP')
#     # instancias de Computador.
#     vastra = Computador(1, 'Vastra', '10/01/2020', 365, dall)
#     polvilion = Computador(2, 'Polvilion', '10/01/2020', 365, lp)

#     print(type(dall))
#     print(type(polvilion))
#     print(isinstance(dall, Marca))
#     print(isinstance(polvilion, Marca))
#     print(isinstance(polvilion, Computador))

# class Alunos():
#     def __init__(self, matricula, nome):
#         self.matricula = matricula
#         self.nome = nome
#         self.livros = []
    
#     def emprestado(self, livro):
#         self.livros.append(livro)
    
#     def devolve(self, livro):
#         if livro in self.livros:
#             self.livros.remove(livro)
#         else:
#             print(f'{self.nome} não pegou o livro {livro} emprestado. \nA lista de livros emprestados para {self.nome} é {self.livros}.')

# if __name__ == '__main__':
#     print(type(Alunos.emprestado))
#     jorge = Alunos(123450, 'Jorge')
#     print(type(jorge.emprestado))
#     jorge.emprestado('Matemática Elementar Vol.1')
#     jorge.emprestado('Curso de Física Básica - Mecânica, Vol.1')
#     jorge.emprestado('Álgebra Linear')
#     jorge.devolve('Curso de Física Básica - Mecânica, Vol.1')
#     print(jorge.livros)
#     jorge.devolve('Pathfinder')

# Herança
class Produto():
    def __init__(self, nome, imposto, custo):
        self.nome = nome
        self.imposto = imposto
        self.custo = custo

    def preco(self, quantidade):
        return (self.custo + self.custo * self.imposto) * quantidade

class Roupa(Produto):
    def __init__(self, nome, imposto, custo, tamanho):
        super().__init__(nome, imposto, custo)
        self.tamanho = tamanho

class Comida(Produto):
    def __init__(self, nome, imposto, custo, validade):
        super().__init__(nome, imposto, custo)
        self.validade = validade

if __name__ == '__main__':
    bola = Produto('Bola', 0.5, 120)
    macarrao = Comida('Macarrão', 0.4, 5, 30)
    camisa = Roupa('Camisa', 0.45, 40, 'G')
    print(f'{bola.preco(1)}\n{macarrao.preco(2)}\n{camisa.preco(1)}')
# perceba que o método preço de produto foi usado em objetos da classe Roupa e Comida! Isso, acontece
# porque informamos que Produto é a classe 'pai' de Roupa e Comida, assim, não houve a necessidade
# de reimplementar o método.
# Usamos a função super() para chamar o método __init__ de Produto: super().__init__(nome, imposto, custo)