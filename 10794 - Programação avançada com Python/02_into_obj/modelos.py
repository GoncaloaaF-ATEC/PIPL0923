"""
    marca
    modelo
    ano
    num_km
    cor
"""


class Carro:
    def __init__(self, marca: str, modelo: str, cor: str, ano: int):  # self -> this
        self.marca = marca.title()
        self.modelo = modelo.title()
        self.ano = ano
        self.num_km = 0
        self.cor = cor.title()

    def mudar_cor(self, cor: str):
        self.cor = cor.title()

    """
    assuma que o carro se desloca a uma velocidade constante 
    
    a velocidade deve ser expressa em km/h
    o tempo em minutos
    
    a função deve atualizar o num_km do carro
    """

    def andar(self, velocidade: int, tempo: int):
        pass

    # calcule o consumo de combustivel total do carro
    # assuma que o consumo e constante (x l por km)
    # devine o x onde fizer mais sentido
    def consumo(self):
        pass

# Crie a class livro (defina apenas os atributos)


# adiciona a data do livro (sem usar bibliotecas)
