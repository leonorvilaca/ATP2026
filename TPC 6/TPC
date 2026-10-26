def criarTab():
    num_dias = int(input("Quantos dias quer ter na sua tabela metereológica?"))
    tabMeteo = []
    while num_dias > 0:
        ano = int(input("Qual é o ano?"))
        while ano < 1:
            print("Ano inválido. Tente novamente.")
            ano = int(input("Qual é o ano?"))
        
        mes = int(input("Qual é o mês?"))
        while mes < 1 or mes > 12:
            print("Mês inválido. Tente novamente (1 a 12).")
            mes = int(input("Qual é o mês?"))

        if mes in (1, 3, 5, 7, 8, 10, 12):
            max_dia = 31
        elif mes in (4, 6, 9, 11):
            max_dia = 30
        elif (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            max_dia = 29
        else:
            max_dia = 28
        
        dia = int(input("Qual é o dia?"))
        while dia < 1 or dia > max_dia:
            print("Dia inválido. Tente novamente (1 a " + str(max_dia) + ").")
            dia = int(input("Qual é o dia?"))

        data = (ano, mes, dia)
        t_min = float(input("Qual a temperatura mínima registada?"))
        t_max = float(input("Qual a temperatura máxima registada?"))
        prec = float(input("Qual o valor de precipitação registado?"))
        tabMeteo.append((data, t_min, t_max, prec))
        num_dias = num_dias - 1
    return tabMeteo

def tem_media(tabMeteo):
    res = []
    for data, tmin, tmax, prec in tabMeteo:
        media = (tmin + tmax) / 2
        res.append((data,media))
    return res

def guardaTabMeteo(t, fnome):
    file = open(fnome, "w")
    for data, tmin, tmax, prec in t:
        ano, mes, dia = data
        file.write(f"{ano}-{mes}-{dia}|{tmin}|{tmax}|{prec}\n")
    file.close()
    return

def carregaTabMeteo(fnome):
    res = []
    file = open(fnome, "r")
    for line in file:
        data, tmin, tmax, prec = line.split("|") 
        ano, mes, dia = data.split("-")
        tempo = ((int(ano), int(mes), int(dia)),float(tmin), float(tmax), float(prec[:-1]))
        res.append(tempo)
    file.close()
    return res

def minMin(tabMeteo):
    minimo = tabMeteo[0][1]
    for dia in tabMeteo:
        if dia[1] < minimo:
            minimo = dia[1]
    return minimo

def amplTerm(tabMeteo):
    res = []
    for data, tmin, tmax, prec in tabMeteo:
        amplitude = tmax - tmin
        res.append((data,amplitude))
    return res

def maxChuva(tabMeteo):
    max_prec = tabMeteo[0][3]
    max_data = tabMeteo[0][0]
    for data, tmax, tmin, prec in tabMeteo:
            if prec > max_prec:
                max_prec = prec
                max_data = data
    return (max_data, max_prec)

def diasChuvosos(tabMeteo, p):
    prec_superior = []
    for data, tmax, tmin, prec in tabMeteo:
        if prec > p:
            prec_superior.append((data,prec))
    return prec_superior

def maxConsecLimite(tabMeteo, p):
    consec_atuais = 0
    maximo_diasconsec = 0
    for data, tmax, tmin, prec in tabMeteo:
        if prec < p:
            consec_atuais = consec_atuais + 1
            if consec_atuais > maximo_diasconsec:
                maximo_diasconsec = consec_atuais
        else:
            consec_atuais = 0
    return maximo_diasconsec


from matplotlib import pyplot as plt #biblioteca

def grafTabMeteo(t):
    y_min = [tmin for data, tmin, tmax, prec in t ]
    y_max = [tmax for data, tmin, tmax, prec in t ]
    y_prec = [prec for data, tmin, tmax, prec in t ]
    x = [f"{data[0]}-{data[1]}-{data[2]}" for data, *_ in t] 

    plt.plot(x,y_min, color="violet", marker="o", label="Tmin ºC") 
    plt.plot(x,y_max, color="red", marker="o", label="Tmax ºC")
    plt.title("Temperatura Mínima e Máxima")
    plt.legend()
    plt.grid(color="black")
    plt.show()

    plt.bar(x,y_prec, color="green", label="Precipitação (mm)")
    plt.title("Precipitação")
    plt.legend()
    plt.grid()
    plt.show()
    return

def mostrar_menu():
    print("\n===== MENU: ANÁLISE DE TABELAS METEREOLÓGICAS =====")
    print("""1) Calcular a temperatura média de cada dia;
2) Guardar a tabela meteorológica num ficheiro de texto;
3) Carregar a tabela meteorológica de um ficheiro de texto;
4) Calcular a temperatura mínima mais baixa registada na tabela;
5) Calcular a amplitude térmica de cada dia;
6) Calcular o dia em que a precipitação registada teve o seu valor máximo e indicar esse valor;
7) Dias com precipitação superior a um limite escolhido;    
8) Maior número de dias consecutivos com precipitação abaixo do limite escolhido;
9) Gráficos da temperatura mínima, máxima e de pluviosidade;
0) Sair da aplicação.\n""")

def principal():
    tabMeteo1 = criarTab()
    print(f"Tabela Metereológica: {tabMeteo1}")
    opcao = -1
    while opcao != 0:
        mostrar_menu()
        opcao = int(input("Escolha uma opção para a operação que pretende efetuar: "))

        if opcao == 0:
            print("\nA terminar a aplicação. Até à próxima!")
        elif opcao == 1:
            print(f"As temperaturas médias de cada dia são: {tem_media(tabMeteo1)}")
        elif opcao == 2:
            guardaTabMeteo(tabMeteo1,"metereologia.txt")
        elif opcao == 3:
            tabMeteo1_recup =carregaTabMeteo("metereologia.txt")
            print(f"A tabela metereológica recuperada é: {tabMeteo1_recup}")
        elif opcao == 4:
            print(f"A temperatura mínima mais baixa registada é: {minMin(tabMeteo1)}")
        elif opcao == 5:
            print(f"A amplitude térmica de cada dia é: {amplTerm(tabMeteo1)}")
        elif opcao == 6:
            diamaisprec = maxChuva(tabMeteo1)
            data, valorprec = diamaisprec
            print(f"Verificou-se o maior valor de precipitação no dia {data} e este valor foi de {valorprec}")
        elif opcao == 7:
            p1 = float(input("Que limite queres escolher para comparar com a precipitação?"))
            print(f"Os dias com precipitação superior a {p1} foram: {diasChuvosos((tabMeteo1), p1)}")
        elif opcao == 8:
            p2 = float(input("Que limite queres escolher para comparar com a precipitação?"))
            print(f"O maior nº de dia com precipitação inferior a {p2} foi: {maxConsecLimite(tabMeteo1, p2)}")
        elif opcao == 9:
            grafTabMeteo(tabMeteo1)
        else:
            print("\nOpção inválida! Tente novamente.")

principal()