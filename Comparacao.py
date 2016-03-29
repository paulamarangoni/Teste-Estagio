######## Antes de rodar é preciso ajustar o resultado do PAOD #######
diretorio1 = '/home/paula/Documentos/Estagio_UERJ'
PAOD = open(diretorio1 + '/colunas_teste.txt')

Manual = open(diretorio1 + '/metar_sbgl_01_2016_alterado_manual.txt')

if PAOD == Manual:
    print('Ok, graças a Deus!!!')

