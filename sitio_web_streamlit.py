import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


#Funcion para nuestra animacion
def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()

lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_0yfsb3a1.json")
#imagen_video = Image.open("/content/maxresdefault (2).jpg") #Pon la ruta de tu imagen
imagen_video = Image.open("mariposa.jpg") #Pon la ruta de tu imagen
with st.container():
  st.subheader("Hola bienvenido a mi sitio web, soy WFCZ")
  st.title("Introduccion a la ciencia de datos")
  st.write("Bienvenido a mi canal")
  st.write("[1.-Mas informacion >](https://dashboardwfcz.streamlit.app/")
  st.write("[2.-Mas informacion >](https://graficosestadisticos.streamlit.app/")
  st.write("[3.-Mas informacion >](https://gdp-dashboard-21j41zht4jt.streamlit.app/")
  st.write("[4.-Mas informacion >](https://cinco-paises-mas-poblados-1955-2020.streamlit.app/")

with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("Mi objetivo")
    st.write(
      """
        Texto aquí
      """
    )
    st.write("[1.- Video-> Albert Einstein >](https://www.youtube.com/watch?v=NARG2MPpVnQ&t=70s")
    st.write("[2.- Video-> Filosofo Platón >](https://www.youtube.com/watch?v=eqMcUGXsRHE")

  with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

with st.container():
  st.write("--")
  st.header("Mis videos")
  image_column, text_column = st.columns((1, 2))
  with image_column:
    st.image(imagen_video)
  with text_column:
    st.write(
      """
      texto aquí
      """
    )
    st.markdown("[Ver video...](http:///youtube.mx)")

#!streamlit run app.py & npx localtunnel --port 8501
  