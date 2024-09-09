num = int(input("Digite um número: "))
print (f"Divisores de {num} são: ")
for i in range (1, num + 1):
    if num % i == 0:
        print ('{}'.format(i), end=' ')