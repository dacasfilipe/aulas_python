#Estrutura if elif else
# if é o se
# elif é o senão se
# else é o senão
idade = 18
if idade >= 18:
    print('é maior de idade.')
else:
    print('é menor de idade.')

#saber se a pessoa é:
# criança 0 a 12 anos
# adolescente 13 a 17
# adulto 18 pra cima
# idoso(a) de 60 em diante
if idade <= 12:
    print('é uma criança')
elif idade < 18: # idade >= 13 and idade <= 17
    print('é um adolescente')
elif idade < 60: # idade >= 18 and idade <= 59
    print('é um adulto')
# pode adicionar vários elif
else:
    print('um idoso(a)')

'''
Operadores lógicos 
E é and
OU é or
not para contrário
'''
salario = 10000
profissao = 'dev'
#Se a pessoa for 'dev' e tiver salário = 2000 imprimir é junior
#Se a pessoa for 'dev' e tiver salário entre 2000 e 7000 é pleno
#Se a pessoa for 'dev' e tiver salário maior que 7000 é senior
# imprima as mensagens conforme cada situação
if profissao == 'dev' and salario == 2000:
    print('é júnior')
elif profissao == 'dev' and salario > 2000 and salario <= 7000:
    print('é pleno')
elif profissao == 'dev' and salario > 7000:
    print('é senior')
else:
    print(f"a pessoa não é {profissao} ou ganha menos que 2000")

# Loops
# loop for
lojas = ['Americanas','Pernambucanas', 'Casas Bahia']
# a variável loja percorre item por item no vetor lojas
for loja in lojas:
  print(loja)
#contar de 1 até 10
#for i in range(1,11):       #conta de 1 até 10
for i in range(5): # for(i=0; i<5; i++) { código }
  print(i)

#Faça um for para contar de 1 até 50
for i in range(1,51): print(i)

i = 1
#Loop while ou enquanto
while i < 10:
    print(i) # 1
    #i= i + 1
    i+=1

esta_chovendo = False #True
while not esta_chovendo: #faz o while enquanto for verdadeiro
    chuva = input('Está chovendo? digite s para Sim e n para Não')
    if chuva == 's':
        print('Está chuvendo!')
        esta_chovendo = True
    elif chuva == 'n':
        print('Não Está chuvendo!')
        esta_chovendo = False
    else:
        print("Digite s ou n")
