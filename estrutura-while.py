#1ª forma de utilizar o while - semelhante ao FOR

contador = 1

while contador <= 5:
    contador = contador + 1
    print(contador - 1)

#2ª forma de utilizar o while - loop condicional normal
print("~"*500)
valor = 0

while valor >=0:
    valor = int(input("Informe uma valor qualquer (digite um valor negativo para terminar: )"))
    print(f"Você digitou {valor}")

print ("~"*500)

#3ª forma de utilizar o while - semelhante a estrutura faça..enquanto

while  True:
    senha = input("Informe a sua senha: ")
    if senha == "123":
        print("Senha correta")
        break
    else:
        print("Senha errada cuzão, mete o pé zé ruela")