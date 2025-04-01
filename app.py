# import necessary libraries
import os
from PIL import Image
from pdf2image import convert_from_path
import rembg
import io
import streamlit as st

# functions to handle file upload, conversion, and background removal
def save_uploaded_file(uploaded_file, folder="uploads"):
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def convert_image(file_path, output_format):
    img = Image.open(file_path)
    
    output_format = output_format.upper()

    # If is 'JPG' convert to 'JPEG'
    if output_format == 'JPG':
        output_format = 'JPEG'

    output_file = file_path.rsplit(".", 1)[0] + f".{output_format}"
    
    # Save image and use the correct format
    img.save(output_file, format=output_format)
    return output_file

def convert_pdf_to_images(file_path, output_format="png"):
    images = convert_from_path(file_path)
    output_files = []
    for i, img in enumerate(images):
        output_file = f"{file_path.rsplit('.', 1)[0]}_{i}.{output_format}"
        img.save(output_file, format=output_format.upper())
        output_files.append(output_file)
    return output_files

def remove_background(file_path):
    input_image = Image.open(file_path)
    output_image = rembg.remove(input_image)
    output_file = file_path.rsplit(".", 1)[0] + "_no_bg.png"
    output_image.save(output_file, format="PNG")
    return output_file


st.set_page_config(
    page_title="Img Converter App",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/eudesgccunha/',
        'Report a bug': "https://github.com/eudesgccunha/image-converter/issues",
        'About': "# This is a free cool app! Clone or Fork it on GitHub!"
    }
)

# Run the Streamlit app
st.title("Image Converter")

# Cabeçalho de uma seção
st.header('Um projeto inteiramente grátis utilizando Streamlit')
st.write("Aqui você pode converter imagens e PDFs para diferentes formatos bem como remover o fundo das imagens. \n Os seguinte formato de arquivo são suportados: jpg, jpeg, png, pdf, webp, tiff, e tif.")

st.write(' --- ')

# subtítulo
st.subheader('Carregar arquivos')

# texto simples
st.text('Selecione seus arquivos para conversão.')


uploaded_files = st.file_uploader("", type=["jpg", "jpeg", "png", "pdf", "webp", "tif", "tiff"], accept_multiple_files=True)

if uploaded_files:
    output_format = st.selectbox("Escolha o formato de conversão", ["jpg", "jpeg", "png", "pdf", "webp", "tif", "tiff"])
    remove_bg = st.checkbox("Remover Background")
    converted_files = []
    
    for uploaded_file in uploaded_files:
        file_path = save_uploaded_file(uploaded_file)
        
        if uploaded_file.type == "application/pdf":
            converted_files.extend(convert_pdf_to_images(file_path, output_format))
        else:
            converted_file = convert_image(file_path, output_format)
            if remove_bg:
                converted_file = remove_background(converted_file)
            converted_files.append(converted_file)
    
    st.success("Conversão concluída!")
    
    # Display the converted files for download
    for converted_file in converted_files:
        with open(converted_file, "rb") as f:
            st.download_button("Baixar " + os.path.basename(converted_file), f, file_name=os.path.basename(converted_file))

st.divider()
st.subheader('Saiba mais sobre o projeto')
st.page_link("https://github.com/eudesgccunha/image-converter.git", label="Repositório no GitHub", icon="🌎")
st.page_link("https://www.linkedin.com/in/eudesgccunha/", label="LinkedIn", icon="ℹ️")