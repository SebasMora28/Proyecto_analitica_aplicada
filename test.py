import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="Pantalla Inicial Decorada",
    layout="wide",  # Puedes usar 'centered' o 'wide'
)

# Título de la página
st.title("Bienvenido a mi aplicación Streamlit")

# Introducción
st.write("Esta es una aplicación de ejemplo decorada con Streamlit. ¡Comencemos!")

# Botones
if st.button("Botón 1"):
    st.write("Botón 1 presionado")
if st.button("Botón 2"):
    st.write("Botón 2 presionado")

# Colores de fondo
st.markdown("---")
st.write("Cambiar color de fondo:")
bg_color = st.selectbox("Seleccione un color de fondo", ["Blanco", "Gris Claro", "Azul Claro"])
if bg_color == "Blanco":
    st.markdown(
        """<style>
        body {
            background-color: #ffffff;
        }
        </style>""",
        unsafe_allow_html=True,
    )
elif bg_color == "Gris Claro":
    st.markdown(
        """<style>
        body {
            background-color: #f0f0f0;
        }
        </style>""",
        unsafe_allow_html=True,
    )
elif bg_color == "Azul Claro":
    st.markdown(
        """<style>
        body {
            background-color: #c7e9c0;
        }
        </style>""",
        unsafe_allow_html=True,
    )

# Estilo para los botones
st.markdown("---")
st.write("Personalizar botones:")
button_color = st.selectbox("Seleccione un color para los botones", ["Azul", "Verde", "Rojo"])
if button_color == "Azul":
    st.markdown(
        """<style>
        .st-eb {
            background-color: #0074e4;
        }
        .st-eb:hover {
            background-color: #0053b3;
        }
        </style>""",
        unsafe_allow_html=True,
    )
elif button_color == "Verde":
    st.markdown(
        """<style>
        .st-eb {
            background-color: #4CAF50;
        }
        .st-eb:hover {
            background-color: #45a049;
        }
        </style>""",
        unsafe_allow_html=True,
    )
elif button_color == "Rojo":
    st.markdown(
        """<style>
        .st-eb {
            background-color: #f44336;
        }
        .st-eb:hover {
            background-color: #d32f2f;
        }
        </style>""",
        unsafe_allow_html=True,
    )