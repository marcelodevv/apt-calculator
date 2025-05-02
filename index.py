#IMPORTAÇÕES
import os

# CORES
Verm="\033[1;31m"
Verde="\033[1;32m"
Amar="\033[1;33m"
Azul="\033[1;34m"
Reset="\033[0;m"

#TITULOS

TITULOB= '''
██████╗ ███████╗███╗   ███╗      ██╗   ██╗██╗███╗   ██╗██████╗  ██████╗ ██╗
██╔══██╗██╔════╝████╗ ████║      ██║   ██║██║████╗  ██║██╔══██╗██╔═══██╗██║
██████╔╝█████╗  ██╔████╔██║█████╗██║   ██║██║██╔██╗ ██║██║  ██║██║   ██║██║
██╔══██╗██╔══╝  ██║╚██╔╝██║╚════╝╚██╗ ██╔╝██║██║╚██╗██║██║  ██║██║   ██║╚═╝
██████╔╝███████╗██║ ╚═╝ ██║       ╚████╔╝ ██║██║ ╚████║██████╔╝╚██████╔╝██╗
╚═════╝ ╚══════╝╚═╝     ╚═╝        ╚═══╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝                                                                      
'''

TITULOTABELA= '''
████████╗ █████╗ ██████╗ ███████╗██╗      █████╗     ██████╗ ███████╗    ██╗   ██╗ █████╗ ██╗      ██████╗ ██████╗ ███████╗███████╗
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║     ██╔══██╗    ██╔══██╗██╔════╝    ██║   ██║██╔══██╗██║     ██╔═══██╗██╔══██╗██╔════╝██╔════╝
   ██║   ███████║██████╔╝█████╗  ██║     ███████║    ██║  ██║█████╗      ██║   ██║███████║██║     ██║   ██║██████╔╝█████╗  ███████╗
   ██║   ██╔══██║██╔══██╗██╔══╝  ██║     ██╔══██║    ██║  ██║██╔══╝      ╚██╗ ██╔╝██╔══██║██║     ██║   ██║██╔══██╗██╔══╝  ╚════██║
   ██║   ██║  ██║██████╔╝███████╗███████╗██║  ██║    ██████╔╝███████╗     ╚████╔╝ ██║  ██║███████╗╚██████╔╝██║  ██║███████╗███████║
   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝      ╚═══╝  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
                                       ______________________________________________         
                                       | Pessoas: 1 | TIPO 1: 20,00 | TIPO 2: 25,00 |
                                       | Pessoas: 2 | TIPO 1: 28,00 | TIPO 2: 34,00 |
                                       | Pessoas: 3 | TIPO 1: 35,00 | TIPO 2: 42,00 |
                                       | Pessoas: 4 | TIPO 1: 42,00 | TIPO 2: 50,00 |
                                       | Pessoas: 5 | TIPO 1: 48,00 | TIPO 2: 57,00 |
                                       | Pessoas: 6 | TIPO 1: 53,00 | TIPO 2: 63,00 |
                                       |____________________________________________|
'''

ERRO= '''
███████╗██████╗ ██████╗  ██████╗ 
██╔════╝██╔══██╗██╔══██╗██╔═══██╗
█████╗  ██████╔╝██████╔╝██║   ██║
██╔══╝  ██╔══██╗██╔══██╗██║   ██║
███████╗██║  ██║██║  ██║╚██████╔╝
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ 
'''

TOTAL='''
▄▄▄███▄▄    ██╗   ██╗ █████╗ ██╗      ██████╗ ██████╗    ████████╗ ██████╗ ████████╗ █████╗ ██╗         ▄▄███▄▄·
██╔════╝    ██║   ██║██╔══██╗██║     ██╔═══██╗██╔══██╗   ╚══██╔══╝██╔═══██╗╚══██╔══╝██╔══██╗██║         ██╔════╝
███████╗    ██║   ██║███████║██║     ██║   ██║██████╔╝█████╗██║   ██║   ██║   ██║   ███████║██║         ███████╗
╚════██║    ╚██╗ ██╔╝██╔══██║██║     ██║   ██║██╔══██╗╚════╝██║   ██║   ██║   ██║   ██╔══██║██║         ╚════██║
███████║     ╚████╔╝ ██║  ██║███████╗╚██████╔╝██║  ██║      ██║   ╚██████╔╝   ██║   ██║  ██║███████╗    ███████║
╚═▀▀▀══╝      ╚═══╝  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝      ╚═╝    ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═▀▀▀══╝
'''

# ENTRADA DE DADOS (INFORMAÇÕES DA RESERVA)

print(Azul, "-"*75)
print(TITULOB)
print("-"*75, Reset)

NomeCliente = input("Digite seu nome: ")
os.system('cls')

print(Verde,"-"*130)
print(TITULOTABELA)
print("-"*130, Reset)

while True:
    while True:
        try:
            PessoasPorApartamento = int(input("Você gostaria de fazer o orçamento para quantas pessoas? (1 a 6): "))
            if not (1 <= PessoasPorApartamento <= 6):
                print(Verm, "ERRO: Digite uma quantidade de pessoas válida de (1 a 6) para o apartamento.", Reset)
                continue 
            break
        except ValueError:
            print(Verm, "ERRO: Por favor, digite um valor inteiro válido para a quantidade de pessoas.", Reset)


    while True:
        try:
            TipoDeApartamento = int(input("Digite o tipo de apartamento desejado? (1 ou 2): "))
            if TipoDeApartamento not in [1, 2]:
                print(Verm, "ERRO: Digite um tipo de apartamento válido (1 ou 2)", Reset)
                continue 
            break 
        except ValueError:
            print(Verm, "ERRO: Por favor, digite um valor inteiro válido para o tipo de apartamento", Reset)
   
   
    while True:
        try:
            QuantidadeDeDiarias = int(input("Digite a quantidade de diárias que você gostaria de alugar: "))
            if QuantidadeDeDiarias <1: 
                print(Verm, "ERRO: A quantidade de diárias deve ser no mínimo 1.", Reset)
                continue 
            break 
        except ValueError:
            print(Verm, "ERRO: Por favor, digite um valor inteiro válido para a quantidade de diárias", Reset)
            
#TABELA DE PREÇOS
    tabela_precos = {
    1: {1: 20, 2: 25},
    2: {1: 28, 2: 34},
    3: {1: 35, 2: 42},
    4: {1: 42, 2: 50},
    5: {1: 48, 2: 57},
    6: {1: 53, 2: 63},
}
    os.system('cls')

    #PROCESSAMENTO
    preco_diaria = tabela_precos[PessoasPorApartamento][TipoDeApartamento]
    valor_total = preco_diaria * QuantidadeDeDiarias
    valor_por_pessoa = round(valor_total / PessoasPorApartamento, 2)

    #SAÍDA
    print(Verde,TOTAL, Reset)
    print("-"*35)
    print("Olá", Verm, NomeCliente, Reset, "Muito obrigado por fazer seu orçamento conosco")
    print("Reserva para:",Azul, PessoasPorApartamento, "pessoa(s)", Reset)
    print(f"Tipo de reserva: ",Azul,f"TIPO {TipoDeApartamento} {Reset} {Verde}R$ {preco_diaria}",Reset)
    print("Orçamento para:",Azul, QuantidadeDeDiarias, "dia(s)",Reset)
    print("Valor total da reserva:", Verde, "R$", valor_total, Reset)
    print("Para cada pessoa:", Verde, "R$", valor_por_pessoa, Reset)
    print("-"*35)

    input(f"{Verm}Pressione Enter para finalizar.{Reset}")
    break