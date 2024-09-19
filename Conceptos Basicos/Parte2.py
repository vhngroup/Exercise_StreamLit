import streamlit as st
import plotly.express as px
import pandas as pd

#Nombre de la pagina
st.set_page_config(page_title="Curso de uso", page_icon="face_palm", layout="wide", initial_sidebar_state="collapsed")

## initial_sidebar_state="collapsed" Establece el estado inicial del sidebar como colapsado
## initial_sidebar_state="expanded" Establece el estado inicial del sidebar como expandido
## initial_sidebar_state="auto" Establece el estado inicial del sidebar como auto

def main():
    st.title('Parte 2 de uso Streamlit')
    st.sidebar.header("Ejemplo de Sidebar") #Agregamos un siderbar
    df = pd.read_csv('./Static/Employee Attrition.csv')
    st.write("Mostramos el Data Frame")
    st.dataframe(df, height=100)
    df_count = df.groupby('dept').count().reset_index() #Contamos por departamento
    #Usamos una grafica de tortas, contamos los ID y segmentamos por departamento
    fig = px.pie(df_count, values="Emp ID", names="dept", title="Empleados por Departamento")
    st.write("Usamos grafica de tortas")
    st.plotly_chart(fig, use_container_width=True) #Graficamos
    st.write("Usamos grafica de barrras")
    df_avg = df.groupby('dept')['Work_accident'].mean().reset_index() #Media por departamento del nivel de satisfaccion
    fig2 = px.bar(df_avg, x="dept", y="Work_accident", color="dept", title="Media de Nivel de Satisfaccion por Departamento")
    st.plotly_chart(fig2, use_container_width=True) #Graficamos
    st.write("Mostramos grafica de lineas")
    df_line = df.groupby('dept')['average_montly_hours'].mean().reset_index() #Media por departamento del nivel de satisfaccion
    fig3 = px.line(df_line, x="dept", y="average_montly_hours",  title="Media de horas de trabajo al mes por departamento")
    st.plotly_chart(fig3, use_container_width=True) #Graficamos
    #st.line_chart(df.groupby('dept')['number_project'])

    

if __name__=='__main__':
    main()