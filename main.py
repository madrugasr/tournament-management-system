"""
A organização da CBF precisa de um programa de gestão
para a construção do campeonato.

Author: Daniel Marques
"""
#Importando Rescursos.
from fileinput import close
import os
import random
import mysql.connector
from numpy import true_divide

#Conexão com Banco de Dados WorldCup
worldcup_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password = 'aaZe!9ae.hVsMGD'
)

print(worldcup_db)

def menu():
    """
    Função: Menu de Opções.
    """
    limpa_tela()

    print('\n\033[1;34;40mGestor de Campeonato\033[m')
    print('\n\033[4;32;40mBRASILEIRÃO\033[m')

    print('\n1. Introduzir Dados')
    print('2. Geração de Dados')
    print('3. Alterar Dados')
    print('4. Eliminar Dados')
    print('5. Consultar')
    print('6. Pesquisar')
    print('7. Total de Expectadores')
    print('8. Total de Expectadores por Time')
    print('9. Limpar Tela')
    print('10. Guardar dados do Ficheiro')
    print('11. Carregar dados do Ficheiro')
    print('\033[1;36;40m12. Sobre Nós!\033[m \n')
    print('\033[31m13. Sair\033[m \n')

    linha(20)

    escolha_opcao = int(input('\nDigite sua Opção: '))
    #Validação das Opções
    while escolha_opcao < 1 and escolha_opcao > 13:
        print('\n\033[31mResposta Incorreta.\033[m')
        escolha_opcao = int(input('\nDigite sua Opção: '))
    
        
    #Atribuição de Atitutes
    if escolha_opcao == 1:
        inserir_dados()

    elif escolha_opcao == 2:
        gerador_dados_aleatorios()
    
    elif escolha_opcao == 4:
        eliminar_dados()

    elif escolha_opcao == 9:
        limpa_tela_menu()

    elif escolha_opcao == 10:
        guardar_ficheiro()
    
    elif escolha_opcao == 11:
        carregar_ficheiro()
    
    elif escolha_opcao == 12:
        sobre()
    
    elif escolha_opcao == 13:
        sair()

def inserir_dados():
    """
    Função: Inserir dados no Sistema.
    """
    limpa_tela()

    lista_jogos = [-1]

    print('\n\033[1;34mINSIRA os DADOS\033[m')
    
    while True:
        jogo = input('\nJogo: ')
        while jogo.isnumeric() == False:
            print('\n\033[30;41mDigite o número do Jogo corretamente.\033[m')
            jogo = input('\nJogo: ')
        
        while len(lista_jogos) -1 == jogo:
           print(f'\n\033[30;41m{jogo} jogo já existe.\033[m')
           jogo = input('\nJogo: ')

        grupo = input('Grupo: ')
        while any(chr.isdigit() for chr in grupo):
            print('\n\033[30;41mDigite o nome do Grupo corretamente.\033[m')
            grupo = input('\nGrupo: ')

        selecao_1 = input('Seleção 1: ')
        while any(chr.isdigit() for chr in selecao_1):
            print('\n\033[30;41mDigite o nome da Seleção corretamente.\033[m')
            selecao_1 = input('\nSeleção 1: ')

        selecao_2 = input('Seleção 2: ')
        while any(chr.isdigit() for chr in selecao_2):
            print('\n\033[30;41mDigite o nome da Seleção corretamente.\033[m')
            selecao_2 = input('\nSeleção 2: ')

        estadio = input('Estádio: ')
        while any(chr.isdigit() for chr in estadio):
            print('\n\033[30;41mDigite o nome do Estádio corretamente.\033[m')
            estadio = input('\nEstádio: ')

        espectadores = input('Espectadores: ')
        while espectadores.isnumeric() == False:
            print('\n\033[30;41mDigite o númer de Espectadores corretamente.\033[m')
            espectadores = input('\nEspectadores: ')
        
        registro_jogos = [jogo, grupo, selecao_1, selecao_2, estadio, espectadores]
        lista_jogos.append(registro_jogos)

        print(), linha(20)

        print('\n1. Menu Inicial')
        print('2. Continuar')
        op = int(input('\n' ))
        while op != 1 and op != 2:
            print('\nOpção Incorreta.')
            print('\n1. Menu Inicial')
            print('2. Continuar')
            op = int(input('\n' ))
        if op == 1:
            limpa_tela(), menu()
        if op == 's':
            close()


