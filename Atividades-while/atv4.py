print("Bem-vindo à Loja do Sr. Manoel")

valorT = 0.0
valorP = 0.0

while valorP != 0:
    valorP = float(input("Digite o preço do item. Para finalizar digite 0: "))
    
    if valorP < 0:
        print("Valor inválido! Digite um preço positivo.")
    elif valorP > 0:
        valorT += valorP

print(f"Total da compra: R$ {valorT:.2f}")

if valorT > 0:
    while True:
        dinheiro = float(input("Digite o valor em dinheiro do pagamento: "))
        
        if dinheiro >= valorT:
            troco = dinheiro - valorT
            print(f"Troco: R$ {troco:.2f} obrigado pela compra")
            break
        elif dinheiro < valorT:
            print("Vai dar calote na mãe >:( ")
        else:
            print(f"Valor insuficiente! Você precisa pagar pelo menos R$ {valorT:.2f}.")