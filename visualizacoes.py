import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Certificando-se de que a base de dados está carregada
if 'df' not in st.session_state:
    st.error("A base de dados não foi carregada corretamente.")
else:
    df = st.session_state['df']

    # Convertendo 'Order Date' para datetime, com erro=coerce para valores inválidos
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

    # Título da página
    st.title('Visualizações')

    # Filtro de categoria
    category_filter = st.selectbox("Selecione uma categoria:", df['Category'].unique())

    # Filtrando a base de dados pela categoria selecionada
    filtered_data = df[df['Category'] == category_filter]

    # Verificação se há dados filtrados
    if filtered_data.empty:
        st.write("Nenhum dado disponível para a categoria selecionada.")
    else:
        # Verificando se a coluna 'Order Date' foi convertida corretamente
        if 'Order Date' in filtered_data.columns and pd.api.types.is_datetime64_any_dtype(filtered_data['Order Date']):
            # Gráfico de Linha - Vendas ao longo do tempo
            st.subheader('Vendas ao longo do tempo')
            sales_over_time = filtered_data.groupby(filtered_data['Order Date'].dt.to_period('M'))['Sales'].sum()
            st.line_chart(sales_over_time)
        else:
            st.write("A coluna 'Order Date' não contém valores válidos de data.")

        # Gráfico de Barras - Lucro por Sub-Categoria
        st.subheader('Lucro por Sub-Categoria')
        profit_by_sub_category = filtered_data.groupby('Sub-Category')['Profit'].sum()
        st.bar_chart(profit_by_sub_category)

        # Gráfico de Pizza - Distribuição de Vendas por Segmento
        st.subheader('Distribuição de Vendas por Segmento')
        sales_by_segment = filtered_data.groupby('Segment')['Sales'].sum()
        fig, ax = plt.subplots(figsize=(6, 6))
        sales_by_segment.plot.pie(autopct="%1.1f%%", ax=ax)
        st.pyplot(fig)

        # Gráfico de Área - Crescimento cumulativo das Vendas
        st.subheader('Crescimento cumulativo das Vendas')
        cumulative_sales = sales_over_time.cumsum()
        st.area_chart(cumulative_sales)
