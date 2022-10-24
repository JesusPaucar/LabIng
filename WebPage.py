import streamlit as st
from skimage import io
#from skimage.io import imread
import gdown

import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
'''
def download_data():
  url = "https://drive.google.com/uc?id=1pi1tDrxSxin4v6Vg58R0wVHPOC--xIgq"
  output = 'Image_Lab.jpg'
  gdown.download(url, output, quiet = False)

download_data()
st.title('Bienvenidos al Laboratorio de Ingeniería UPCH')
st.header('1. Descripción', anchor = None)
image = io.imread('Image_Lab.jpg')
st.image(image, caption = 'Imagen de Prueba', width = None, use_column_width = None, clamp = False, channels = 'RGB', output_format = 'jpg')
st.markdown('# Solicitudes', unsafe_allow_html = True)
st.markdown('#### Solicitar Materiales', unsafe_allow_html = True)
st.markdown('#### Solicitud de copias', unsafe_allow_html = True)
'''
