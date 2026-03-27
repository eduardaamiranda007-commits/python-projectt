# Solicitar a quantidade de pessoas a serem cadastradas
qtd_pessoas = int(input("Digite a quantidade de pessoas a serem cadastradas: "))

# Inicializar contadores
entraram = 0
barradas = 0
entraram_sem_convite = 0

# Loop para cada pessoa
for i in range(qtd_pessoas):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    convite = int(input(f"A pessoa {i+1} possui convite? (1 para sim, 0 para não): "))
    
    if idade < 16:
        barradas += 1
    elif 16 <= idade <= 17:
        if convite == 1:
            entraram += 1
        else:
            barradas += 1
    else:  # idade >= 18
        entraram += 1
        if convite == 0:
            entraram_sem_convite += 1

# Informar os resultados
print(f"Quantidade de pessoas que entraram: {entraram}")
print(f"Quantidade de pessoas barradas: {barradas}")
print(f"Quantidade de pessoas que entraram sem convite: {entraram_sem_convite}")