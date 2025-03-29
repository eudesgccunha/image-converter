# Image Converter 
[ENG]
This is a free project to you convert images and pdf with python.

## Libraries

- [streamlit](https://docs.streamlit.io/develop/api-reference) → Framework to create the application's web interface.
- Pillow (PIL) → Image manipulation.
- pdf2image → PDF to image conversion.
- rembg → Image background removal.

## File structures

📂 image-converter/ <br>
│── 📜 app.py              # main code <br>
│── 📂 uploads/            # temp storage for uploaded files <br>
│── 📂 outputs/            # temp storage for outputed files <br>

## Run App Localy

### Install libraries

#### 1st option
* **Create and activate a virtual enviroment**
    ```bash
    conda create -n img-conv-venv python=3.12
    conda activate img-conv-venv
    ```

* **Run requirements.txt**
  
    ```bash
    pip install -r requirements.txt
    ```

#### 2nd option
* **Create a virtual enviroment**

    ```bash
    conda env create -f environment.yaml
    ``` 

* **Activate a virtual enviroment**

    ```bash
    conda activate img-conv-venv
    ``` 

### Run in terminal
```bash
streamlit run app.py
```


# 📝 Como funciona o código?
[BR]
O usuário faz upload de um ou mais arquivos de imagem ou PDF.

  1. O programa salva os arquivos na pasta uploads/.
  2. Se o arquivo for PDF, ele é convertido em imagens (uma por página).
  3. Para imagens, o programa converte para o formato desejado.
  4. Se a opção de remover fundo estiver marcada, o fundo da imagem é removido.
  5. O usuário pode baixar os arquivos convertidos diretamente pelo Streamlit.