salário = float(input("Digite o salário do funcionário: "))

if salário <= 1900:
    imposto = 0

elif salário >= 1901 and salário <= 2800:
    imposto = salário * 0.075

elif salário >= 2801 and salário <= 3700:
    imposto = salário * 0.15

elif salário > 3700:
    imposto = salário * 0.225

print(imposto)
