import streamlit as st
import os
from PIL import Image
from pdf2image import convert_from_path
import rembg
import io

def save_uploaded_file(uploaded_file, folder="uploads"):
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def convert_image(file_path, output_format):
    img = Image.open(file_path)
    output_file = file_path.rsplit(".", 1)[0] + f".{output_format}"
    img.save(output_file, format=output_format.upper())
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

st.title("Conversor de Arquivos e Removedor de Background")
uploaded_files = st.file_uploader("Envie arquivos", type=["jpg", "jpeg", "png", "pdf", "webp", "tif", "tiff"], accept_multiple_files=True)

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
    
    for converted_file in converted_files:
        with open(converted_file, "rb") as f:
            st.download_button("Baixar " + os.path.basename(converted_file), f, file_name=os.path.basename(converted_file))
