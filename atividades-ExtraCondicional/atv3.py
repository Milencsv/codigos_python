idade = int(input("Digite a sua idade: "))
if idade < 12:
 print("Você é uma criança")
elif idade >= 12 and idade < 18:
    print("Você é adolescente")
elif idade >= 18 and idade < 60:
   print("Você é adulto")
elif idade >= 60:
   print("Você é idoso")