def gerador_dados_aleatorios():
    """
    Função: Gerador de Dados Aleatorios.
    """
    limpa_tela()

    while True:
        print('\n\033[1;34mGERAÇÃO DE DADOS ALEATORIOS\033[m')

        #Jogos
        jogos_ale = random.randint(1, 195)
        print('\nJogo:', jogos_ale)
        
        #Grupo
        letras = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        grupo_ale = random.choice(letras)
        print('Grupo:', grupo_ale)

        #Seleções
        ficheiro_paises = open("database/lists/reading/coutries.csv","r", encoding="utf8")
        lista_paises = []
        
        for linha in ficheiro_paises.readlines():
            lista_paises.append(linha.strip())
        ficheiro_paises.close()
        
        #Seleção 1
        selecao1_ale = random.choice(lista_paises)
        print('Seleção 1:', selecao1_ale)

        #Seleção 2
        selecao2_ale = random.choice(lista_paises)
        print('Seleção 2:', selecao2_ale)

        #Estádio
        ficheiro_stadiums = open('database/lists/reading/stages.csv','r', encoding='utf8')
        lista_estadios = []

        for linha in ficheiro_stadiums.readlines():
            lista_estadios.append(linha.strip())
        ficheiro_stadiums.close()

        estadios_ale = random.choice(lista_estadios)
        print('Estádio:', estadios_ale)

        #Espectadores
        espectadores_ale = random.randint(35000, 100000)
        print('Espectadores:', espectadores_ale)
    
        registro_dados_ale = [jogos_ale, grupo_ale, selecao1_ale, selecao2_ale, estadios_ale, espectadores_ale]
        print()
        print(registro_dados_ale)

        op_c = input('\nContinuar gerando Dados Aleatórios: [S/n] ')
        while op_c != 'S' and op_c != 'n':
            print('\nOpção Incorreta.')
            op_c = input('\nContinuar gerar Dados Aleatórios: [S/n] ')
        
        if op_c == 'n':
            #Guardar Dados Aleatórios
            op_gd = input('\nGuardar os Dados: [S/n] ')
            while op_gd != 'S' and op_gd != 'n':
                print('\nOpção Incorreta.')
                op_gd = input('\nGuardar os Dados: [S/n] ')
            
            if op_gd == 'S':
                salvar_dados = open("database/lists/storage/random-game-data.csv","w+")
                #salvar_dados.write('Jogo | Grupo | Seleção 3 | Seleção 2 | Estádio | Espectadores \n')

                for item in registro_dados_ale:
                    salvar_dados.writelines(item)
                salvar_dados.close()
            else:
                limpa_tela_menu()



def eliminar_dados():
    """
    Função: Eliminar dados do Sistema.
    """
    global lista_jogos

    print('Digite que jogo quer digitar.')

    
def linha(vezes):
    """
    Função: Linha.
    """    
    print('\033[1;33m==\033[m' * vezes)


def limpa_tela_menu():
    """
    Função: Limpar a tela e retorna a função Menu.
    """
    if os.name == 'nt':
        os.system('cls')
        menu()
    else:
        os.system('clear')
        menu()

def limpa_tela():
    """
    Função: Limpar a Tela.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def sair():
    """
    Função: Sair."
    """
    limpa_tela(), close()

def guardar_ficheiro():
    """
    Função: Salvar Ficheiro.
    """




def carregar_ficheiro():
    """
    Função: Carregar Ficheiro.
    """



def sobre():
    """
    Função: Sobre o Programa.
    """
    limpa_tela()
    print("""
    \033[34mSobre Nós!\033[m\n
    Este programa foi desenvolvido a pedido da FIFA (Federação Internacional de Futebol),
    para atender as necessidades de Gestão dos Campeonatos Mundiais da Copa do Mundo.
    
    \033[35mAuthor e Desenvolvedor:\033[m Daniel Marques.\n""")

    linha(60) 

    opcao = input('\nMenu Inicial? [S/n] ')
    #Validação das Opções
    while opcao != 'S' and opcao != 'n':
        print('\n\033[31mResposta Incorreta.\033[m')
        opcao = input('\nMenu Inicial? [S/n] ')
    
    if opcao == 'S':
        limpa_tela(), menu()
    elif opcao == 'n':
        limpa_tela(), sair()
                    
menu()