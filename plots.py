import plotly.express as pty
import plotly.graph_objects as go
import streamlit as st
from plotly.express import density_map


def teste_grafico(self,coluna):
    fig = pty.histogram(self, x=coluna, nbins=50, marginal='violin',  title='Histograma interativo com boxplot', labels={coluna: coluna.capitalize()}
     , template= 'plotly_white', )
    fig.update_layout(bargap=0.2)
    (fig.update_traces(box_visible=True, selector={'type': 'violin'}))


    st.plotly_chart(fig, use_container_width=True)

def scatter_3d(self,col1,col2,col3,alvo):
    hover_config = {col: True for col in self.bd.columns}
    fig2 = pty.scatter_3d(self.bd,x=col1,y=col2,z=col3, color=alvo,  hover_data=hover_config)

    st.plotly_chart(fig2, use_container_width=True)

def histograma_fit(self,coluna,pdf_x,pdf_y):
    fig = pty.histogram(self.bd[coluna], x=coluna, nbins=55, title="Histograma com ajuste de distribuição",  labels={coluna: coluna.capitalize()}, template= 'plotly_white', histnorm='probability density', )
    fig.update_layout(bargap=0.1)
    fig.add_trace(go.Scatter (x=pdf_x,
                              y=pdf_y,
                              name='Curva teórica aplicada ao histograma',
                              mode='lines',
                              ))



    st.plotly_chart(fig, use_container_width=True)

def histograma_filtro(self,coluna,filtro):
    fig=pty.histogram(self,x=coluna, color=filtro, nbins=50, template= 'plotly_white', title='histograma com filtragem')
    fig.update_layout(bargap=0.1)
    st.plotly_chart(fig, use_container_width=True)

def grafico_pizza(self,coluna,filtro):
    fig=pty.pie(self, values=coluna, color=filtro, title='grafico de pizza', template= 'plotly_white')
    st.plotly_chart(fig, use_container_width=True)
