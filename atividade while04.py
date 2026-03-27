# 4
numero = int(input("Digite um número para contagem: "))
while (numero != 0 ):
    decompor = int(numero / 10)
    contador = contador+1
    numero = decompor
print(f"Onúmero que você digitou tem {contador} digitos !!!")