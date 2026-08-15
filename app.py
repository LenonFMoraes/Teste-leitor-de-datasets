from streamlit.testing.v1.element_tree import Title

import Projeto_analisado
import streamlit as st
import plots
import pandas as pd


main_page= st.Page("Home.py", title="Página inicial")
pag2=st.Page("pag2.py", title="Tratamento de dados")
pag3=st.Page("Plots e Stats.py", title="Plots")
pag4=st.Page("Pag Distribuições.py", title="Teste com distribuições")

pg=st.navigation({'Página inicial':[main_page],
'ferramentas':[pag2,pag3,pag4]})
pg.run()
# 1. Título e textos (aceita Markdown!)



# 2. Criar uma caixinha de seleção na barra lateral
