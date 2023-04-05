import statistics
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------------------------------------------------
#                                      Leitura do Arquivo com Dados do Projeto
#-------------------------------------------------------------------------------------------------------------------
def cargaDosDados(nome):     
        arquivo = open(nome, "r") 
        dados = []
        for linha in arquivo: 
            linha1 = linha[:-1] #retira \n do final de cada linha
            dados.append(linha1)
        arquivo.close()
        return dados

#-------------------------------------------------------------------------------------------------------------------
#                               Criação da Lista de Lista com os Dados, sem Cabeçalho
#-------------------------------------------------------------------------------------------------------------------    
def criaLista(lista):
    listaDeItens = []
    contador = 1 #inicia a contagem a partir do índice 1 para não incluir o cabeçalho
    while contador < len(lista):
        listaDeItens.append(lista[contador].split(';'))
        contador += 1    
    return listaDeItens

# #-------------------------------------------------------------------------------------------------------------------
# #                                          Criação de Listas de Dicionários 
# #-------------------------------------------------------------------------------------------------------------------  
def listaDeDicionarios(lista):
    dicionarios = []
    decada = 0
    for item in lista:  
        if int(item[0][6:10]) < (1971):
            decada = 1960
        elif int(item[0][6:10]) < (1981):
            decada = 1970
        elif int(item[0][6:10]) < (1991):
            decada = 1980
        elif int(item[0][6:10]) < (2001):
            decada = 1990
        elif int(item[0][6:10]) < (2011):
            decada = 2000
        elif int(item[0][6:10]) < (2021): #porém dados vão até 2016
            decada = 2010
        dicionarios.append({
            "decada": decada,
             "ano": int(item[0][6:10]),  #conversão de dados em int e float para serem usados nas análises estatísticas
             "mes": int(item[0][3:5]),
             "dia": int(item[0][0:2]),
             "precip": float(item[1]),     
             "maxima": float(item[2]),
             "minima": float(item[3]),
             "horas_insol": float(item[4]),
             "temp_media": float(item[5]),
             "um_relativa": float(item[6]),
             "vel_vento": float(item[7])               
             })
    return dicionarios

#-------------------------------------------------------------------------------------------------------------------
#                                                   Dados Precipitação
#-------------------------------------------------------------------------------------------------------------------

def acumuladoMes(lista, mes, ano):
    soma = 0
    for item in lista:
        if item["ano"] == ano:
            if item["mes"] == mes:
                soma += item["precip"]
    return soma


def mesMaisChuvoso():
    precipitacao = []
    meses = []

    dadosProjeto = cargaDosDados('ArquivoDadosProjeto.csv')
    amostra = criaLista(dadosProjeto)
    chuva = listaDeDicionarios(amostra)

    for ano in range(1961,2017): #colocado 2017, pois vai até 2016
        for mes in range(1,13): #colocado 13, pois vai até 12 (dezembro)
            chuvaMes = acumuladoMes(chuva, mes, ano)
            precipitacao.append(chuvaMes)
            meses.append((mes,ano))

    for mes in range(1,8): #colocado 8 por que assim vai até 7 (julho), e o dados em 2016 vão até julho
        chuva2017 = acumuladoMes(chuva, mes, 2017) 
        precipitacao.append(chuva2017)
        meses.append((mes, 2017))
   
    for i in range(0,len(precipitacao)-1):
        for j in range(0,len(precipitacao)-1-i):
            if precipitacao[j]<precipitacao[j+1]:  
                aux = precipitacao[j]
                precipitacao[j] = precipitacao[j+1]
                precipitacao[j+1] = aux
                aux = meses[j]
                meses[j] = meses[j+1]
                meses[j+1] = aux
    print("\n---- MÊS COM MAIOR VALOR ACUMULADO DE CHUVA DE 1961 A 2016 ---- \n")
    print(f"\nO mês de {meses[0]} possui o maior valor acumulado de chuva no período avaliado, totalizando {precipitacao[0]:.3f} mm/m²\n")

#-------------------------------------------------------------------------------------------------------------------
#                                               Dados mês de agosto
#-------------------------------------------------------------------------------------------------------------------

#>>>>>>>>Temperatura mínima 

def tempMinAgosto(ano):
    dadosProjeto = cargaDosDados('ArquivoDadosProjeto.csv')
    amostra = criaLista(dadosProjeto)
    agostos = listaDeDicionarios(amostra)
    temperatura = 0
    dias = 0
    minimas = []
    for item in agostos:
        if item["ano"] == ano:
            if item["mes"] == 8: 
                temperatura += item["minima"]
                dias += 1
                minimas.append(item["minima"])
    moda = statistics.mode(minimas) 
    media = temperatura/dias 
    print(f"Em agosto de {ano} a média das temperaturas mínimas foi {media:.3f}°C e a moda foi {moda:.3f}°C")

#>>>>>>>>Vento

