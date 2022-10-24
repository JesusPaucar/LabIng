import streamlit as st
from skimage import io
import gdown

def download_data():
  url = "https://drive.google.com/uc?id=1pi1tDrxSxin4v6Vg58R0wVHPOC--xIgq"
  output = 'Image_Lab.jpg'
  gdown.download(url, output, quiet = False)

download_data()
tab1, tab2, tab3, tab4 = st.tabs(['Nosotros', 'Miembros', 'Solicitudes', 'Contacto'])
with tab1:
  st.title('Bienvenidos a los Laboratorios de Ingeniería UPCH')
  st.header('1. Nosotros', anchor = None)
  st.write('uno dos tres cuatro cinco seis siete ocho nueve diez.... añadir descripción de nosotros')
  image = io.imread('Image_Lab.jpg')
  #col1, col2, col3 = st.columns(3)
  #col2.image(image, width = 1000)
  st.image(image, caption = 'Imagen de Prueba', width = None, use_column_width = True, clamp = False, channels = 'RGB', output_format = 'jpg')
with tab2:
  st.markdown('**Miembros**')
with tab3:
  st.markdown('# Solicitudes', unsafe_allow_html = False)
  st.markdown('#### Solicitar Materiales', unsafe_allow_html = False)
  st.markdown('#### Solicitud de copias', unsafe_allow_html = False)
with tab4:
  st.markdown('**Teléfonos de contacto**')
