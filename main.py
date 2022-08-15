import streamlit as st
import cultos
from informacoes import inforComuns
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

with open('style.css') as estilo:
    st.markdown(f'<style>{estilo.read()}</style>', unsafe_allow_html=True)

st.header('Bora congregar?')
st.write('A paz de Deus meus irmãos! A relação com os dias de culto está logo abaixo, porém, antes, gostaria de esclarecer algumas coisas sobre esse projeto. Esta não é uma aplicação oficial da CCB, é apenas um projeto solo meu, que tem como único objetivo de facilitar a visualização dos dias de culto. O projeto está em fase de crescimento, e quaisquer idéias dão bem vindas. Qualquer dúvida/sugestão, estou a disposição. Deus abençoe, e bora congregar meus companheiros(as).')

# Menu top
with st.sidebar:
    menuFalso = option_menu(menu_title='',options=[''])
    menuFalso
menu = option_menu(
    menu_title= None,
    options=['Culto', 'Ensaios', 'Batismos', 'Santas Seias'],
    icons=['journal-bookmark-fill', 'music-note', 'water','droplet-fill'],
    menu_icon='cast',
    default_index=0,
    orientation='horizontal',
    styles={
        "nav-link": {"font-size": "0px",
        "margin-right": "0px !important"},
        "icon": {"margin":"0px"}
    }
)

if menu:
    cultos.ativar()

st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')