def ventoAgosto(ano):
    dadosProjeto = cargaDosDados('ArquivoDadosProjeto.csv')
    amostra = criaLista(dadosProjeto)
    agostos = listaDeDicionarios(amostra)
    vento = 0
    dias = 0
    velocidadeVento = []
    for item in agostos:
        if item["ano"] == ano:
            if item["mes"] == 8: 
                vento += item["vel_vento"]
                dias += 1
                velocidadeVento.append(item["vel_vento"])
    moda = statistics.mode(velocidadeVento) 
    media = vento/dias
    print(f"Em agosto de {ano} a média da velocidade do vento foi {media:.3f} m/s e a moda {moda:.3f} m/s")

#>>>>>>>>>Umidade

def umidadeAgosto(ano):
   
    dadosProjeto = cargaDosDados('ArquivoDadosProjeto.csv')
    amostra = criaLista(dadosProjeto)
    agostos = listaDeDicionarios(amostra)
    umidade = 0
    dias = 0
    umidadeRelativa = []
    for item in agostos:
        if item["ano"] == ano:
            if item["mes"] == 8: 
                umidade += item["um_relativa"]
                dias += 1
                umidadeRelativa.append(item["um_relativa"])
    moda = statistics.mode(umidadeRelativa) 
    media = umidade/dias 
    print(f"Em agosto de {ano} a média da umidade relativa do ar foi {media:.3f}% e a moda {moda:.3f}%")
   

#>>>>>>>> Exibição dos dados

def dadosAgostos():
    print("\n---- DADOS DO INVERNO DE 2006 A 2016 (MÊS DE AGOSTO) ---- \n")
    for ano in range(2006,2016):
        tempMinAgosto(ano)
        umidadeAgosto(ano)
        ventoAgosto(ano)
        print("\n")
    print("O ano de 2016 não possui dados para o mês de agosto.\n")
    print("A ")

#-------------------------------------------------------------------------------------------------------------------
#                                               Década mais chuvosa
#-------------------------------------------------------------------------------------------------------------------
def acumuladoDecada(lista, decada):
    soma = 0
    for item in lista:
        if item["decada"] == decada:
            soma += item["precip"]
    if decada == 2010:
        media = soma/5.5   #média da década que vai até metade de 2016
    else:
        media = soma/10     #média da decada completa
    return media


def decadaMaisChuvosa():
    precipitacao = []
    decadas = ["1960", "1970", "1980", "1990", "2000", "2010"]
    dadosProjeto = cargaDosDados('ArquivoDadosProjeto.csv')
    chuvaDecada = criaLista(dadosProjeto)
    chuva = listaDeDicionarios(chuvaDecada)
    chuva1960 = acumuladoDecada(chuva, 1960)
    chuva1970 = acumuladoDecada(chuva, 1970)
    chuva1980 = acumuladoDecada(chuva, 1980)
    chuva1990 = acumuladoDecada(chuva, 1990)
    chuva2000 = acumuladoDecada(chuva, 2000)
    chuva2010 = acumuladoDecada(chuva, 2010)
    precipitacao.append(chuva1960)
    precipitacao.append(chuva1970)
    precipitacao.append(chuva1980)
    precipitacao.append(chuva1990)
    precipitacao.append(chuva2000)
    precipitacao.append(chuva2010)
    print("\n---- DÉCADA COM MAIOR MÉDIA DE CHUVA ACUMULADA POR ANO ---- \n") 
    print("A precipitação média por ano das décadas ", decadas, " foi, respectivamente: \n", precipitacao, "\n")

 #>>>>>>>>> Gráfico

    plt.bar(decadas, precipitacao, color = "pink") # plota o gráfico de barras
    plt.title("Precipitação acumulada média por ano (mm/m²) da década de 1960 a década de 2010") # título do gráfico
    plt.xlabel("Décadas") # legenda eixo x
    plt.ylabel("Média de chuva acumulada por ano(mm/m²)") # legenda eixo y
    plt.show() # exibe o gráfico

    for i in range(0,len(precipitacao)-1): # Vai ordenar as listas
        for j in range(0,len(precipitacao)-1-i):
            if precipitacao[j]<precipitacao[j+1]:  #decrescente
                aux = precipitacao[j]
                precipitacao[j] = precipitacao[j+1]
                precipitacao[j+1] = aux
                aux = decadas[j]
                decadas[j] = decadas[j+1]
                decadas[j+1] = aux
                
    print(f"A década {decadas[0]} possuiu a maior média de chuva acumulada por ano no período avaliado: {precipitacao[0]:.3f} mm/m² de chuva.")


#-------------------------------------------------------------------------------------------------------------------
#                                                    Programa
#-------------------------------------------------------------------------------------------------------------------
  
try:
    print(" ") 
    print("-"*82)
    print("INFORMAÇÕES CLIMÁTICAS DO MUNICÍPIO DE PORTO ALEGRE, ENTRE OS ANOS DE 1961 E 2016")
    print("-"*82)
    
    mesMaisChuvoso()         
    dadosAgostos()    
    decadaMaisChuvosa()

except FileNotFoundError:
        print('\n\n>>>> O arquivo de dados não foi encontrado.')
