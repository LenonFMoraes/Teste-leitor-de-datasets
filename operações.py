import numpy as np
import scipy.stats as stats



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
        #contagem(col,resultados_coluna)

        self.resumo_estatistico[col]=resultados_coluna
    return self.resumo_estatistico[col]
def media(self,col,resultado):
    resultado['media'] =round(float(np.mean(self.bd[f'{col}'])),2)
    return resultado['media']

def mediana(self,col,resultado):
    resultado['mediana']=round(float(np.median(self.bd[f'{col}'])),2)
    return resultado['mediana']

def maximo(self,col,resultado):
    resultado['max'] = round(int(np.max(self.bd[f'{col}'])),2)
    return resultado['max']


def minimo(self,col,resultado):
    resultado['min']=round(int(np.min(self.bd[f'{col}'])),2)
    return resultado['min']

def moda(self,col,resultado):
    if self.tipo_coluna[col]=='Numérica':
        resultado['moda'] =int(self.bd[f'{col}'].mode()[0])
        return resultado['moda']
    else:
        resultado['moda'] =self.bd[f'{col}'].mode()[0]
        return resultado['moda']

def desvio_padrao(self,col,resultado):
    resultado['desvio_padrao'] =round(float(np.std(self.bd[f'{col}'])),2)
    return resultado['desvio_padrao']

def variancia(self,col,resultado):
    resultado['variancia'] =round(float(np.var(self.bd[f'{col}'])),2)
    return resultado['variancia']

#def contagem(self,col,resultado):
    resultado['contagem'] = np.unique_counts(self.bd[f'{col}'])

#def frequencia(self,col,resultado):
    resultado['frequencia']= np.unique_values(self.bd[f'{col}'])