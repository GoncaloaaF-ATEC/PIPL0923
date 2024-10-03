# Condições / Controlo de fluxo

# Boolean

'''

T e T -> T
T e F -> F
F e T -> F
F e F -> F


T ou T -> T
T ou F -> T
F ou T -> T
F ou F -> F


T xou T -> F
T xou F -> T
F xou T -> T
F xou F -> F

'''


ano = 20231

# if (se)
# else (se não)

if ano == 2024:
    print("ano = 2024")
else:
    print("Outro ano")

print("fora do if")

#Faça um Programa que peça dois números e imprima o maior deles.
num1 = int(input("val1: "))
num2 = int(input("val2: "))

if num1 > num2:
    print(num1)
else:
    print(num2)


print("--" * 10)

num = 5

# F e T -> F

# num = 5
#       F       and      T
if num % 2 == 0 and num % 5 == 0:
    print("par e div por 5")
else:
    print("impar ou nao div por 5")


'''
 == <- comparações
 
 =  <- atribuição 

'''



print("------" * 3)
num = 5
# F ou T -> T
# num = 5
#       F       and      T
if num % 2 == 0 or num % 5 == 0:
    print("par ou div por 5")
else:
    print("impar ou nao div por 5")



# else if (se não se)

print("------" * 3)

num = 10

if num % 2 == 0:
    print("par ou div por 5")
elif num % 5 == 0:
    print("div por 5")
else:
    print("impar nem nao div por 5")

# Faça um Programa que verifique se uma letra digitada é "F" ou "f" ou "M" ou "m".
# Conforme a letra escrever:
#   F - Feminino,
#   M - Masculino,
#   Genero Inválido.


print("------" * 3)

# switch (escolha)
num = 60

match num:
    case 0:
        print("o num é 0")

    case 1:
        print("o num é 1")

    case 5:
        print("o num é 5")

    case _:
        print("Outro valor")



memu = """######## Menu #########
# op1 ............. 1 #
# op2 ............. 2 #
# op3 ............. 3 #
#######################
"""

print(memu)
op = input("Selecione a op: ")


match op:
    case "1":
        print("op 1")

    case "2":
        print("op 2")

    case "3":
        print("op 3")

    case _:
        print("op Invalida")

# loop

# while (enquanto- faça)

count = 0
while op != "q":

    print(f"loop: {count}")

    op = input("Selecione a op while: ")

    count += 1

num = 0

while num < 10:
    print(num)
    num += 1

'''
num += 1 
num++

num = num + 1


num += 4
num = num + 4


num *= 4
num = num * 4


'''



# Range

range(0,10,2)

"""
range(a, b, c) 

a - LB

b - UB 

c -  step, se oculto c = 1


range(1, 5) 
1, 2, 3, 4

range(5) 
0, 1, 2, 3, 4

range(0, 11, 2) 
0, 2, 4, 6, 8, 10


"""
print("---" * 10)
for elm in range(0,11,2):
    print(elm)



print("---" * 10)

for elm in range(0,100):
    if elm % 2 == 0:
        continue

    print(elm)
    #if elm == 50:
    #    break

print("---" * 10)
print("---" * 10)

nomes = [
    "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Daniela","Igor", "Julia",
    "Karla", "Lucas", "Mariana", "Nicolas","Daniela","Olivia", "Pedro", "Quintino", "Rafael", "Sara", "Tatiana",
    "Ursula", "Vinicius", "Wagner", "Xavier","Daniela","Yasmin", "Daniela"
]

for nome in nomes:
    print(nome)

print("Fim do loop")

print(nomes.count("Daniela"))

print(nomes.__len__())
print(len(nomes))

print(nomes.__contains__("Sara"))
print(nomes.__contains__("Ana"))
print("Pedro" in nomes)








#for (par)




