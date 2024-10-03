#cmt

"""
cmt
varias
linhas

"""

#prt
print("Ola Mundo")


#var
nome = "Valor" # String
idade = 10 # max int em c ->  2,147,483,647, max int em Py -> não existe
nota = 10.9 # Flaot( 6 a 7) e Double (14)
aprovado = True #


print(nome)
nome = 10
print(nome)

soma = idade + 3
print(soma)


soma2 = nota + 2
print(soma2)

nome = "Valor"
soma3 = nome + " Foo"
print(soma3)


nome = "Valor"
# soma4 = nome + 2024
#print(soma4)

op5 = nome * 2
print(op5)

#print v2


nome = "Gonçalo"
ano = 2024

# "Ola Mundo, Gonçalo em 2024"

anoStr = str(ano) # converte para string

print("Ola Mundo, " + nome + " em " + str(ano))

print("Ola Mundo,", nome ,"em", str(ano))

print("Ola Mundo,", nome ,"em", ano)

print(f"Ola Mundo, {nome.upper()} em {ano}")



# -> % <-

op2 = 10 % 3
print(op2)

op2 = 12 % 3
print(op2)


op2 = 10 / 3
print(op2)

op2 = 10 // 3
print(op2)


# ler dados do teclado
nome2 = input("Digite seu nome: ")
print(f"ola, {nome2}")

print("--" * 10)
# Ifs


idade = 19
if idade > 18:
    print("adulto")
else:
    print("nao Adulto")

print("Fora do if")



idade = 10

if idade > 18:
    print("adulto")
elif idade > 11:
    print("jovem")
else:
    print("criança")


print("Faça um Programa que peça dois números e imprima a soma.")

val1 = input("valor1: ")
val2 = input("valor2: ")

soma = float(val1) + float(val2)

print(soma)

print("1 Faça um Programa que mostre a mensagem \"Alo mundo\" na tela.")


print("2 Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]")


print("Faça um Programa que peça dois números e imprima a soma. V2")

val1 = float(input("valor1: "))
val2 = float(input("valor2: "))

soma = val1 + val2

print(soma)


print("Faça um Programa que peça as 4 notas bimestrais e mostre a média.")