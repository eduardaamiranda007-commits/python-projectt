# 3.
turmas = int(input("Digite a quantidade de turmas:   "))
qtd_alunos = int(input("Digite a quantidade de alunos:   "))
resto = qtd_alunos % turmas
media = qtd_alunos / turmas
                 
while media > 40:
    print("A quantidade de alunos por turma não pode ultrapassar 40. Tente novamente.")
    qtd_alunos = int(input("Digite a quantidade de alunos:   "))

print(f"A média de alunos por turma é: {media:.2f}")