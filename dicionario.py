#Criando um dicionário, é basicamente uma lista com índice textual

pessoa = {
    'Nome':'Pablo Emilio Escobar Gaviria',
    'Idade': 75,
    'Enderço':'Jalapão' 
}

print(pessoa)

print("--" *50)

#exibindo as chaves utilizando o comando keys() = indices
print(pessoa.keys())
print("--" *50)

#Exibindo os valores utilizando o comando values() = valores contidos nos indices
print(pessoa.values())
print("--" *50)

#exibindo tanto a chave quanto o valor
print(pessoa.items())
print("--" *50)

for chave , valor in pessoa.items():
    print(f"{chave} : {valor}")

#Realizando operações com dicionário
#Adicionando dados
#Forma 1
pessoa["Peso"] = 69
print(pessoa)

#Forma 2 - usando update()
pessoa.update({"Profissão" : "Paderiro"})

#Removendo dados do dicionário
#Forma 1 - pop()
pessoa.pop("Peso")
print(pessoa)

#Forma 2 - del()
del(pessoa["Enderço"])
print(pessoa)