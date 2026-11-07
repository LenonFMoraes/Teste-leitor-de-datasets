from dbm import error
from logging import exception
import streamlit as st
import pandas as pd

import numpy as np











def contar_linhas(self):
        return len(self.bd)

def mostrar_bd(self):####mostra o dataframe
        return self.bd


def Mostrar_Nulos(self):###Conta quantas linhas tem valores nulos

        return self.bd.isna().sum().to_dict()

def Remover_Nulos(self,col):###remove valores nulos
        self.bd=self.bd.dropna(subset=[col])


def Preencher_Nulos(self,col,opcao):
        if opcao == "Média":
            self.bd[col]= self.bd[col].fillna(self.bd[col].mean())
        elif opcao == '0':
            self.bd[col]= self.bd[col].fillna(0)
        elif opcao == 'Mediana':
            self.bd[col]= self.bd[col].median()
        else :
            return


def Mostrar_nao_Nulos(self):###conta quantas linhas estão sem valores nulos
        'não nulos'
        return self.bd.notnull().sum()


def mostrar_primeiros(self):###mostra as primeiras linhas do dataframe
        return self.bd.head()

def analisar_colunas(self):###Função que pega o dataframe e analisa quais tipos de dados compões cada coluna
        self.tipo_coluna={}###dicionário que vai guardar o par nome de uma coluna e o tipo de dado que a compõe(numérico ou categórico)

        ##print(f'O dataset tem {len(self.bd.columns)} colunas')
        for nome_coluna in self.bd.columns:##
            sem_nulos=self.bd[nome_coluna].dropna()

            Tres_primeiros=(sem_nulos.head(3).tolist()) ###minha ideia foi pegar os 3 valores do inicio e os 3 ultimos-
                                                                   ###para ver o tipo de dado predominante na coluna
            print()
            Tres_ultimos=(sem_nulos.tail(3).tolist())
            print()
            lista_valores=list(dict.fromkeys(Tres_primeiros+Tres_ultimos))##cria uma lista de valores únicos(pra evitar caso-
                                                                          ##o dataset seja muito pequeno dar algum erro)
            print(lista_valores)
            contador = 0 ###contador numérico
            conta_erro = 0###contador de strings(quando o try falha de converter o dado para número)

            for num in range(len(lista_valores)):

            ##percorre a coluna contando os dados das linhas e checando os tipos
                    try:

                        lista_valores[num]=float(lista_valores[num])
                        contador+=1

                        if contador>=len(lista_valores): ###se os dados forem todos numericos a coluna recebe essa atribuição
                            print("Coluna Numérica")
                            self.tipo_coluna[nome_coluna]='Numérica' ###salva a combinação para adicionar a classe no fim
                                                                     ##do código

                    except Exception as error:
                    ###caso não consiga fazer a conversão a coluna é atribuída como categórica(strings)
                        conta_erro += 1
                        if conta_erro >= len(lista_valores):
                            print(f'Coluna Categórica, Erro:{error}')
                            self.tipo_coluna[nome_coluna]='Categórica'


        return self.tipo_coluna####retorna o dicionário criando um atributo para o mesmo na classe analisada

def renomear_coluna(self,col,novo_nome):
    tipo_de_coluna=self.tipo_coluna[col]
    self.bd.rename(columns={col:novo_nome}, inplace=True)
    self.tipo_coluna[novo_nome]=tipo_de_coluna
    del(self.tipo_coluna[col])


def deletar_coluna(self,col):

    self.bd.pop(col)
    self.tipo_coluna.pop(col)
    self.resumo_estatistico.pop(col)
    ajustes=[]
    for i in self.dists:
        chave=i.split('¨')

        if col == chave[1]:
            ajustes.append(i)
    for n in ajustes:
        self.dists.pop(n)
    else:
          self.bd.pop(col)



def recorte(self,col,minimo,maximo):
    '''A função recebe o nome da coluna e os limites escolhidos pelo usuário na interface
    para remover possíveis outliers da análise.'''

    if minimo=='minimo':
       minimo=self.bd[col].min()

    if maximo=='maximo':
       maximo=self.bd[col].max()


    self.bd[f'{col}_filtrada']=self.bd[col].loc[(self.bd[col]>=minimo) & (self.bd[col]<=maximo) ]















