from funcoes import TelaAbertura,principaisCausas,SugereMinimizacaoSintomas,AtualizaMatrizScoreRisco,CalculaPercentual,ImprimeMatrizScoreRisco
from dados_coletados import lista_respostas

TelaAbertura()

matriz = AtualizaMatrizScoreRisco(lista_respostas)

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= MENU -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("1 - Ação para minimização dos efeitos")
print("2 - Score e nível de risco de uma pessoa")
print("3 - Impressão de todas as pessoas")
print("4 - Percentual de pessoas com risco baixo")
print("5 - Percentual de pessoas com risco moderado")
print("6 - Percentual de pessoas com risco alto")
print("7 - Encerrar o programa")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(" "*50)

       
opcao = 0

while True:

    opcao = int(input("Insira a opção desejada: "))
    while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6 and opcao != 7:
        print("Opção invalida!!!")
        opcao = int(input("Insira a opção desejada: "))
    
    if opcao == 1:
        principaisCausas()
        escolha = int(input("Sobre qual desejar saber dicas de como lidar?(0 a 9):  "))
        while escolha < 0 and escolha > 9:
            print("numero invalido!!")
            escolha = int(input("Sobre qual desejar saber dicas de como lidar?(0 a 9):  "))
        print(" "*40)
        print("=-"*60)
        print(" "*40)
        print(SugereMinimizacaoSintomas(escolha))
        print(" "*40)
        print("=-"*60)
        print(" "*40)
    
    elif opcao == 2:
        nome = input("Digite o nome da pessoa (ex: Pessoa_10): ").strip().capitalize()
        encontrou = False
        for pessoa in matriz[1:]:
            if pessoa[0] == nome:
                print(" "*40)
                print("=-"*30)
                print(f"{pessoa[0]} tem Score = {pessoa[-2]} e está em {pessoa[-1]}")
                print("=-"*30)
                encontrou = True
                break
        if not encontrou:
            print("Pessoa não encontrada. Verifique o nome (ex: Pessoa_1 a Pessoa_120).")
    
    elif opcao == 3:
        ImprimeMatrizScoreRisco(matriz)
    
    elif opcao == 4:
        print(" "*40)
        print("=-=-=-=-=-=-=-=- Percentuais -=-=-=-=-=-=-=-=-=")
        print(" "*40)
        print(f"Total de pessoas na faixa Baixo risco: {CalculaPercentual(matriz, 'Baixo risco'):.1f}%")
        print(" "*40)
    elif opcao == 5:
        print(" "*40)
        print("=-=-=-=-=-=-=-=- Percentuais -=-=-=-=-=-=-=-=-=")
        print(" "*40)
        print(f"Total de pessoas na faixa Moderado risco: {CalculaPercentual(matriz, 'Moderado risco'):.1f}%")
        print(" "*40)
    elif opcao == 6:
        print(" "*40)
        print("=-=-=-=-=-=-=-=- Percentuais -=-=-=-=-=-=-=-=-=")
        print(" "*40)
        print(f"Total de pessoas na faixa Alto risco: {CalculaPercentual(matriz, 'Alto risco'):.1f}%")
        print(" "*40)
    
    elif opcao == 7:
        print("Programa encerrado...")
        break
    