import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd

# Corrigir o caminho do arquivo para usar o caminho onde ele foi salvo após o upload anterior
file_path = '/mnt/data/base_gabriela.xlsx'  # Caminho do arquivo previamente salvo

# Carregar os dados da planilha
df = pd.read_excel(file_path)

# Definir as colunas de medidas e dimensões com base nos dados da sua planilha
st.session_state['df'] = df
st.session_state['dimensao'] = ['Segment', 'Country', 'City', 'Category', 'Sub-Category']  # Dimensões
st.session_state['dimensao_tempo'] = ['Order Date', 'Ship Date']  # Dimensões temporais
st.session_state['medida'] = ['Sales']  # Medidas numéricas

# Verificar se todas as colunas estão presentes no dataframe
try:
    selected_columns = st.session_state['dimensao'] + st.session_state['dimensao_tempo'] + st.session_state['medida']
    df_selected = st.session_state['df'][selected_columns]
    
    # Renderizar usando Pygwalker com as colunas selecionadas
    pyg_app = StreamlitRenderer(df_selected)

except KeyError as e:
    st.error(f"Coluna não encontrada no dataframe: {e}")
