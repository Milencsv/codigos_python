compra = float(input("Informe o valor da compra: R$"))
parcelas = int(input("Informe o número de parcelas: "))

if parcelas < 1 or parcelas > 24:
    print("Número de parcelas inválido. Deve ser entre 1 e 24.")

else:
    juros = 0

if parcelas > 12:
    juros = compra * 0.015
    adicional = (parcelas - 12) * 6

    valor_total = compra + juros + adicional
    valor_parcela = valor_total / parcelas
    print("Valor total a ser pago: R${:.2f}".format(valor_total))
    print("Valor da parcela: R${:.2f}".format(valor_parcela))
    