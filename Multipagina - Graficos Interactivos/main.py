import streamlit as st
import pandas as pd
import plotly.express as px

def pagina_Principal():
    st.title("Este es el Home")
    st.write("Usa el menu de navegación izquierdo")

def pagina_Datos():
    st.title("Página de Datos")
    st.write("Carga un archivo CSV para visualiar los datos")
    archivo_Cargado = st.file_uploader("Selecciona un archivo CSV", type=["csv"])
    if archivo_Cargado is not None:
        df = pd.read_csv(archivo_Cargado, sep=";", on_bad_lines='skip')
        st.write("Datos del archivo cargados")
        st.dataframe(df)
        st.write("Estadisticas descriptivas")
        st.write(df.describe())

def pagina_Graficos():
    st.title("Página de Gráficos")
    st.write("Carga un archivo CSV para crear gráficos interactivos")
    #Key es para que no cuando lo queramos usar, se pueda invocar y se se realacione con el otro cargador
    archivo_Cargado = st.file_uploader("Selecciona un archivo CSV", type=["csv"], key="2")
    if archivo_Cargado is not None:
        df = pd.read_csv(archivo_Cargado, sep=";", on_bad_lines='skip') 
        st.write("Seleciona una columna para el eje X")
        eje_x = st.selectbox("Eje X", df.columns)
        st.write("Seleciona una columna para el eje Y")
        eje_y = st.selectbox("Eje y", df.columns)
        if st.button("Generar gráfico"):
            st.write("Gráficos interactivos")
            fig =px.bar(df, x=eje_x, y=eje_y, title=f"Gráfico de barras {eje_x} vs {eje_y}")
            st.plotly_chart(fig)
            fig2 =px.scatter(df, x=eje_x, y=eje_y, title=f"Gráfico de dispersión {eje_x} vs {eje_y}")
            st.plotly_chart(fig2)
            fig3=px.line(df, x=eje_x, y=eje_y, title=f"Gráfico de líneas {eje_x} vs {eje_y}")
            st.plotly_chart(fig3)
            df_line = df.groupby(eje_y)[eje_x].mean().reset_index() 
            fig4 = px.line(df_line, x=eje_x, y=eje_y,  title=f"Media de precio por {eje_x}")
            st.plotly_chart(fig4, use_container_width=True) 
            df_count = df.groupby(eje_y).count().reset_index() 
            fig5 = px.pie(df_count, values=eje_x, names=eje_y, title=f"Agrupamos las marcas y contamos {eje_x}")
            st.plotly_chart(fig5, use_container_width=True) 

st.sidebar.title("Menu de Navegación")
st.write("------------------------------------------------------------")
pagina = st.sidebar.selectbox("Selecciona Pagina", ["Página de Inicio", "Pestaña de Datos", "Pestaña de Gráficos"])
if pagina == "Página de Inicio":
    pagina_Principal()
elif pagina == "Pestaña de Datos":
    pagina_Datos()
elif pagina == "Pestaña de Gráficos":
    pagina_Graficos()   