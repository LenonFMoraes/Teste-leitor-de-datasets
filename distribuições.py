import numpy as np
import scipy.stats as sp

import plots
import plots as plot
import streamlit as st





def ajuste(self,distribuicao,coluna):
    distribuicoes={"gamma": sp.gamma,"exponencial":sp.expon, "lognormal": sp.lognorm, "chi²": sp.chi2,}
    if distribuicao in distribuicoes:

        dist=distribuicoes[distribuicao]
        parametros=dist.fit(self.bd[coluna])
        parametros_limpos=[round(float(p),2) for p in parametros]
        nome=f"{distribuicao}¨{coluna}"
        parametros_tela={nome:parametros_limpos}
        self.dists[nome]=parametros
        print(distribuicao)
        print(parametros)
        return self.dists[nome], parametros_tela

def PDF(self,distribuicao,parametros,coluna):
    distribuicoes = {"gamma": sp.gamma.pdf, "exponencial": sp.expon.pdf, "lognormal": sp.lognorm.pdf, "chi²": sp.chi2.pdf, }
    if distribuicao in distribuicoes:
        x=np.linspace(self.bd[coluna].min(),self.bd[coluna].max(),5000)
        d=print(distribuicao)
        s=print(parametros)


        y=distribuicoes[distribuicao](x,*parametros)
        b=print(y.max())
        plots.histograma_fit(self,coluna,x,y)
    return s,d,b




