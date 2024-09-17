objetos = ("Lápis","Borracha","Caderno")
print(objetos[1]) #Irei exibir o item na posição 1, ou seja segunda posição, uma vez que toda coleção começa na posição zero.

print(type(objetos))#irá mostrar o tipo da variável

print(objetos)#  exibe todos os itens de uma vez só

print("~"*90)
for item in range(0,3):
    print(objetos[item], end=", ")# exibindo os itens da tupla

# Exibindo todos os itens da tupla se a função range
print("")
print("~"*90)

for elementos in objetos:
    print(elementos)

#Iremos tentar alertar o conteúdo da tupla
