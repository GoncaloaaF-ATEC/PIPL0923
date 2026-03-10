from modelos import Carro

c1 = Carro("BMW", "X1", "Azul", 2010)
c2 = Carro("ford", "Puma", "Amarelo", 2025)

print(c1.marca)
print(c2.marca)

c1.marca = "Bayerische Motoren Werke"
print(c1.marca)

print("-----------------")

print(c2.cor)
c2.mudar_cor("Preto")
print(c2.cor)
