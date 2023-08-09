# Análise de Dados com Python

### Desafio:
""""
Você trabalha em uma empresa do varejo e tem milhares de clientes diferentes

Com o objetivo de aumentar o faturamento e o lucro da sua empresa, a diretoria quer conseguir identificar quem é o cliente ideal para seus produtos, baseado no histórico de compras dos clientes.

Para isso, ela fez um trabalho de classificar os clientes com uma nota de 1 a 100. Só que agora, sobrou para você conseguir, a partir dessa nota, descobrir qual o perfil de cliente ideal da empresa.

Qual a profissão? Qual a idade? Qual a faixa de renda? E todas as informações que você puder analisar para dizer qual o cliente ideal da empresa.

Base de Dados: clientes.csv

"""

#Passo 1: importar base de dados
import pandas
import openpyxl
import numpy

tabela = pandas.read_csv("clientes.csv", encoding="latin", sep =";")
    #Utilizando "latin" devido o csv estar em portugues


##Passo 2: visualizar a base de dados
    #entender as info q vc tem disponivel
    #procurar erros na base de dados

    #print(tabela)

##passo 3: Tratamento de dados
    #deletar informaçoes inuteis
tabela = tabela.drop("Unnamed: 8", axis =1)#tirar a coluna Unmaed: 8
    #axis = 1 -> coluna ; axies = 0 -> linha

    #reconhecer as colunas(string, numero...)
    #print(tabela.info())
tabela["Salário Anual (R$)"] = pandas.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")#coerce forçar um erro a virar numero


    #corrigir infos vazias
    #display(tabela[tabela["Profissão"].isna()])
tabela = tabela.dropna()


##Passo 4: Análise Inicial -> entender as notas dos clientes
#print(tabela.describe())
import plotly.express as px

    #criar e depois exibir grafico
    #for coluna in tabela.columns:
    #grafico = px.histogram(tabela, x="Profissão", y="Nota (1-100)", histfunc="avg", text_auto=True)
    #grafico.show()

#Passo 5: Analise completa -> entender como cada caracteristica do cliente impacta na nota
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto=True) # avg -> média
    grafico.show()


#Análise de dados final
"""
Perfil ideial de cliente
    Nao possui muita diferença entre os clientes de promocao e os de nao promocao
    Acima de 17 anos
    faixa salarial n parece fazer tanta diferença
    entreterimento e artitas possuem notas maiores; Contruçao possui uma media menor
    tem entre 10 e 15 anos de experiencia de trablho
    familias acima de 7 pessoas são ruins

Gráfico ID x Nota
    Não traz muitas informações uteis, tendo em consideração que o ID é apenas um identificador
Gráfico Origem X Nota
    Os clientes vindos de compras normais possuem a nota um pouco maior(4 pontos) em relação ao clientes de promoção
Gráfico Idade X Nota
    Apesar de não fazer sentido dados de pessoas com idade de pessoas menores de 15, temos que as notas começam a melhorar a partir
    dos 17 anos em diante 
Gráfico Salário anual X Nota
    Os salários de [0-500], [25000-30000] e [45000-50000] possuem a maior nota
    Os salários de [10000-25000] possuem a menor nota
Gráfico Nota X Nota
    O gráfico em questão não é útil
Gráfico Profissão X Nota
    os clientes de entreterimento e Artista possuem a maior nota
Gráfico Experiencia Trabalho X Nota
    Os clientes de 10 a 15 anosde experiência já possuem uma nota superior aos outros. Os clientes de 2 a 3 anos também possuem uma média de nota muito boa.
Gráfico Tamanho Família X Nota
    Os clientes com uma familia de 1 até 7 familiares tem uma media muito parecida e as pessoas com 8 e 9 possuem uma media menor
"""