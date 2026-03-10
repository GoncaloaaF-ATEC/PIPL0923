from Pessoa import Pessoa

p = Pessoa("Ana", 160, 45, 20)
p2 = Pessoa("Ana", 160, 45, 20)

print(p.nome)

str_p = str(p)  # "cast" de var -> criar uma str com o valor indicado

print(str_p)

"""

(int) "10"; -> 10  

"""
print(p > p2)
