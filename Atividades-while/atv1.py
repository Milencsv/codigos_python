while True:
    valor = int(input("Digite um valor: "))
    if valor > 100:
        print("O limite foi excedido")

    elif valor > 5 and valor <10:
        valor = valor ** 3
        print(f"O resultado é {valor}")

    elif valor> 10:
        valor = valor**2 
        print(f"O resultado é {valor}")

    elif valor<= 0:
       print("Programa encerrado")
    break
    
       
    