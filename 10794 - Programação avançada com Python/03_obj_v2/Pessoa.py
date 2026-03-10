class Pessoa:
    def __init__(self, nome: str, altura: float, peso: float, idade: int = 0):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso  # peso em gramas
        self.energia = 100
        self.acordado = True

    # por cada coisa que comer engorda 100g
    def comer(self, alimentos: list[str]):
        # for _ in alimentos:
        self.peso += (100 * alimentos.__len__())

    def falar(self):
        return "Bla bla bla"

    def andar(self):
        return "a pessoa esta a andar"

    def crescer(self, cm: float = 2.5):
        self.altura += cm

    # até aos 21 anos por cada ano que envelher vai crecer 2cm
    def envelhecer(self, anos: int = 1):
        if self.idade < 21:
            self.crescer()

        self.idade += anos

    def dormir(self):
        if self.acordado:
            self.acordado = False
            self.energia = 100

    # crie um metodo para acordar, garanta que so acorda se estiver a dormir
    def acordar(self):
        if not self.acordado:
            self.acordado = True

    def __gt__(self, other):
        return self.idade > other.idade

    def __str__(self):
        return "class convertida para string"
