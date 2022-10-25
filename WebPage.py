import streamlit as st
from skimage import io
import gdown
#from streamlit.componets.v1 import html
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

def download_data(url, output):
  gdown.download(url, output, quiet = False)

def image(src_as_string, **style):
  return img(src = src_as_string, style = styles(**style))

def link(link, text, **style):
  return a(_href = link, _target = '_blank', style = styles(**style))(text)

def layout(*args):
  style = """
  <style>
    # MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp {bottom: 80px; }
  </style>
  """
  
  style_div = styles(position = 'fixed', 
                     left = 0, 
                     bottom = 0, 
                     margin = px(0, 0, 0, 0), 
                     width = percent(100), 
                     color = 'black', 
                     text_align = 'center', 
                     height = 'auto', 
                     opacity = 1)
  
  style_hr = styles(display = 'block',
                    margin = px(0, 0, 0, 0),
                    border_style = 'inset',
                    border_widht = px(2))
  
  body = p(id = 'myFooter',
           style = styles(margin = px(0, 0, 0, 0),
                          paddin = px(5),
                          font_size = '0.8rem',
                          color = 'rgb(51, 51, 51)')
          )
  foot = div(style = style_div)(hr(style = style_hr), body)
  st.markdown(style, unsafe_allow_html = True)
  
  for arg in args:
    if isinstance(arg, str):
      body(arg)
    elif isintance(arg, HtlmlElement):
      body(arg)
  
  st.markdown(str(foot), unsafe_allow_html = True)
  
  js_code = '''
  <script>
  function rgbReverse(rgb){
    var r = rgb[0]*0.299;
    var g = rgb[1]*0.587;
    var b = rgb[2]*0.114;
    
    if ((r + g + b)/255 > 0.5){
        return "rgb(49, 51, 63)"
    }else{
        return "rgb(250, 250, 250)"
    }
  };
  
  var stApp_css = window.parent.document.querySelector("#root > div:nth-child(1) > div > div > div");
  window.onload = function(){
    var mutationObserver = new MutationObserver(function(mutations) {
      mutations.forEach(function(mutation) {
        /**************------------------*****************************/
        var bgColor = window.getComputedStyle(stApp_css).backgroundColor.replace("rgb(", "").replace(")", "").split(", ");
        var fontColor = rgbReverse(bgColor);
        var pTag = window.parent.document.getElementById("myFooter");
        pTag.style.color = fontColor;
        /**********************---------****************************/
      });
    });
    
    /**Element**/
    mutationsObserver.observe(stApp_css, {
      attributes: true,
      characterData: true,
      childList: true,
      subtree:true,
      attributeOldValue: true,
      characterDataOldValue: true});
  }
  
  </script>
  '''
  html(js_code)

def footer():
  with open('Fig_1.jpg', 'rb') as f:
    img_logo = f.read()
  logo_cache = st.image(img_logo)
  logo_cache.empty()
  
  myargs = ["Made in", image('Fig_1.jpg', width = px(25), height = px(25)),
            "with ❤️ by", link("https://www.cayetano.edu.pe", "@zafiro")]
  layout(*myargs)
                 
# Imagen para la presentación
url1 = "https://drive.google.com/uc?id=1pi1tDrxSxin4v6Vg58R0wVHPOC--xIgq"
output1 = 'Image_Lab.jpg'

# Imagen para miembros (Parte superior)
url2 = "https://drive.google.com/uc?id=11v-Ys6Ll30ZMze6fJLkS_qyM9od-3rl6"
output2 = 'Fig_M.jpg'

# Imagen para miembros (Parte inferior 1)
url3 = "https://drive.google.com/uc?id=1cSiWY4jlXls4FsEo12geg_lDN_9xdrb-"
output3 = 'Fig_1.jpg'

# Imagen para miembros (Parte inferior 2)
url4 = "https://drive.google.com/uc?id=1y72UA5dOzAu3s-3s8vF6JMwvhJNAa2Vc"
output4 = 'Fig_2.jpg'


# Imagen para miembros (Parte inferior 3)
url5 = "https://drive.google.com/uc?id=1Hmf8YUi5O1gDQ-ejPWTI7xgYC0n9DocP"
output5 = 'Fig_3.jpg'


# Imagen para miembros (Parte inferior 4)
url6 = "https://drive.google.com/uc?id=1kZsL14HqU_no4zOxqsPLIzAb7kQMOpUd"
output6 = 'Fig_4.jpg'

download_data(url1, output1)
download_data(url2, output2)
download_data(url3, output3)
download_data(url4, output4)
download_data(url5, output5)
download_data(url6, output6)

tab1, tab2, tab3, tab4 = st.tabs(['Nosotros', 'Miembros', 'Solicitudes', 'Contacto'])
with tab1:
  st.title('Bienvenidos a los Laboratorios de Ingeniería UPCH')
  st.header('1. Nosotros', anchor = None)
  st.write('uno dos tres cuatro cinco seis siete ocho nueve diez.... añadir descripción de nosotros')
  image = io.imread('Image_Lab.jpg')
  #col1, col2, col3 = st.columns(3)
  #col2.image(image, width = 1000)
  st.image(image, caption = 'Imagen de Prueba', width = None, use_column_width = True, clamp = False, channels = 'RGB', output_format = 'jpg')
  st.header('2. Presentación', anchor = None)
  st.header('3. Misión', anchor = None)
  st.header('4. Visión', anchor = None)
  st.header('5. Campus', anchor = None)
  st.header('6. Organización', anchor = None)
  footer()
with tab2:
  st.markdown('**Miembros**')
  image1 = io.imread('Fig_M.jpg')
  image2 = io.imread('Fig_1.jpg')
  image3 = io.imread('Fig_2.jpg')
  image4 = io.imread('Fig_3.jpg')
  image5 = io.imread('Fig_4.jpg')
  
  col1, col2, col3 = st.columns(3)
  col2.image(image1, caption = 'Juan Manuel')
  col11, col22, col33, col44 = st.columns(4)
  col11.image(image2, caption = 'ALEX')
  col22.image(image3, caption = 'ARELÍ')
  col33.image(image4, caption = 'ABRAHAM')
  col44.image(image5, caption = 'PIERO')
with tab3:
  st.markdown('# Solicitudes', unsafe_allow_html = False)
  st.markdown('#### Solicitar Materiales', unsafe_allow_html = False)
  st.markdown('#### Solicitud de copias', unsafe_allow_html = False)
with tab4:
  st.markdown('**Teléfonos de contacto**')
