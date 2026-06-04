from HKuteis import *

print(moda(1, 2, 2, 3, 3, 3))      # 3
print(moda(1, 1, 2, 2))             # 1
print(moda('x', 'y'))               # None
print(moda())                        # None

print(mediana(1, 3, 5))             # 3
print(mediana(1, 2, 3, 4))          # 2.5
print(mediana())                     # None (lista vazia — vê o que retorna)

print(variancia(2, 4, 4, 8))        # 4.75
print(variancia(1))                  # None
print(variancia())        

print(desvio_padrao(2, 4, 4, 8))    # 2.179...
print(desvio_padrao(1))              # None
print(desvio_padrao())               # None# None

print(eh_primo(7))          # True
print(eh_primo(4))          # False
print(eh_primo(1))          # False

print(mdc(12, 8))           # 4
print(mdc(9, 6))            # 3

print(mmc(4, 6))            # 12
print(mmc(3, 5))            # 15

print(fibonnaci(7))         # [0, 1, 1, 2, 3, 5, 8]
print(fibonnaci(1))         # [0, 1] ou [0]?