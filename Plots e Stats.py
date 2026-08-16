import streamlit as st
from Projeto_analisado import ProjetoAnalisado
import plots

if 'PA' in st.session_state:
    PA=st.session_state['PA']

    coluna_selecionada = st.sidebar.selectbox(
        "Escolha a coluna para analisar:",options=PA.bd.columns)
    st.subheader('Histograma e métricas da coluna')
    plots.teste_grafico(PA.bd,coluna_selecionada)
    ##separando as métricas em colunas para melhor visualização
    if PA.tipo_coluna[f'{coluna_selecionada}']=='Numérica':
        cols=st.columns([1,1,1])
        cols[0].metric(label=f"Média de {coluna_selecionada}", value=PA.resumo_estatistico[coluna_selecionada]['media'])
        cols[0].metric(label=f"Mediana de {coluna_selecionada}", value=PA.resumo_estatistico[coluna_selecionada]['mediana'])
        cols[2].metric(label=f"Valor maximo da coluna {coluna_selecionada}", value=PA.resumo_estatistico[coluna_selecionada]['max'])
        cols[2].metric(label=f"Valor mínimo da coluna {coluna_selecionada}", value=PA.resumo_estatistico[coluna_selecionada]['min'])
        cols[1].metric(label=f"Moda de {coluna_selecionada}", value=PA.resumo_estatistico[coluna_selecionada]['moda'])
        cols[1].metric(label=f"Desvio Padrão de {coluna_selecionada}", value=PA.resumo_estatistico[coluna_selecionada]['desvio_padrao'])
        cols[1].metric(label=f"Variância de {coluna_selecionada}", value=PA.resumo_estatistico[coluna_selecionada]['variancia'])

    else:
        cols = st.columns([1, 1, 1])
        cols[0].metric(label=f"Moda de {coluna_selecionada}", value=PA.resumo_estatistico[coluna_selecionada]['moda'])
        st.info('Coluna de Strings não tem como tirar média, desvio padrão e variancia')



    ###Scatter plot3d interativo
    plot=st.selectbox('Outros plots', options=['Opções', 'Scatter plot', 'Histograma com filtros', 'Scatter 3d', 'Charts', 'Pizza', 'Boxplot'])
    if plot=="Scatter 3d":
        st.subheader('Scatter plot 3d')
        with st.container(horizontal=True):
            col1=st.selectbox('Primeira coluna', options=PA.bd.columns, width=100)
            col2=st.selectbox('Segunda coluna', options=PA.bd.columns,width=100)
            col3=st.selectbox('Terceira coluna', options=PA.bd.columns ,width=100)
            alvo=st.selectbox('Coluna alvo', options=PA.bd.columns,width=100)

        plots.scatter_3d(PA,col1,col2,col3,alvo)
        st.info("Modo de uso: escolha as colunas 1,2,3 como eixos para visualizar e a coluna alvo para colorir os dados, caso o alvo seja uma coluna numérica os dados serão coloridos por um gradiente indo de azul a branco,"
                "se for categórica o scatter separa uma cor pra cada categoria e gera uma legenda no canto com cada uma, o usuário pode usar essa legenda para filtrar os dados também caso queira(apenas se alvo for coluna categórica)")

    elif plot=='Histograma com filtros':
        st.subheader('Histograma com filtros')
        col1=st.selectbox(label='Coluna alvo', options=PA.bd.columns, width=100)
        col2=st.selectbox('Coluna Filtro', options=PA.bd.columns, width=100 )

        plots.histograma_filtro(PA.bd,col1,col2)

    elif plot=='Pizza':
        st.subheader('Gráfico de Pizza')
        col1=st.selectbox('Coluna alvo', options=PA.bd.columns, width=100)
        col2=st.selectbox('Coluna Filtro', options=PA.bd.columns, width=100)

        plots.grafico_pizza(PA.bd,col1,col2)

    elif plot=='Boxplot':
        st.subheader('Boxplot')
        col1=st.selectbox('Coluna alvo', options=PA.bd.columns, width=100)
        col2=st.selectbox('Coluna Filtro', options=PA.bd.columns, width=100)
        plots.boxplot(PA.bd,col1,col2)
else:
    st.info('Faça upload do seu dataframe na página principal para liberar as opções desta página')


