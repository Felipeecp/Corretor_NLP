# Projeto NLP - Corretor ortográfico 

**Curso de NLP Alura, Construindo um corretor ortográfico utilizando python**

## Biblioteca Necessária
* <a href="https://www.nltk.org">NLTK</a>

## Lógica por trás do corretor 

1. Input de uma palavra escrita de maneira equivocada
2. Gerar possiveis palavras corretas
3. Verificar quais das possiveis palavras corretas é realmente a palavra correta.

## Algoritmos para correção
* Inserindo letras, para o caso em que a palavra falta uma letra.
* Deletando letras, para o caso em que a palavra tem letra a mais.
* Trocando letras, para o caso em que uma letra está trocada.
* Invertendo letras, para o caso em que uma letra está invertida.

## Base de dados

Como base de dados foi utilizado os artigos do blog da alura.
Para determinar o número de palavras foi utilizado a biblioteca nltk, foi separado todo o texto do arquivo em tokens.

Com isso foi possivel saber que nessa base de dados tinhamos 403104 palavras, para usarmos como base no corretor.

## Taxa de acertos do corretor

Para observar se o corretor estava funcionando corretamente foi utilizada uma base de teste com 186 palavras, que foram passadas para esse corretor desenvolvido e foi póssivel concluir o seguinte:

* A taxa de acerto para essa base de testes foi de 76.34% de acertos em um total de 186 palavras.

* Nesse erro 6.99% foi devido a palavras desconhecidas.

## Pontos para melhorar

* Utilizar outra base de dados com um número maior de dados. 

* O corretor só consegue encontrar erros a uma distancia da palavra correta. Por exemplo, ele pode corrigir lógiica para lógica, porém não vai conseguir de lógiiica para lógica.

