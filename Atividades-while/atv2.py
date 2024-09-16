import  datetime

ano_atual = datetime.date.today().year
while True:
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        print('Você está apto a se inscrever no concurso!')
        break
    else:
        print('Você não está apto a se inscrever no concurso, pois ainda não tem 18 anos.')
        continue