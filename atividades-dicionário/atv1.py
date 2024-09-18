notas_alunos = {}
# Loop para coletar a nota e o nome de 5 alunos
for contador in range (1,6):
   nome = input(f"Insira o nome do aluno {contador}: ")
   nota = float(input(f"Digite a nota do {nome}: "))
   notas_alunos[nome] = nota#aramazenando o nome e a nota dos alunos no dicionário

# Permite o usuário procurar pelo aluno e ver a sua nota
nome_aluno = input("Digite o nome do aluno para ver sua nota: ")   

# Vai verificar se o aluno está ou não no dicionário e irá exibir sua nota caso esteja
if nome_aluno in notas_alunos:
   print(f"A nota de {nome_aluno} é {notas_alunos[nome_aluno]}")
else:
   print("Aluno não foi encontrado")