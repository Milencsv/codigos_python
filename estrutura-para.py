'''
Este código é uma representação do que acontece na maioria das linguagens de progrmação

for(contador=1; contador <=5 ; contador++)
'''

#1º forma de operação do for
for contador in range(1,6):
    print(contador)

print(200*"=")

#2º forma de operação do for
for contador in range(7,100,7):# o 3º parâmetro indica como os valores serão incrementados (alteração de valor)
    print(contador)

print(200*"=")

#3º forma de operação do for
for contador in range (1000,0,-7):
    print(contador,end=" ")#função end informa como os valores serão exibidos ao final, por ádrão é dado um enter(\n)