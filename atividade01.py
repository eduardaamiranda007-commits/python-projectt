# Passo 1 e 2: entradada de dados
num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))

if num1 < num2:
    print("O menor número é:", num1)
else:
    print("O menor número é:", num2)



# passo 1
numero = int(input("Digite um número inteiro:"))

# Passo 2, 3 e 4
if numero % 2 == 0:
    print ("O Número é par")
else:
    print ("O Número é ímpar")



# Passo 1 
estado_civil = input("Digite seu estado civil(s,c,d,vi):").lower()
if estado_civil == 's':
    print("Solteiro(a)")
elif estado_civil == 'c':
    print("Casado(a)")
elif estado_civil == 'd':
    print("Divorciado(a)")
elif estado_civil == 'vi':
    print("Viúvo(a)")
else:
    print("Estado civil inválido")




