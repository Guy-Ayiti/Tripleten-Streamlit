
#------------------------------------------------#
#------------------------------------------------#
#------------------------------------------------#
import streamlit as st
import pandas as pd
import plotly.express as px

#================================================#
#                    Bienvenida                  #
#================================================#
st.header("ANALISIS VENTA AUTOS")


#================================================#
#                   Leer Datos                   #
#================================================#
Datos = pd.read_csv("C:/Users/guy3h/Downloads/GitHub/Tripleten-Streamlit/vehicles_us.csv")


#================================================#
#                Desplegar Tabla                 #
#================================================#
st.dataframe(Datos)


#================================================#
#                GRAFICA de BARRAS               #
#             (columnas categoricas)             #
#================================================#
opt = st.radio( label      = "Ver la Grafica de Barra para la Columna siguiente :",
                options    = Datos.select_dtypes(include='object').columns[:-1],
                index      = 0,
                horizontal = True
               )

Tabla = Datos.groupby(opt)['price'].count()
Tabla = pd.DataFrame( { opt:Tabla.index, 'conteo':Tabla.values} )

fig = px.bar( Tabla, x=opt, y='conteo' )
st.plotly_chart( fig, use_container_width=True )


#================================================#
#                    HISTOGRAMAS                 #
#               (columnas numericas)             #
#================================================#
opt_2 = st.radio( label      = "Construir el Histograma para la Columna siguiente :",
                options    = Datos.select_dtypes(include=['int64','float64']).columns,
                index      = 0,
                horizontal = True
               )

binNumb = st.slider('Fijar el numero de Bins', min_value=1, max_value=100, value=10, step=1)

fig = px.histogram( Datos, x=opt_2, nbins=binNumb )
fig.update_traces(marker_line_width=1, marker_line_color="black")

st.plotly_chart(fig, use_container_width=True)
