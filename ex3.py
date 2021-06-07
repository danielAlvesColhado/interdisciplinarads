# Ler o nome e a data de nascimento de três pessoas

#Dentre os três nomes, Selecionar e listar o mais velho e informar a classificação segundo OMS.
# estágios: Meia - idade: 45 a 59 anos;
# Idoso(a): 60 a 74 anos;
# Ancião: 75 a 90 anos;
# Velhice extrema: 90 anos em diante.
#Transforma o código de leitura de três nomes em um código de leitura até a digitação da palavra “FIM” ou “fim”


from datetime import date


def pedir_nome(index, pessoas):
    pessoa_nome = input(f'Pessoa{index + 1} Qual seu nome? ')
    pedir_data(pessoa_nome, pessoas)


def pedir_data(pessoa_nome, pessoas):
    nascimento_dia = int(input(f'{pessoa_nome} Qual dia você nasceu? "informe 00" '))
    nascimento_mes = int(input(f'{pessoa_nome} Qual mes você nasceu? "informe 00" '))
    nascimento_ano = int(input(f'{pessoa_nome} Qual ano você nasceu? "informe 0000"'))
    idade = calcular_idade(nascimento_ano, nascimento_mes, nascimento_dia)
    adicionar_pessoas_na_lista_segundo_classificacao(pessoa_nome, idade, pessoas)


def calcular_idade(nascimento_ano, nascimento_mes, nascimento_dia):
    data_atual = date.today()
    return data_atual.year - nascimento_ano - ((data_atual.month, data_atual.day) < (nascimento_mes, nascimento_dia))


def adicionar_pessoas_na_lista_segundo_classificacao(pessoa_nome, idade, pessoas):
    if idade in range(45, 60):
        pessoas.append([pessoa_nome, idade, 'Meia idade'])
    elif idade in range(60, 75):
        pessoas.append([pessoa_nome, idade, 'IDOSO'])
    elif idade in range(75, 90):
        pessoas.append([pessoa_nome, idade, 'Ancião'])
    elif idade >= 90:
        pessoas.append([pessoa_nome, idade, 'Velhice extrema'])
    else:
        pessoas.append([pessoa_nome, idade, 'jovem'])


def verificar_quem_e_mais_velho(pessoas):
    pessoa_mais_velha = []
    pessoa_mais_velha.append(pessoas[0])
    for i in range(1, len(pessoas)):
        if pessoas[i][1] > pessoa_mais_velha[0][1]:
            pessoa_mais_velha[0] = pessoas[i]
    return pessoa_mais_velha[0]



def rodar_programa():
    pessoas = []
    index_pessoa = 0
    continuar_cadastrando = True
    while continuar_cadastrando:
        pedir_nome(index_pessoa, pessoas)
        index_pessoa += 1
        quer_continuar = input('quer continuar? digite SIM ou FIM para parar')
        if quer_continuar.upper() == 'FIM':
            continuar_cadastrando = False



    for j in range(0, len(pessoas)):
        print(f'Pessoa{j + 1}: {pessoas[j][0]}, idade: {pessoas[j][1]}, classificação: {pessoas[j][2]} ')

    print(f'A pessoa mais velha é {verificar_quem_e_mais_velho(pessoas)[0]}, idade: {verificar_quem_e_mais_velho(pessoas)[1]}, classificação: {verificar_quem_e_mais_velho(pessoas)[2]} ')


rodar_programa()