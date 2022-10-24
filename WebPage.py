import streamlit as st
from skimage import io
#from skimage.io import imread
import gdown

def download_data():
  url = "https://drive.google.com/uc?id=1pi1tDrxSxin4v6Vg58R0wVHPOC--xIgq"
  output = 'Image_Lab.jpg'
  gdown.download(url, output, quiet = False)

download_data()
st.title('Bienvenidos al Laboratorio de Ingeniería UPCH')
st.header('Descripción', anchor = 'Descripción')
image = io.imread('Image_Lab.jpg')
st.image(image, caption = 'Imagen de Prueba', width = None, use_column_width = None, clamp = False, channels = 'RGB', output_format = 'jpg')
