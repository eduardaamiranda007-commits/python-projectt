nota1 = float(input("Digite o primeiro numero"))
nota2 = float(input("Digite o segundo numero"))
soma = nota1+nota2 
subtracao = nota1-nota2
divisao = nota1/nota2 
multiplicacao = nota1*nota2 
resto = nota1%nota2
expoente = nota1**nota2
opcao = int(input("===Digite o numero da opção desejada===\n" \
"1. Adição\n" 
"2. Subtração\n" \
"3. Divisão\n" \
"4. Multiplicação\n" \
"5. Restante da divisão\n" \
"6. Expoente"
"------"))


if (opcao == 1):
    nota1 = float(input("Digite o primeiro número: "))
    nota2 = float(input("Digite o segundo número: "))
    print(f"{nota1}+{nota2}={(nota1+nota2)}")
elif(opcao == 2):
    nota1 = float(input("Digite o primeiro número: "))
    nota2 = float(input("Digite o segundo número: "))
    print(f"{nota1}-{nota2}={(nota1-nota2)}")
elif(opcao == 3):
    nota1 = float(input("Digite o primeiro número: "))
    nota2 = float(input("Digite o segundo número: "))
    print(f"{nota1}/{nota2}={(nota1/nota2)}")
elif(opcao == 4):
    nota1 = float(input("Digite o primeiro número: "))
    nota2 = float(input("Digite o segundo número: "))
    print(f"{nota1}*{nota2}={(nota1*nota2)}")
elif(opcao == 5):
    nota1 = float(input("Digite o primeiro número: "))
    nota2 = float(input("Digite o segundo número: "))
    print(f"{nota1}%{nota2}={(nota1%nota2)}")
elif(opcao == 6):
    nota1 = float(input("Digite o primeiro número: "))
    nota2 = float(input("Digite o segundo número: "))
    print(f"{nota1}**{nota2}={(nota1**nota2)}")
else:
    print("Você digitou uma opção inválida!!!")





