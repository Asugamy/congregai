import streamlit as st
from informacoes import inforComuns
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

with st.sidebar:
    choose = option_menu("App Gallery", ["About", "Photo Editing", "Project Planning", "Python e-Course", "Contact"],
                         icons=['house', 'camera fill', 'kanban', 'book','person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

with open('style.css') as estilo:
    st.markdown(f'<style>{estilo.read()}</style>', unsafe_allow_html=True)

st.title('Bora congregar?')
st.subheader('Mouss, congrega com nós hoje...')

st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
dia = st.selectbox(
     'Escolha um dia:',
     ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado')
)

col1, col2, col3 = st.columns(3, gap="small")

igrejas = {
    'Domingo':['', 'Central', 'Cidade Indsutrial', 'José Carlos de Lima', 'Delfino', 'Independência', 'Jd Primavera', 'Major Prates', 'Maracanã', 'Morrinhos', 'Nova América', 'Renascença', 'Roxo Verde', 'Sagrada Família', 'Santa Rafaela', 'Santo Amaro', 'São Judas', 'Vila Atlântida', 'Vila Áurea II', 'Vila Sion', 'Village do Lago'],

    'Segunda':['', 'Esplanada', 'Edgar Pereira', 'Interlagos', 'Jaraguá', 'Santo Antônio II','Vila Anália', 'Vila Atlântida','Castelo Branco'],

    'Terça':['', 'Vila Oliveira',   'Cidade Indsutrial', 'José Carlos de Lima', 'Delfino', 'Independência', 'Jd Alegre', 'Jd Eldorado', 'Major Prates', 'Morrinhos', 'Planalto', 'Renascença', 'Vila Antônio Narciso', 'Vila Oliveira', 'Vila Sion', 'Village do Lago'],

    'Quarta':['', 'Central'],

    'Quinta':['', 'Alto São João', 'Carmelo', 'Cidade Indsutrial', 'Esplanada', 'Independência', 'Jd Brasil', 'Jd Primavera', 'Maracanã', 'Monte Sião', 'Roxo Verde', 'Santo Amaro', 'São Geraldo II', 'São Judas', 'Vila Anália', 'Castelo Branco', 'Vila Oliveira', 'Vila Sion'],

    'Sexta':['', 'Jd Alvorada', 'José Carlos de Lima', 'Delfino', 'Interlagos', 'Jd Eldorado', 'Sagrada Família', 'Santa Rafaela', 'Santo Antônio II', 'Vila Atlântida'],

    'Sábado':['', 'Alto São João', 'Carmelo', 'Edgar Pereira', 'Esplanada', 'Jaraguá', 'Jd Alegre', 'Jd Brasil', 'Jd Primavera', 'Monte Sião', 'Nova América', 'Planalto', 'Renascença', 'Roxo Verde', 'São Bento', 'São Geraldo II', 'Vila Anália', 'Vila Áurea II', 'Castelo Branco', 'Vila Oliveira', 'Village do Lago']
}
comum = igrejas[dia]

def card():
    for i in range (1,len(comum)):
        imagem = inforComuns(comum[i])[3]
        if i % 3 == 0:
            with col3:
                with st.form(str(i)):
                    st.markdown(f"### {comum[i]}")
                    st.image(f'{imagem}')
                    st.form_submit_button('Mais')
        elif i % 2 == 0 or dia == 'Quarta':
            with col2:
                with st.form(str(i)):
                    st.markdown(f"### {comum[i]}")
                    st.image(f"{imagem}")
                    st.form_submit_button('Mais')

        else:
            with col1:
                with st.form(str(i)):
                    st.markdown(f"### {comum[i]}")
                    st.image(f"{imagem}")
                    st.form_submit_button('Mais')

card()