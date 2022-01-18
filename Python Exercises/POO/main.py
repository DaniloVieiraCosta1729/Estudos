from vetores import Vetor

v = Vetor(2, 0, 0)
u = Vetor(0, 2, 0)

print(v.escalar(u))
print(v.vetorial(u))
print(v.modulo())
print(v.cosdir())