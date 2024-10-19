
#------------------------------------------------#
#------------------------------------------------#
#------------------------------------------------#
import streamlit as st
import pandas as pd
import plotly.express as px


#================================================#
#                 Leer archivo                   #
#================================================#
Datos = pd.read_csv("vehicles_us.csv")


#================================================#
#                    Streamlit                   #
#================================================#
st.header("EXAMPLE OF STREAMLIT APP")
st.write("Ejemplo de Aplicacion en Streamlit")


#-------------------HISTOGRAMA-------------------#
histButton = st.button("Desplegar Histograma:")

if histButton:
    # desplegar un Mensaje en la aplicacion
    st.write("Histograma de visualizacion de los datos de venta de Autos")

    # crear un histograma
    fig = px.histogram(Datos, x="odometer")

    # grafica interactiva en Plotly
    st.plotly_chart(fig, use_container_width=True)



#--------------GRAFICA DISPERSION-----------------#
dispButton = st.Button("Desplegar Grafica de Dispersion:")

if dispButton:
    # desplegar un Mensaje en la aplicacion
    st.write("Grafica de Dispersion relativa a los datos")

    # crear un histograma
    fig = px.scatter(Datos, x="odometer", y="price")

    # grafica interactiva en Plotly
    st.plotly_chart(fig, use_container_width=True)

    