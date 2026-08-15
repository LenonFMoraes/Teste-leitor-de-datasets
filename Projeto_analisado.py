import Limpeza_de_dados as Limpeza
import plots
import operações as op
import pandas as pd
import os


arquivos_suportados={'csv','xls','xlsx','feather','json','parquet'}
###lista com extensões de arquivos suportados(meio que, sql's e db ainda precisam de ajuste para importar)



class ProjetoAnalisado: ###classe que utiliza de todos os outros módulos para guardar os dados da análise
    def __init__(self, arquivo):

        self.bd = arquivo   #atributo que vai receber o banco de dados lido pelo pandas
        self.dists={}  #lista para guardar em dicionários os fits de distribuições e os seus parâmetros
        self.resumo_estatistico={}





