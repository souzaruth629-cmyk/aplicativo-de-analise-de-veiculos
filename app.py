import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Dashboard de Vendas de Carros")

car_data = pd.read_csv("vehicles_us.csv")

st.write("✅ Arquivo carregado com sucesso!")
st.write(f"Total de linhas: {len(car_data)}")

hist_button = st.button("Criar histograma")

if hist_button:
    st.write("Criando histograma para o conjunto de dados de anúncios de vendas de carros")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
scatter_button = st.button("Criar gráfico de dispersão")
if scatter_button:
    st.write("Criando gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)






