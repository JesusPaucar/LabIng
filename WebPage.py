import streamlit as st
from skimage import io
import gdown

def download_data():
  url = "https://drive.google.com/uc?id=1pi1tDrxSxin4v6Vg58R0wVHPOC--xIgq"
  output = 'Image_Lab.jpg'
  gdown.download(url, output, quiet = False)

download_data()
tab1, tab2, tab3, tab4 = st.tabs(['Descripción', 'Miembros', 'Solicitudes', 'Contacto'])
with tab1:
  st.title('Bienvenidos al Laboratorio de Ingeniería UPCH')
  st.header('1. Descripción', anchor = None)
  image = io.imread('Image_Lab.jpg')
  st.image(image, caption = 'Imagen de Prueba', width = None, use_column_width = None, clamp = False, channels = 'RGB', output_format = 'jpg')
with tab2:
  st.markdown(**Miembros**)
with tab3:
  st.markdown('# Solicitudes', unsafe_allow_html = True)
  st.markdown('#### Solicitar Materiales', unsafe_allow_html = True)
  st.markdown('#### Solicitud de copias', unsafe_allow_html = True)
with tab4:
  st.markdown(**Teléfonos de contacto**)
