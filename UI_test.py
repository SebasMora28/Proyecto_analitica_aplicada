import streamlit as st
import requests

st.title("Clasificación de la población con mayor riesgo de hurto en transporte público en Medellín")

# Agrega elementos para que el usuario ingrese características
features = st.text_area("Ingrese las características (separadas por comas)")

if st.button("Obtener Predicción"):
    # Convierte las características ingresadas en una lista de números
    features_list = [float(x) for x in features.split(',')]

    # Realiza una solicitud POST a la API Flask
    api_url = "http://127.0.0.1:5000/predict"  # Ajusta la URL según tu configuración de Flask
    response = requests.post(api_url, json={"features": features_list})

    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.success(f"Predicción: {prediction}")
    else:
        st.error("Error al obtener la predicción")