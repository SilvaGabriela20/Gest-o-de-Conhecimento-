import streamlit as st
import pandas as pd
from datetime import datetime

# Certificando-se de que a base de dados está carregada
if 'df' not in st.session_state:
    st.error("A base de dados não foi carregada corretamente.")
else:
    df = st.session_state['df']

    # Convertendo a coluna 'Order Date' para o formato datetime, especificando o formato ou usando dayfirst
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

    # Encontrando o valor mínimo e máximo da coluna de datas para o filtro
    min_date = df['Order Date'].min().date()  # Convertendo para tipo date
    max_date = df['Order Date'].max().date()  # Convertendo para tipo date

    # Aplicando o filtro de data com o valor mínimo e máximo definidos
    order_date_filter = st.date_input(
        "Selecione a data do pedido:",
        value=min_date,  # Valor padrão
        min_value=min_date,  # Definindo o valor mínimo
        max_value=max_date   # Definindo o valor máximo
    )

    # Filtrando o dataframe com base na data selecionada
    filtered_data = df[df['Order Date'].dt.date == order_date_filter]

    # Exibindo o dataframe filtrado
    st.dataframe(filtered_data)
