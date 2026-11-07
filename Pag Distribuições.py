import streamlit as st
import distribuições as dist


st.info("Nesta página você pode ajustar uma distribuição teórica(gamma,normal e etc em uma coluna específica)")

if 'PA' in st.session_state:
    PA=st.session_state['PA']
    numericas=[]
    for n in PA.tipo_coluna:
        if PA.tipo_coluna[n] =="Numérica":
            numericas.append(n)

    alvo=st.selectbox("Escolha a coluna alvo", options=numericas)
    mapa={"gamma":'gamma', "lognormal": 'logn',
    "chi²":'chi2', "exponencial": "expon",}
    distribuicao=st.select_slider("Escolha a distribuição desejada", options=mapa.keys(),format_func=lambda x: mapa[x])
    parametros_tela=dist.ajuste(PA,distribuicao,alvo)
    st.info(f"Parâmetros estimados:{parametros_tela[1]}")

    st.subheader(f"Ajustar a curva teórica ao histograma da coluna")
    ajustes_col_alvo=[]
    for nome_dists in PA.dists:
        if alvo in nome_dists:
            ajustes_col_alvo.append(nome_dists)
    ajuste=st.selectbox("Escolha entre as distribuições(Caso tenha calculado mais de uma)", options=ajustes_col_alvo )
    if ajuste is not None:
        chave=ajuste.split('¨')
        chave_dist=chave[0]
        #st.info(f"Chave:{chave_dist}")
        chave_col=chave[1]
        #st.info(f"Chave:{chave_col}")

        parametros=PA.dists[ajuste]
        arrendondados=[float(round(p,2)) for p in parametros]
        st.info(f"Parâmetros estimados:{ arrendondados}")
        dist.PDF(PA,chave_dist,PA.dists[ajuste],chave_col)



else:st.warning('Carregue o dataset por favor')
