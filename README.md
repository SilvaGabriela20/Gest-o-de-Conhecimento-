# Aula 07 - Avaliação

## Objetivos

1. Encontrar uma base de dados e descrever as colunas.
2. Classificar as colunas da base de dados conforme o modelo multidimensional (4W1H).
3. Implementar um cubo na base escolhida.
4. Implementar os 4 tipos de visualizações na base de dados.
5. Descrever 2 rotinas para cada tipo de análise de dados implementada na base escolhida.

## 1. Base de Dados

**Nome:** Superstore (Loja de Varejo)

**Descrição:** Conjunto de dados de vendas de uma empresa, contendo informações detalhadas sobre pedidos, clientes e produtos.

**Colunas:**

1. **Row ID:** Identificador único para cada linha de dados.
2. **Order ID:** Código exclusivo que identifica um pedido.
3. **Order Date:** Data em que o pedido foi realizado.
4. **Ship Date:** Data em que o pedido foi enviado.
5. **Ship Mode:** Método ou tipo de envio usado para a entrega (ex.: Padrão, Expresso).
6. **Customer ID:** Identificador único para o cliente.
7. **Customer Name:** Nome completo do cliente que fez o pedido.
8. **Segment:** Categoria de cliente, como "Consumidor", "Corporativo", etc.
9. **Country:** País de onde o pedido foi feito.
10. **City:** Cidade onde o pedido foi realizado.
11. **State:** Estado ou província associado ao endereço do cliente.
12. **Postal Code:** Código postal associado ao endereço de entrega.
13. **Region:** Região geográfica onde o cliente está localizado.
14. **Product ID:** Identificador exclusivo para cada produto.
15. **Category:** Categoria à qual o produto pertence (ex.: Móveis, Tecnologia).
16. **Sub-Category:** Subcategoria mais específica do produto (ex.: Cadeiras, Computadores).
17. **Product Name:** Nome ou descrição do produto.
18. **Sales:** Valor total de vendas associado ao pedido.

## 2. Classificação das Colunas (Modelo Multidimensional 4W1H)

- **Who (Quem):** Customer Name, Segment
- **When (Quando):** Order Date, Ship Date
- **What (O que):** Category, Sub-Category, Product Name
- **Where (Onde):** Country, City, State, Region, Postal Code
- **How (Como):** Ship Mode
- **Medidas (Fatos):** Sales, Quantity, Profit

## 3. Implementação do Cubo

O arquivo `cubo.py` foi implementado e ajustado para se adequar à base escolhida.

**Exemplo do Cubo:** [Captura de tela do cubo](#)

**Código:** [cubo.py no GitHub](https://github.com/SilvaGabriela20/Gest-o-de-Conhecimento-/blob/a995580adfcd4321947ee9a58a6772bf39a34689/cubo.py)

## 4. Implementação dos 4 Tipos de Visualizações

**Código:** [visualizacoes.py no GitHub](https://github.com/SilvaGabriela20/Gest-o-de-Conhecimento-/blob/27f0da71c01c137a83cbe8d423a197b4df4b9724/visualizacoes.py)

1. **Gráfico de Linha (Line Chart):** Visualiza a soma das vendas (Sales) ao longo do tempo, agrupando por mês. Usado para mostrar tendências temporais.
2. **Gráfico de Barras (Bar Chart):** Exibe o lucro (Profit) por sub-categoria (Sub-Category). Útil para comparar diferentes categorias de dados.
3. **Gráfico de Pizza (Pie Chart):** Mostra a distribuição das vendas (Sales) por segmento (Segment). Usado para visualizar proporções de cada segmento.
4. **Gráfico de Área (Area Chart):** Exibe o crescimento cumulativo das vendas ao longo do tempo. Usado para mostrar o acúmulo de vendas ao longo do período.

## 5. Rotinas de Análise de Dados

### Gráfico de Linha (Tendências Temporais)

- **Rotina 1: Análise de vendas mensais ao longo do tempo**
  - **Objetivo:** Identificar flutuações nas vendas ao longo dos meses para determinar sazonalidades ou tendências de crescimento/declínio.
  - **Uso:** Exibe um gráfico de linha para mostrar como as vendas mudam ao longo dos meses ou anos, permitindo identificar picos e quedas de vendas.

- **Rotina 2: Comparação de vendas entre anos**
  - **Objetivo:** Comparar o desempenho de vendas entre diferentes anos para avaliar o crescimento anual.
  - **Uso:** Gráficos de linha com múltiplos anos sobrepostos, ajudando a avaliar como as vendas evoluíram em períodos anuais e identificar possíveis anomalias.

### Gráfico de Barras (Comparações Categóricas)

- **Rotina 1: Comparação de lucro por sub-categoria de produto**
  - **Objetivo:** Visualizar o lucro gerado por cada sub-categoria de produto para identificar os produtos mais lucrativos.
  - **Uso:** Gráficos de barras ajudam a comparar o desempenho de diferentes sub-categorias e fornecer insights sobre quais áreas devem ser priorizadas.

- **Rotina 2: Comparação de vendas entre regiões**
  - **Objetivo:** Comparar o volume de vendas em diferentes regiões para identificar áreas geográficas com melhor desempenho.
  - **Uso:** Um gráfico de barras pode mostrar claramente quais regiões estão gerando mais receita, auxiliando na tomada de decisões estratégicas.

### Gráfico de Pizza (Distribuição Proporcional)

- **Rotina 1: Distribuição de vendas por segmento de clientes**
  - **Objetivo:** Entender qual segmento de clientes (por exemplo, consumidor, corporativo) está gerando mais vendas.
  - **Uso:** O gráfico de pizza permite ver de forma clara a proporção de vendas que cada segmento representa, ajudando na segmentação de marketing.

- **Rotina 2: Análise da distribuição de vendas por categorias de produto**
  - **Objetivo:** Identificar a participação de cada categoria (móveis, tecnologia, etc.) nas vendas totais.
  - **Uso:** Gráficos de pizza permitem visualizar rapidamente qual categoria de produto contribui mais para as vendas totais.

### Gráfico de Área (Acumulação ao Longo do Tempo)

- **Rotina 1: Crescimento cumulativo das vendas ao longo do tempo**
  - **Objetivo:** Monitorar o crescimento das vendas ao longo dos meses ou anos para visualizar o acúmulo total.
  - **Uso:** O gráfico de área pode mostrar a acumulação contínua de vendas, fornecendo insights sobre o ritmo de crescimento da empresa.

- **Rotina 2: Crescimento cumulativo do lucro**
  - **Objetivo:** Avaliar o lucro acumulado ao longo do tempo e verificar se ele está em crescimento constante.
  - **Uso:** O gráfico de área permite visualizar o crescimento do lucro acumulado, o que pode ser útil para decisões financeiras e projeções de longo prazo.




