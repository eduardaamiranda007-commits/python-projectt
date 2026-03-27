# 1- OR
idade = int(input("Digite sua idade: "))
autorizacao = input("Possui autorização dos responsáveis? (sim/não): ")
if idade >= 18 or autorizacao == "sim":
    print("Entrada permitida!")
else:
    print("Entrada não permitida!")


# 2- OR
nota = float(input("Digite a nota final:"))
frequencia = float(input("Digite a frequência (em %): "))

if nota >= 7 or frequencia >= 75:
    print("Aluno Aprovado!")
else:
    print("Aluno Reprovado!")    


# 3- AND 
usuario = input("digite o nome de usuario")
senha = input("Digite a senha: ")
if usuario == "admin" and senha == "1234":
    print("acesso permitido!")
else:
    print("acesso negado!")


# 4- AND
salario = float(input("Digite o salário: "))
tempo = int(input("Digite o tempo de empresa (em anos): "))
if salario < 3000 and tempo >= 2:
    print("Bônus concedido!")
else:
    print("Bônus não concedido.")
   



