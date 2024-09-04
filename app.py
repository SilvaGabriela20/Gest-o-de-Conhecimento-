import pandas as pd
import streamlit as st


@st.cache_data
def load_database():
    try:
        df = pd.read_excel('data/base_gabriela.xlsx')
        return df
    except Exception as e:
        st.error(f"Erro ao carregar a base de dados: {e}")
        return None

if 'df' not in st.session_state:
    st.session_state['df'] = load_database()


if st.session_state['df'] is None:
    st.stop()  


if 'dimensao' not in st.session_state:
    st.session_state['dimensao'] = [
        'Customer Name', 'Segment', 'Order Date', 'Ship Date', 
        'Category', 'Sub-Category', 'Product Name', 
        'Country', 'City', 'State', 'Region', 'Postal Code', 'Ship Mode'
    ]

if 'medida' not in st.session_state:
    st.session_state['medida'] = ['Sales', 'Quantity', 'Profit']

if 'agregador' not in st.session_state:
    st.session_state['agregador'] = ['sum', 'mean', 'count', 'min', 'max']

st.title('Gestão de Conhecimento')

pg = st.navigation(
    {
        "Introdução": [
            st.Page(page='introducao/tabela.py', title='Tabela', icon='🏠'),
            st.Page(page='introducao/cubo.py', title='Cubo', icon='📊'),
            st.Page(page='introducao/visualizacoes.py', title='Visualizações', icon='📈')
        ],
    }
)

pg.run()
