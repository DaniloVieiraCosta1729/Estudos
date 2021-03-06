class Vetor:

    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def escalar(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z
    
    def vetorial(self, v):
        a = self.y * v.z - self.z * v.y
        b = -(self.x * v.z - self.z * v.x)
        c = self.x * v.y - self.y * v.x
        return f'({a})i + ({b})j + ({c})k'
    
    def modulo(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def cosdir(self):
        cx = self.escalar(Vetor(1, 0, 0)) / self.modulo()
        cy = self.escalar(Vetor(0, 1, 0)) / self.modulo()
        cz = self.escalar(Vetor(0, 0, 1)) / self.modulo()
        return f'cos(a) = {cx}, cos(b) = {cy}, cos(c) = {cz}'

# Eu poderia ter usado arrays ou listas como input da função init, porque assim seria mais fácil de simular
# um espaço vetorial. Essa classe poderia ter um método soma, e outro método para o produto com relação a um
# escalar, cujo o resultado seria um novo vetor, i.e, teriamos o axioma de fecho da soma e do produto 
# "funcionando". Mas esse arquivo é apenas um exemplo de aplicação das classes em python, portanto, não
# há necessidade de alterar o exercício.