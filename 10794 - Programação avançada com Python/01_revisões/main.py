"""

var
op com var

condições
loops

listas
dict
set

funçoes

"""

# Crie uma variável com um nome e mostre esse nome na consola

nome = "Gonçalo"
print(nome)

# escreva na consola a msg "Ola <Nome>", utilize 3 opções para mostrar a msg

print("Ola", nome)
print("Ola " + nome)

print(f"Ola {nome}")  # <--

print("Ola {}".format(nome))

# escreva na consola a msg "Ola <Nome> em <ano>", utilize 3 opções para mostrar a msg

ano = 2026
print("Ola", nome, "em", ano)
print("Ola " + nome + " em " + str(ano))
print(f"Ola {nome} em {ano}")  # <--
print("Ola {} em {}".format(nome, ano))  # <-- metodo pré f-string

print("-------------------------")

n1 = 10
n2 = 10.0

soma = n1 + n2
print(soma)

sub = n1 - n2
print(sub)

multip = n1 * n2
print(multip)

divi = n1 / n2
print(divi)

print(type(n1))
print(type(n2))
print("--------------------")

n1 = 10
n2 = 10

soma = n1 + n2
print(soma)

n1 = 10
n2 = 10

sub = n1 - n2
print(sub)

n1 = 10.5
n2 = 10.5

soma = n1 + n2
print(soma)

n1 = 10
n2 = 10
multip = n1 * n2
print(multip)

n1 = 20
n2 = 10

divi = n1 / n2
print(divi)

# condições


# if - elif - else

# match - case


# tendo o codigo:

idade = 10

# verifique se a pessoa e adulta ou não (um adulto tem mais de 18 anos)


# verifique se a pessoa e
#   - adulta (um adulto tem mais de 18 anos)
#   - adolescente (12 aos 18 anos)
#   - criança (menos de 12 anos)


# Crie uma app que receba 2 notas


# se as duas notas forem positivas (maior ou igual a 10) o aluno está aprovado
# se apenas uma das notas for positiva pode fazer recuperação
# se nenhuma das duas notas for positiva está reprovado


# Crie um menu com 3 opções:
#  na opt 1 mostre a msg "ola Mundo"
#  na opt 2 mostre a msg "Bom dia"
#  na opt 3 mostre a msg "Boa noite"
#  se a opt for invalida indique que a opt é invalida
#


# loops


# Faça uma app que mostre o resultado da tabuada.
# deve pedir o num da tabuada


# adapte o seu memu para estar sempre a pedir uma opção até ser inserido o valor 0 (sair)


# for vs while


"""

listas
dict
set

funções

"""

lst = ["elm1", "elm2", "elm3", "elm1"]
print(lst)
lst.append("elm4")
print(lst)
lst.append(30)
print(lst)
lst.remove("elm4")
print(lst)
lst.pop()
print(lst)

cnt = lst.count("elm1")
print(cnt)

print(len(lst))
print(lst.__len__())

nome = "JoãoC"

print(nome.__len__())

"""

lst:
    add
    remover
    contar
    iterar 
"""

print(lst[0])

# crie um programa que peça ao utilizador 5 nomes, mostre a lista dos nomes pedidos


# crie um programa que peça ao utilizador nomes até ser inserido "0",
# e mostre os nomes pedidos, deve mostrar um nome por linha


for elm in lst.__reversed__():
    print(elm)

# dict


aluno = {
    "nome": "Carlos",
    "media": 12,
    "estado": "Aprovado"
}

print(aluno["nome"])

aluno["escola"] = "ATEC"

print(aluno)

aluno["escola"] = "IEFP"

print(aluno)

# aluno.pop("escola")

print(aluno)

# aluno.popitem()
print(aluno)

for keys in aluno:
    print(keys)
print("-----------------------")
for keys in aluno.keys():
    print(keys)

print("-----------------------")
for values in aluno.values():
    print(values)

print("-----------------------")
for keys, values in aluno.items():
    print(f"k:{keys:10} v:{values}")

print("-----------------------")


# Função
def nome():
    print("antes")
    pass  # <- cria um bloco vazio
    print("depois")


def soma(val1, val2):
    return val1 + val2


res = soma(12, 12)

print(res)


def soma2(val1: int, val2: int) -> int:
    return val1 + val2


res = soma2(121, 12)
print(res)


def demo(num1: int, num2):
    pass
