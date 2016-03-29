 ####### Iniciando Programa de Avançado de Organização de Dados - PAOD #################
#-*-encoding:UTF-8-*-
# Importei o numpy.
import numpy as np
 # Abrindo o arquivo texto. Foi indicado todo o caminho até o arquivo.
diretorio = '/home/paula/Documentos/Estagio_UERJ/metar_sbgl_01_2016.txt'

arquivo = open(diretorio)

# Preciso fazer com que o arquivo seja lido linha por linha.
# Leu cada linha e transformou numa lista com 1598 índices, cada indice é uma linha de texto. (lista para string)
linhas = arquivo.readlines()
# Digo para ele que colunas é uma lista vazia.
colunas = []
# Lista vazia.
lista_X = []
lista_4 = []
# Faço um loop que percorre as linhas do arquivo. a é a própria linha de texto.
for a in linhas:
    # Isso ignora as linhas vazias /n, pq se  indice for 0, a linha começa com 2016...
    if a.find('20') > -1:
        # Ignora se tiver SABZ, pois sab = -1, quer dizer que não encontrou.
        if a.find('SABZ') == -1:
            # Pula todos os dados que tiverem com SAXX.
            if a.find('SAXX') == -1:
                # Ignora as linhas de dados faltosos. As quais contém REDEMET em comum.
                if a.find('REDEMET') == -1:
                    # Ignora os dados de erro que tem MySQL.
                    if a.find('MySQL') == -1:
                        # Eliminou o /n do final de cada linha com o [:-1]. Adicionou tudo (sem as coisas que eu não preciso) a lista colunas.
                        colunas.append(a.split(' ')[:-1]) # O split quebra as linhas, separando os campos por espaço.
# Faz um loop para cada campo na lista de listas (colunas).
#lista_2 = [9, 10]
#lista_3 = [8, 9, 10]
for x in colunas:
# Se na segunda coluna do arquivo tiver -, apaga a coluna do traço.
    if x[1] == '-': x.pop(1)
    ######## Juntando metar + cor ################################
    if x[2][0:3] == 'COR':
        # Localiza o cor e o metar na lista
        cor = x[2]
        metar = x[1]
        # Une os dois com o +
        metarcor = metar + cor
        # Apaga os individuais, metar
        x.pop(1)
        # Acrescenta o novo metaecor (junto)
        x.insert(1, metarcor)
        # Apaga o cor.
        x.pop(2)
    # Lista vazia.
    y = []
    # Para um índice do comprimento de x (anda entre todos os caracteres de cada campo). Cada ind é um indice que anda no comprimento do x.
    for ind in range(len(x)):
        # SE for encontrado R na posição 0 e / na posição 3, faça:
        if x[ind].find('R') == 0 and x[ind].find('/') == 3:
            # Coloque esses resultados na lista y.
            y.append(ind)
    # Depois do for coloque em ordem decrescente, reverter, o conteudo da lista y.
    y.reverse()
    # Um loop para os itens da nova lista
    for ind in y: x.pop(ind) # o x pop vai apagar cada item.

    ######## Consertando a visibilidade ###############################################
    ######## Unir os dados adicionais de visibilidade como 5000 1200NE ################
    # Se a quinta coluna for um número.
    if x[5].isnumeric():
        # Se a sexta coluna tiver um numero de 4 digitos
        if x[6][0:4].isnumeric():
            # Soma as duas colunas.
            # Guarda o resultado da soma na coluna anterior.
            x[5] += x[6]
            # Apaga a informação adicional de visibilidade.
            x.pop(6)
    elif x[5][0:6] == 'CAVOK':
        lista_X = [6, 7, 8, 9, 10]
        # Fiz um for para evitar de colocar varios inserts, já que eu quero que cada X seja um campo separado na lista.
        for ind in lista_X:
            x.insert(ind, 'X')
    nuvens = ('FEW', 'SCT', 'BKN', 'OVC')
    # Sem tempo presente
    if x[6].startswith(nuvens) or x[6].startswith('NSC'):
        x.insert(6, 'X')
    # Com tempos presentes ##################################################
    # SE tiver tempo presente
    # Quando nao começa com x tem tempo prese. Quando a coluna 7 não começa com nuvens ou nsc, so pode ser os tempo presente adicional. 
    if not x[6].startswith('X') and not x[7].startswith(nuvens) and not x[6].startswith('NSC'):
            x[6] += x[7]
            x.pop(7)
    # Tem nuvem no 7 não tem no resto e o and not exclui o caso de aparecer quem tem cavok.
    if not x[8].startswith(nuvens) and not x[8].startswith('X'):
        for ind in range(3): x.insert(8, 'X')
    if not x[9].startswith(nuvens) and not x[9].startswith('X'):
        for ind in range(2): x.insert(9, 'X')
    if not x[10].startswith(nuvens) and not x[10].startswith('X'):
        for ind in range(1): x.insert(10, 'X')
########## Retirando / das temperaturas e separando em 2 colunas.
    temp = x[11].split('/')
    x.insert(11, temp[0])
    x.pop(12)
    x.insert(12, temp[1])  
# Salva o arquivo gerado no formato string, vom delimitador de ,
np.savetxt('colunas_teste.txt', colunas, fmt = '%s', delimiter = ',')
 
