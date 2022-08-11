import streamlit as st

with open('style.css') as estilo:
    st.markdown(f'<style>{estilo.read()}</style>', unsafe_allow_html=True)

st.title('Bora congregar?')
st.subheader('Mouss, congrega com nós hoje...')

st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n\n\nSegunda')

col1, col2, col3 = st.columns(3)

with col1:
    with st.form("Roxo Verde"):
        st.markdown("### Roxo Verde")
        st.image("https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80")
        st.form_submit_button('Mais')

with col2:
    with st.form("Lagoinha"):
        st.markdown("### Lagoinha")
        st.image("https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80")
        st.form_submit_button('Mais')

with col3:
    with st.form("Jd Primavera"):
        st.markdown("### Jd Primavera")
        st.image("https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80")
        st.form_submit_button('Mais')

with col1:
    with st.form("b"):
        st.markdown("### Roxo Verde")
        st.image("https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80")
        st.form_submit_button('Mais')

with col2:
    with st.form("a"):
        st.markdown("### Lagoinha")
        st.image("https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80")
        st.form_submit_button('Mais')

with col3:
    with st.form("c"):
        st.markdown("### Jd Primavera")
        st.image("https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80")
        st.form_submit_button('Mais')
