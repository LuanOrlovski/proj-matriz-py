def TelaAbertura():
    print(" "*100)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- BURNOUT -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(" "*100)
    print(
        "Burnout é uma síndrome reconhecida pela Organização Mundial da Saúde (OMS), relacionada ao esgotamento físico e mental provocado por estresse crônico, especialmente no ambiente de estudo ou trabalho. \n"
        "Ele se manifesta por sintomas como exaustão constante, desmotivação, sensação de ineficácia e distanciamento emocional das atividades. \n"
        "Nos dias de hoje, com rotinas aceleradas, alta pressão por desempenho, falta de pausas e estímulos constantes por meio da tecnologia,\n"
        "cada vez mais estudantes e profissionais enfrentam sintomas de burnout, muitas vezes sem perceber.\n"
        "Neste contexto, esta matriz fornecida representa um conjunto simulado de respostas de 120 pessoas a perguntas ligadas a sintomas de Burnout.\n"
        "O objetivo ao manipular esses dados é obter estatísticas que ajudem a identificar padrões de risco, compreender como certos comportamentos se relacionam\n" 
        "com níveis de esgotamento e estimular decisões mais conscientes sobre bem-estar e saúde mental, especialmente em ambientes acadêmicos e profissionais.\n"
)
    print("-="*100)
    print(" "*100)

def principaisCausas():
    print(" "*20)
    print("=-"*20)
    print(" "*20)
    print("PRINCIPAIS CAUSAS DE BURNOUT")
    print(" "*20)
    print("1. Cansaço físico")
    print("2. Sem energia para tarefas")
    print("3. Falta de Motivação pelo trabalho")
    print("4. Procrastinação")
    print("5. Falta de Sentido no trabalho")
    print("6. Pensamentos negativos")
    print("7. Isolamento emocional")
    print("8. Isolamento social ")
    print("9. Falta de fazer algo prazeroso ")
    print(" "*20)
    print("=-"*20)
    print(" "*20)

def CalculaScoreIndividual(pessoa):
    # Pula o cabeçalho e o nome da pessoa
    respostas = pessoa[1:10]
    
    # Converte respostas para números
    valores = []
    for resposta in respostas:
        if resposta in ['Nunca', 'Sim', 'Não']:
            valores.append(0)
        elif resposta in ['Às vezes', 'Com dificuldade', 'Um pouco', 'Neutro', 'Já tive essa semana', 'Levemente', 'Com esforço', 'Não tive tempo']:
            valores.append(1)
        else:
            valores.append(2)
    
    # Pesos das perguntas (da tabela)
    pesos = [3, 2, 3, 2, 3, 3, 2, 2, 2]
    
    # Calcula o score
    score = 0
    for i in range(9):
        score += pesos[i] * valores[i]
    
    return score

def CalculaPercentual(matriz, nivel):
    total = len(matriz) - 1  # -1 para ignorar o cabeçalho
    if total == 0:
        return 0.0
    
    contador = 0
    for pessoa in matriz[1:]:  # Pula o cabeçalho
        if pessoa[-1].strip().lower() == nivel.strip().lower():  # Comparação mais flexível
            contador += 1
    
    return round((contador / total) * 100, 2)

def AtualizaMatrizScoreRisco(matriz):
    nova_matriz = [matriz[0] + ['Score', 'Risco']]  # Cabeçalho
    
    for pessoa in matriz[1:]:  # Pula o cabeçalho
        score = CalculaScoreIndividual(pessoa)
        risco = ClassificaNivelRisco(score)
        nova_matriz.append(pessoa + [score, risco])
    
    return nova_matriz

def ImprimeMatrizScoreRisco(matriz):
    print("Lista de Pessoas e seus Níveis de Risco:\n")
    for i in range(1, len(matriz)):  # pula o cabeçalho
        pessoa = matriz[i][0]
        risco = matriz[i][-1]
        print(f"{pessoa:<15} - {risco}")

def ClassificaNivelRisco(score):
    if score <= 10:
        return "Baixo risco"  # Removi o "Risco " e a exclamação
    elif score <= 20:
        return "Moderado risco"
    else:
        return "Alto risco" 
    
def SugereMinimizacaoSintomas(pergunta):
    sugestoes = [
        [1, "Evite estudar até tarde e reduza o uso de telas à noite.Incorpore pausas estratégicas durante o dia (técnica Pomodoro, por exemplo)."],
        [2, "Organize sua rotina com pequenas vitórias, como arrumar a cama ou tomar café — isso ativa o cérebro e gera estímulo."],
        [3, "Busque aplicar conteúdos em projetos reais, participar de hackathons, ou explorar temas que te inspiram dentro do curso."],
        [4, "Use listas com entregas claras e realistas por dia. Elimine distrações e crie um ambiente de foco (limpo, silencioso, com metas visíveis)."],
        [5, "Converse com colegas e professores, entenda o impacto do que você está estudando e crie conexões com seus valores pessoais. "],
        [6, "Reconheça o limite entre cansaço e sofrimento. Conversar com alguém que compreenda sua trajetória pode aliviar a sobrecarga emocional."],
        [7, "Mesmo em poucos minutos, práticas como respiração guiada ou alongamentos reduzem o acúmulo emocional. "],
        [8, "Uma ligação de 5 minutos ou uma pausa para café com alguém confiável ajuda a recuperar o senso de pertencimento. "],
        [9, "Desenhar, ouvir música, assistir algo leve, cozinhar... O prazer gratuito recarrega energia emocional e combate a anedonia."]
    ]
    
    for num in sugestoes:
        if num[0] == pergunta:
            return num[1]




