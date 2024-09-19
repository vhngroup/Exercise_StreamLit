import streamlit as st
from rembg import remove
import os
from PIL import Image

def save_uploaded_file(uploaded_file):
    upload_dir = "uploads"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    file_path = os.path.join(upload_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer()) #Guaradmos archivo en buffer
    return file_path

def run_background_removal(input_image_file):
    input_image_path = save_uploaded_file(input_image_file)
    output_img_path = input_image_path.replace('.', '_rmbg.').replace('jpg', 'png').replace('jpeg', 'png')
    try:
        image = Image.open(input_image_path) #Abrimos la imagen  original
        output = remove(image) #Aplicamos el algoritmo para remover el fondo
        output.save(output_img_path, "PNG") #Guardamos la imagen procesada sin fondo
        st.success("Imagen procesada con exito")
        col1, col2 = st.columns(2) # Creamos dos columnas y las mostramos
        with col1:
            st.header("Imagen original") #Se trata del Input
            st.image(input_image_path, caption="Imagen original")
            with open(input_image_path, "rb") as img_file:
                st.download_button(
                    label="Descargar imagen original",
                    data=img_file,
                    file_name=os.path.basename(input_image_path),
                    mime="image/jpeg",
                )
        with col2:
            st.header("Imagen procesada") #Se trata del Output
            st.image(output_img_path, caption="Fondo removido")
            with open(output_img_path, "rb") as img_file:
                st.download_button(
                    label="Descargar imagen procesada",
                    data=img_file,
                    file_name=os.path.basename(output_img_path),
                    mime="image/png",
                )

        st.success("Fondo removido Exitosamente")
    except Exception as e:
        st.error(e)

def main():
    st.set_page_config(page_title="Removedor de Fondo", page_icon="🎨")
    st.title("Removedor de Fondo")
    uploaded_file = st.file_uploader("Subir imagen", type=["jpg", "jpeg", "png"]) #Se trata del Input con los archivos soportados
    if uploaded_file is not None: #Validamos que el archivo no este vacio
        run_background_removal(uploaded_file)

if __name__ == "__main__":
    main()


