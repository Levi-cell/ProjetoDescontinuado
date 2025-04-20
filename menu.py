from manipulandoBanco import adicionaFaturamento as af, adicionaCusto as ac
from tratandoErros import tratamento_de_retorno, trata_entrada_de_opcao
from manipulandoDatas import funcoesResultandes as fr
from conexaoBanco import cursor, conexao
import datetime


iniciar = (input("Olá casal Lemos, Digite qualquer coisa para iniciar o programa de Gerenciamento"
                 " Financeiro do Caldeirão Nordestino: \n"))

data_atual = datetime.date.today()
data_inicial_proxima_semana, data_final_proxima_semana = fr.calcula_proximo_periodo_semanal()
parou = False
while not parou:

    print(f"1 - Consultar informações. \n"
          f"2 - Registrar um faturamento \n"
          f"3 - Registrar um custo. \n"
          f"4 - Adicionar um copo. \n"
          f"5 - Alterar um copo. \n")

    menu = input("O que deseja fazer? digite uma opção dentre as acima: \n ")

    menu = trata_entrada_de_opcao(menu)

    if menu == "1":

        primeira_dia_semana, ultimo_dia_semana = fr.calcula_ultimo_periodo_semanal()
        primeiro_dia_mes, ultimo_dia_mes = fr.calcula_ultimo_periodo_mensal()
        primeiro_dia_ano, ultimo_dia_ano = fr.ultimo_periodo_anual()

        opcao = input(f" 1 - Consultar informações da semana passada: {primeira_dia_semana} até {ultimo_dia_semana}. \n"
                      f" 2 - Consultar informações do mês passado: {primeiro_dia_mes} até {ultimo_dia_mes}. \n"
                      f" 3 - Consultar informações do ano passado:  {primeiro_dia_ano} até {ultimo_dia_ano}. \n"
                      f" 4 - Consultar todos os registros da empresa. \n"
                      f" 5 - Consultar o faturamento, custo e lucro total da empresa. \n")

        opcao = trata_entrada_de_opcao(opcao)

        if opcao == "1":

            # Espaço para a função que mostrará o total de lucro, custo, e faturamento da última semana.

            nova_opcao = input("Deseja visualizar o registro de cada dia dessa semana? Digite ""sim"" ou pressione "
                               "qualquer tecla para voltar ao menu principal:")

            if nova_opcao == "sim":

                # Espaço para a função que irá mostrar o lucro, custo e faturamento de cada dia da semana.

                parou = tratamento_de_retorno(parou)

        elif opcao == "2":

            # Espaço para a função que mostrará o total de lucro, custo, e faturamento do último mês.

            nova_opcao = input(f"Deseja visualizar o registro de cada dia desse mês? Digite sim ou pressione "
                               "qualquer tecla para voltar ao menu principal:")

            if nova_opcao == "sim":
                # Espaço para a função que mostrará o lucro, custo, e faturamento de cada dia desse último mês.

                parou = tratamento_de_retorno(parou)

        elif opcao == "3":

            # Espaço para a função que mostrará o total de lucro, custo, e faturamento do ano passado.

            nova_opcao = input(f"Deseja visualizar o registro de cada mês desse ano? Digite sim ou pressione "
                               "qualquer tecla para voltar ao menu principal:")

            if nova_opcao == "sim":
                # Espaço para a função que mostrará o lucro, custo, e faturamento de cada mês do ano passado.

                parou = tratamento_de_retorno(parou)

        elif opcao == "4":

            # espaço para a função que mostrará todos os registro da empresa

            parou = tratamento_de_retorno(parou)

        elif opcao == "5":

            # espaço para a função que mostrará o total de cada registro da empresa

            parou = tratamento_de_retorno(parou)
        else:

            opcao_invalida = input("Você digitou uma opção inválida, pressione qualquer tecla para voltar ao "
                                   "menu principal")

    elif menu == "2":

        opcao = input(f" 1 - Registrar faturamento do dia atual:{data_atual} \n"
                      f" 2 - Registrar faturamento de uma data passada\n")

        if opcao == "1":

            af.adiciona_faturamento_diario_atual()

            parou = tratamento_de_retorno(parou)

        elif opcao == "2":

            # Espaço para a função que irá adicionar um faturamento em uma data determinada
            parou = tratamento_de_retorno(parou)

        else:

            opcao_invalida = input("Você digitou uma opção inválida, pressione qualquer tecla para volta ao "
                                   "menu principal")

    elif menu == "3":

        opcao = input(f" 1 - Registrar custo dos materiais para a próxima semana:"
                      f" {data_inicial_proxima_semana} até {data_final_proxima_semana}.\n"
                      f" 2 - Registrar custo com entregas no dia atual:{data_atual}\n"
                      f" 3 - Registrar custo de uma data passada\n")

        if opcao == "1":

            ac.adiciona_custo_semanal()

            parou = tratamento_de_retorno(parou)

        elif opcao == "2":

            # espaço para função que irá registrar o custo das entregas no dia

            parou = tratamento_de_retorno(parou)

        elif opcao == "3":

            # espaço para função que irá registrar o custo de uma data determinada no passado.

            parou = tratamento_de_retorno(parou)

        else:

            opcao_invalida = input("Você digitou uma opção inválida, pressione qualquer tecla para volta ao "
                                   "menu principal")
    elif menu == "4":

        # Espaço para a função que irá adicionar um copo

        parou = tratamento_de_retorno(parou)

    elif menu == "5":

        # Espaço para a função que irá alterar um copo

        parou = tratamento_de_retorno(parou)

    else:

        opcao_invalida = input("Você digitou uma opção inválida, pressione qualquer tecla para volta ao "
                               "menu principal")

cursor.close()
conexao.close()
