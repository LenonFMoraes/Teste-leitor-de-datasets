import numpy as np
import scipy.stats as stats
from pandas.core.methods.to_dict import to_dict


def calcular(self,col): #recebe o dataset e dispara todas as funções de calculo,depois retorna os valores
    resultados_coluna={}
    if self.tipo_coluna[col]=='Numérica':
        media(self,col,resultados_coluna)
        mediana(self,col,resultados_coluna)
        maximo(self,col,resultados_coluna)
        minimo(self,col,resultados_coluna)
        moda(self,col,resultados_coluna)
        desvio_padrao(self,col,resultados_coluna)
        variancia(self,col,resultados_coluna)

        self.resumo_estatistico[col]=resultados_coluna


    else:
        moda(self,col,resultados_coluna)
        qt_unicos(self,col,resultados_coluna)
        unicos(self,col,resultados_coluna)
        frequencia(self,col,resultados_coluna)
        self.resumo_estatistico[col]=resultados_coluna
    return self.resumo_estatistico[col]

def media(self,col,resultado):
    resultado['media'] =round(float(np.mean(self.bd[col])),2)
    return resultado['media']

def mediana(self,col,resultado):
    resultado['mediana']=round(float(np.median(self.bd[col])),2)
    return resultado['mediana']

def maximo(self,col,resultado):
    resultado['max'] = round(int(np.max(self.bd[col])),2)
    return resultado['max']


def minimo(self,col,resultado):
    resultado['min']=round(int(np.min(self.bd[col])),2)
    return resultado['min']

def moda(self,col,resultado):
    if self.tipo_coluna[col]=='Numérica':
        resultado['moda'] =int(self.bd[col].mode()[0])
        return resultado['moda']
    else:
        resultado['moda'] =self.bd[col].mode()[0]
        return resultado['moda']

def desvio_padrao(self,col,resultado):
    resultado['desvio_padrao'] =round(float(np.std(self.bd[col],ddof=1)),2)
    return resultado['desvio_padrao']

def variancia(self,col,resultado):
    resultado['variancia'] =round(float(np.var(self.bd[col], ddof=1)),2)
    return resultado['variancia']

def qt_unicos(self,col,resultado):
    resultado['contagem'] = self.bd[col].nunique()
    return resultado['contagem']

def frequencia(self,col,resultado):
    resultado['frequencia']= (self.bd[col].value_counts(normalize=True)*100).to_dict()
    for valor in resultado['frequencia']:
        resultado['frequencia'][valor]=round(resultado['frequencia'][valor],2)
        resultado['frequencia'][valor]=str(resultado['frequencia'][valor])
        resultado['frequencia'][valor]=resultado['frequencia'][valor]+'%'
    return resultado['frequencia']

def unicos(self,col,resultado):
    resultado['unicos']= self.bd[col].unique().tolist()

    return resultado['unicos']