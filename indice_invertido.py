import sys
import nltk
def retorna_conteudo_lista(nome_arquivo):
    arq = open(nome_arquivo,"r",encoding="utf-8")
    linhas = arq.readlines()
    arq.close()
    return linhas
def transforma_minuscula(string):
    return string.lower()
def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l
def escreve_arquivo(string):
    arq = open("indice.txt","a")
    arq.write(string)
    arq.close()
def apaga_arquivo():
    arq = open("indice.txt","w")
    arq.close()
def subs_virg_espaco(string):
    tam = len(string)
    if tam <= 4:
        return string
    else:
        if tam > 4:
            cont = 0
            frase = ''
            for var in string:
                if (var.isdigit() or var == ',') and cont < 3:
                    cont = cont + 1
                    frase = frase + var
                else:
                        frase = frase + ' '
                        cont = 0
    return frase

if len(sys.argv) == 2:
    param = sys.argv[1]
    linhas = retorna_conteudo_lista(param)
    #print("Dados que tem dentro de arquivo.txt\n")
    #print(linhas)
    #print("\n")
    #declarando o dicionario
    dic = {}
    #contador para numerar os arquivos
    cont = 1
    #acessando os dados dos caminhos que tem no primeiro arquivo
    for i in linhas:
        nome = i.rstrip() #tirando os \n com rstrip
        #print("Esses Dados sao do arquivo: ",nome)
        conteudo = retorna_conteudo_lista(nome)
        # colocando em um dicionario
        dic[cont] = conteudo
        cont = cont + 1
    #mostrando o que tem nos arquivos
    #print(dic)
    cont1 = 1
    dicionario = {}
    for item in dic:
        frases = ""
        for i in range(len(dic[item])):
           frases = frases + dic[item][i].replace("\n"," ").replace("."," ").replace(";"," ").replace("?"," ").replace("!"," ").replace(","," ").lower()
        dicionario[cont1] = frases
        cont1 = cont1 + 1
    # A variavel dicionario tem todos as frases do arquivo
    #print(dicionario)
    #Tirando as stopwords e os radicais das palavras
    dicionario_semstopwords = {}
    cont2 = 1
    stopwords = nltk.corpus.stopwords.words
    stopwords = nltk.corpus.stopwords.words("portuguese")
    #print(stopwords)
    stemmer = nltk.stem.RSLPStemmer()
    for chave in dicionario:
        conteudo = nltk.word_tokenize(dicionario[chave])
        conteudo_sem_stopwords = ""
        for x in conteudo:
            if x not in stopwords:
                conteudo_sem_stopwords += stemmer.stem(x) + " "
        dicionario_semstopwords[cont2] = conteudo_sem_stopwords
        cont2 = cont2 + 1
    dicionario_comparacao = {}
    cont3 = 1
    for chave in dicionario_semstopwords:
        conteudo = nltk.word_tokenize(dicionario_semstopwords[chave])
        dicionario_comparacao[cont3] = conteudo
        cont3 = cont3 + 1
    #print(dicionario_comparacao)
    #print(dicionario_semstopwords)
    dicionario_comparacao_sem_repetidos = {}
    cont6 = 1
    for chave in dicionario_comparacao:
       dicionario_comparacao_sem_repetidos[cont6] = remove_repetidos(dicionario_comparacao[chave])
       cont6 = cont6 + 1

    #print(dicionario_comparacao_sem_repetidos)
    dicionario_contador = {}
    #dicionario_contador["palavra" ] = "Arquivo,Quantidade"
    cont4 = 1
    cont5 = 0
    for chave in dicionario_comparacao:
        contador_radicais = 0
        for x in dicionario_comparacao_sem_repetidos[chave]:
            contador_radicais = dicionario_comparacao[cont4].count(x)
            #dicionario_contador[cont5] = [x + ':',chave,contador_radicais]
            #print("{}: ".format(x), "{},".format(chave), "{}".format(contador_radicais))
            #cont5 = cont5 + 1
            if x not in dicionario_contador:
                dicionario_contador[x] = [chave, contador_radicais]
            else:
                dicionario_contador[x] = dicionario_contador[x] + [chave,contador_radicais]
        cont4 = cont4 + 1

    #print(dicionario_contador)
    apaga_arquivo()
    resposta = ""
    for ch in dicionario_contador:
        resposta = ch + ": " + subs_virg_espaco(str(dicionario_contador[ch]).strip('[]').replace(' ', '')) + '\n'
        #print(resposta)
        escreve_arquivo(resposta)

else:
    print('Erro: A entrada precisa ter 2 parametros')




