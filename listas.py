animais = ["Cachorro","Gato","Ovelha"]
print(type(animais))#exibindo o tipo da variável

print(animais)

 #Exibindo todos os itens da lista
print("~"*200)
for itens in animais:
    print(itens)

#1ª Etapa: Atualizar dados
print("~"*200)
animais[0]="Coelho"
print(animais)

#2ª Etapa: Inserir dados
print("~"*200)
#Forma 1 - Usando append
animais.append("Cavalo")#irá inserir um novo item no final dda lista
print(animais)

#2ª Forma - Usando Insert
animais.insert(1,"Pássaro")# o insert precisa de 2 valors, o 1ª será o índicie que desejo inserir o valor. O 2ª é o conteúdo que quero inserir na lista
print(animais)

#3ª Etapa: Excluir dados
print("~"*200)
#Forma 1 - usando pop()
animais.pop()#Remove o último item da lista
print(animais)

#Forma 2 - usando pop() com índice
animais.pop(0)# Aqui iremos escolher qual índice dalista será  excluído 

#Forma 3 - usando remove
print("~"*200)
animais.remove("Ovelha")#Irá remover o item pelo seu conteúdo
print(animais)