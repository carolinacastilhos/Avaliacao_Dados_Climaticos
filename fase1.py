# *******************************************FASE 1****************************************************************



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
#                                         Exibição de Lista de Lista de Dados 
#-------------------------------------------------------------------------------------------------------------------
def exibeLista(lista):
    nova = []
    indice = 0
    while indice < len(lista):
        nova.append(lista[indice].split(';'))
        indice += 1
    return print(f"\n>>> Lista de Dados Climáticos: \n\n{nova}")

#-------------------------------------------------------------------------------------------------------------------
#                                      Gravação dos Dados em Lista de Lista e em Arquivo txt 
#-------------------------------------------------------------------------------------------------------------------
def gravaArquivo(nome, dados):
    lista = list(dados)
    arquivo = open(nome, "w")
    nova = []
    indice = 0
    while indice < len(lista):
        nova.append(lista[indice].split(';'))
        indice += 1
    arquivo.write(str(nova))
    arquivo.close()    

#-------------------------------------------------------------------------------------------------------------------
#                                          Conversão e Estruturação de Dados
#-------------------------------------------------------------------------------------------------------------------
def conversaoDados(linha):
    itens = linha.split(';')
    itensConvertidos = [itens[0]] #ao invés de iniciar vazia, a lista já inicia com a string 'data' (índice zero) para não ser convertida em float
    contador = 1  
    while contador <len(itens):
        itensConvertidos.append(float(itens[contador])) #converte demais itens da lista em float. Dados convertidos para serem usados na fase 2 do projeto. 
        contador += 1
    return itensConvertidos 

#-------------------------------------------------------------------------------------------------------------------
#                               Criação da Lista de Lista com os Dados, sem Cabeçalho
#-------------------------------------------------------------------------------------------------------------------    
def criaLista(lista):
    listaDeItens = []
    contador = 1 #inicia a contagem a partir do índice 1 para não incluir o cabeçalho
    while contador < len(lista):
        listaDeItens.append(conversaoDados(lista[contador]))
        contador += 1    
    return listaDeItens
#-------------------------------------------------------------------------------------------------------------------
#                                        Exibe Resultado dos Dados - Precipitação
#-------------------------------------------------------------------------------------------------------------------
def exibeResultadoPrecipitação(lista): 
    resultado = []
    for item in lista:
      if data in item[0]:
          resultado.append(item[0:2])   
    if len(resultado) == 0:
        return print(f"\n>>> Não há dados para o período informado: {data}")
    else:
        return print(f"\n>>> Precipitação em {data}:\n {resultado}")                    
    
# #-------------------------------------------------------------------------------------------------------------------
# #                                      Exibe Resultado dos Dados - Temperatura Máxima
# #-------------------------------------------------------------------------------------------------------------------
def exibeResultadoTemperatura(lista, ano):
    resultado = []
    meses = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    for mes in meses:
        data = f"/{mes}/{ano}"
        contador = 0
        for item in lista:
            if data in item[0]:
                resultado.append(item[0]) 
                resultado.append(item[2]) 
                contador += 1
                if contador == 7:
                    break
    if len(resultado) == 0:
        return print(f"\n>>> Não há dados para o período informado: {anoTemperatura}")
    else:
        return print(f"\n>>> Temperatura máxima dos 7 primeiros dias dos meses de {anoTemperatura}:\n {resultado}")               
    
#-------------------------------------------------------------------------------------------------------------------
#                                                    Programa
#-------------------------------------------------------------------------------------------------------------------
dadosProjeto = cargaDosDados('ArquivoDadosProjeto.csv')
cabecalho = dadosProjeto[0].split(';')
dadosTratados = criaLista(dadosProjeto)

while True:
    print(" ") 
    print("-"*80)
    print(" Informações climáticas do município de Porto Alegre, entre os anos 1961 e 2016")
    print("-"*80)
    print("\n---- MENU ----")
    print("1) Exibir Lista dos Dados Climáticos")
    print("2) Gravar Dados em Arquivo txt")
    print("3) Dados da Precipitação")
    print("4) Dados da Temperatura Máxima")
    print("0) Sair do Programa")
    opcao = input("Informe a opção desejada: ")
    if opcao == "0":
        print("\n>>> Programa Finalizado. ")
        break
    else:
        if opcao == "1":
            exibeLista(dadosProjeto)
        elif opcao == "2": 
            gravaArquivo('ListaDados.txt', dadosProjeto)
            print("\n>>> Dados gravados com sucesso!\n")
        elif opcao == "3":
            print("\n---- DADOS DA PRECIPITAÇÃO (em milímetros por m2) ---- \n")
            anoPrecipitacao = (input("Informe o ano que gostaria de saber a informação (entre 1961 e 2016): "))
            mesPrecipitacao = (input("Informe o mês (entre 01 e 12): "))
            if (anoPrecipitacao < "1961" or anoPrecipitacao > "2016") or (mesPrecipitacao < "01" or mesPrecipitacao > "12"):
                print("\n>>> O período informado é inválido.")                
            else:
                data = f"{mesPrecipitacao}/{anoPrecipitacao}"
                exibeResultadoPrecipitação(dadosTratados)
        elif opcao == "4":
            print("\n---- DADOS DA TEMPERATURA MÁXIMA (em graus celsius) ---- \n")
            anoTemperatura = (input("Informe o ano que gostaria de saber a informação (entre 1961 e 2016): "))
            if (anoTemperatura < "1961" or anoTemperatura > "2016") or (len(anoTemperatura) != 4):
                print("\n>>> O ano informado é inválido.")
            else:
                data2 = f"{anoTemperatura}"
                exibeResultadoTemperatura(dadosTratados, anoTemperatura)
        else: print("\n>>> Opção invalida. Digite uma opção entre 1 e 0.")