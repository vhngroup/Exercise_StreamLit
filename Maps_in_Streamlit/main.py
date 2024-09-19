import folium
import streamlit as st
from IPython.display import display


st.set_page_config(
    page_title="Maps in streamlit",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None,
)

#Coordinates for NewYork
map_center = [40.7128, -74.0060]
mymap = folium.Map(location=map_center, zoom_start=12)

folium.Marker(
    map_center, popup="VHNGROUP", tooltip="VHNGROUP",
    icon=folium.Icon(color="blue", icon="info-sign")
).add_to(mymap)

st.header("VHNGROUP Location in New York", divider=True)
st.components.v1.html(folium.Figure().add_child(mymap).render(), height=500)