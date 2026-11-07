import plotly.express as pty
import streamlit as st
import numpy as np
from statsmodels.graphics.tsaplots import acf, pacf
from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.stats.diagnostic import acorr_ljungbox



def diff(y,lag):
    novo_valor=y.diff(lag)
    return novo_valor



def plot_serie(self,x,y):
    fig=pty.line(self.bd,x,y, template='plotly_white',title='Plot da serie', color_discrete_sequence=['red'])

    st.plotly_chart(fig, use_container_width=False)


def acf_plot(y,lag):
    valor_acf,conf=acf(y.dropna(),nlags=lag,alpha=0.05)
    banda_inferior=conf[:,0]-valor_acf
    banda_superior=conf[:,1]-valor_acf
    fig=pty.bar(x=np.arange(len(valor_acf)),y=valor_acf,labels={"x": "Lags", "y": "Autocorrelação"},
    title="ACF", color_discrete_sequence=['red'])
    fig.update_layout(
        yaxis=dict(range=[-1.1, 1.1])
    )

    fig.add_hrect(
        y0=banda_inferior[1], y1=banda_superior[1],fillcolor='rgba(246, 158, 73, 1)', line_width=0, layer="below",
    )
    st.plotly_chart(fig, use_container_width=True)


def pacf_plot(y,lag):
    valor_pacf,conf=pacf(y.dropna(),nlags=lag, method='ywm',alpha=0.05)
    banda_inferior = conf[:, 0] - valor_pacf
    banda_superior = conf[:, 1] - valor_pacf
    fig=pty.bar(x=np.arange(len(valor_pacf)),y=valor_pacf,labels={'x': 'lags', 'y': 'Autocorrelação Parcial'},title='PACF', color_discrete_sequence=['red'])
    fig.update_layout(
        yaxis=dict(range=[-1.1, 1.1])
    )

    fig.add_hrect(
        y0=banda_inferior[1], y1=banda_superior[1], fillcolor='rgba(246, 158, 73, 1)', line_width=0, layer="below",
    )
    st.plotly_chart(fig, use_container_width=True)

def adfuller(x):
    ad=adfuller(x.dropna())
    return ad

def kpss(x):
    kp=kpss(x.dropna(), regression='c', nlags='auto')
    return kp

