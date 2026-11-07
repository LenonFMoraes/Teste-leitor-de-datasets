import plotly.express as pty
import pandas as pd
import plotly.graph_objects as go
import streamlit as st


def teste_grafico(self,coluna):
    fig = pty.histogram(self, x=coluna, nbins=50, marginal='violin',  title='Histograma interativo com boxplot', labels={coluna: coluna.capitalize()}
     , template= 'plotly_white', color_discrete_sequence=['crimson'] )
    fig.update_layout(bargap=0.2)
    (fig.update_traces(box_visible=True, selector={'type': 'violin'}))


    st.plotly_chart(fig, use_container_width=True)

def scatterplot(self,col1,col2,col3):

    if self[col1].size<50000:
        fig = pty.scatter(self,x=col1,y=col2,color=col3, template= 'plotly_white')
        st.plotly_chart(fig, use_container_width=True )
    else:
        amostragem_col_1=self[col1].sample(frac=0.1)
        st.info(amostragem_col_1.count())
        amostragem_col_2=self[col2].sample(frac=0.1)
        st.info(amostragem_col_2.count())
        df_amostras=pd.DataFrame({f"amostras_{col1}":amostragem_col_1, f"amostras_{col2}":amostragem_col_2})
        fig= pty.scatter(df_amostras, x=amostragem_col_1, y=amostragem_col_2,  template= 'plotly_white')
        st.plotly_chart(fig, use_container_width=True)

def scatter_3d(self,col1,col2,col3,alvo):
    hover_config = {col: True for col in self.bd.columns}
    fig2 = pty.scatter_3d(self.bd,x=col1,y=col2,z=col3, color=alvo,  hover_data=hover_config)

    st.plotly_chart(fig2, use_container_width=True)

def histograma_fit(self,coluna,pdf_x,pdf_y):
    fig = pty.histogram(self.bd[coluna], x=coluna, nbins=55, title="Histograma com ajuste de distribuição",  labels={coluna: coluna.capitalize()}, template= 'plotly_white', histnorm='probability density', color_discrete_sequence=['royalblue'] )
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

def boxplot(self,coluna,filtro):
    fig=pty.box(self,filtro,coluna, color=filtro, title='boxplot', template= 'plotly_white', points='all')
    st.plotly_chart(fig, use_container_width=True)

def grafico_linha(self,coluna1,coluna2):
    fig=pty.line(self,coluna1,coluna2, template= 'plotly_white', line_shape= 'linear', color_discrete_sequence=['crimson'])
    st.plotly_chart(fig, use_container_width=True)