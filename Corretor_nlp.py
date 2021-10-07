import nltk

def separa_palavras(lista_tokens):
    lista_palavras = []
    for token in lista_tokens:
        if token.isalpha():
            lista_palavras.append(token)
    return lista_palavras

def normalizacao(lista_palavras):
    lista_normalizada = []
    for palavra in lista_palavras:
        lista_normalizada.append(palavra.lower())
    return lista_normalizada

def insere_letras(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:   
        for letra in letras:
            novas_palavras.append(E + letra + D)
    return novas_palavras

def deletando_caracteres(fatias):
    novas_palavras = []
    for E, D in fatias:
        novas_palavras.append(E+D[1:])
    return novas_palavras

def troca_letra(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:   
        for letra in letras:
            novas_palavras.append(E + letra + D[1:])
    return novas_palavras

def inverte_letras(fatias):
    novas_palavras = []
    for E, D in fatias:
        if len(D)>1:
            novas_palavras.append(E+D[1]+D[0]+D[2:])
    return novas_palavras

def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra)+1):
        fatias.append((palavra[:i],palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deletando_caracteres(fatias)
    palavras_geradas += troca_letra(fatias)
    palavras_geradas += inverte_letras(fatias)
    return palavras_geradas



def probabilidade(palavra_gerada):
    total_palavras = len(palavras_normalizada)
    return frequencia[palavra_gerada]/total_palavras

def corretor(palavra):
    palavras_geradas = gerador_palavras(palavra)
    palavra_correta = max(palavras_geradas, key=probabilidade)
    return palavra_correta

def avaliador(testes,vocabulario):
    numero_palavras = len(testes)
    acertou = 0
    desconhecida = 0
    for correta, errada in testes:
        palavra_corrigida = corretor(errada)
        if palavra_corrigida == correta:
            acertou+=1
        else:
            desconhecida += (correta not in vocabulario)
            
    taxa_acerto = acertou/numero_palavras
    taxa_desconhecida = desconhecida/numero_palavras
    print(f"\ntaxa de acerto: {round(taxa_acerto * 100,2)}% de acertos em um total de {numero_palavras} palavras")
    print(f"taxa de palavras desconhecidas: {round(taxa_desconhecida * 100,2)}% de palavras desconhecidas em um total de {numero_palavras} palavras")

def cria_dados_teste(nome_arquivo):
    lista_palavras_teste = []
    f = open(nome_arquivo, "r", encoding='UTF-8')
    for linha in f:
        correta, errada = linha.split()
        lista_palavras_teste.append((correta, errada))
    f.close()
    return lista_palavras_teste

# Abrindo artigos que serviram com base de palavras para o corretor
with open("corretor-master/artigos.txt","r", encoding="utf8") as f:
    artigos = f.read()

# Separando tokens do artigo 
lista_tokens = nltk.tokenize.word_tokenize(artigos)

lista_palavras = separa_palavras(lista_tokens)
palavras_normalizada = normalizacao(lista_palavras)

frequencia = nltk.FreqDist(palavras_normalizada)

# Recuperando palavras únicas da base de palavras
vocabulario = set(palavras_normalizada)

# Criando dados de teste
lista_teste = cria_dados_teste("corretor-master/palavras.txt")       
avaliador(lista_teste, vocabulario)

palavra = input('\nDigite uma palavra: ')
print('Correção :' +corretor(palavra)+'\n')


