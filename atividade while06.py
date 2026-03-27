# 6.
numeros = 0 
qts_numeros = 0
numero = int(input("Digite um número para ser somado:" ))
numeros = numeros + numero

while (numeros != 0):
    qts_numeros = qts_numeros + 1
    print(f"Voce digitou {qts_numeros} números e a soma é {numeros}")
    break