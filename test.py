import streamlit as st
import requests
import json

# URL de la API Flask
api_url = 'http://127.0.0.1:5000/predict' # Ajusta la URL según la dirección de tu API Flask

# Crear una interfaz de usuario con Streamlit
st.title('Clasificación de la población con mayor riesgo de hurto en transporte público en Medellín')

# Definir arreglos de opciones
from global_variables import sexo_options
from global_variables import estado_civil_options
from global_variables import transporte_options
from global_variables import modalidad_options
from global_variables import conducta_options
from global_variables import comuna_options
from global_variables import lugar_options
from global_variables import bien_options
from global_variables import grupo_edad

# Crear listas desplegables para que el usuario seleccione las features
Feature1 = st.selectbox('Estado civil', estado_civil_options)
Feature2 = st.selectbox('Medio de transporte público', transporte_options)
Feature3 = st.selectbox('Modalidad de robo', modalidad_options)
Feature4 = st.selectbox('Conducta', conducta_options)
Feature5 = st.selectbox('Comuna', comuna_options)
Feature6 = st.selectbox('Lugar', lugar_options)
Feature7 = st.selectbox('Bien', bien_options)

def encontrar_posicion(valor, lista):
    for i, elemento in enumerate(lista):
        if elemento == valor:
            return i
    return -1  # Valor no encontrado

if st.button('Realizar Predicción'):
    feature1_value = encontrar_posicion(Feature1,estado_civil_options)
    feature2_value = encontrar_posicion(Feature2,transporte_options)
    feature3_value = encontrar_posicion(Feature3,modalidad_options)
    feature4_value = encontrar_posicion(Feature4,conducta_options)
    feature5_value = encontrar_posicion(Feature5,comuna_options)
    feature6_value = encontrar_posicion(Feature6,lugar_options)
    feature7_value = encontrar_posicion(Feature7,bien_options)


    # Crear el objeto JSON con las features para enviar a la API
    data = {
        'features': [feature1_value, feature2_value, feature3_value,feature4_value,feature5_value,feature6_value,feature7_value]
    }
    #st.write(data)
    # Realizar la solicitud a la API Flask
    response = requests.post(api_url, json=data)
    
    if response.status_code == 200:
        result = json.loads(response.text)
        
        # Access the prediction list
        prediction_list = result['prediction']
        
        # Access the first element in the prediction list
        first_element = prediction_list[0]
        
        # Access specific values inside the first element
        value_1 = int(first_element[0])  # Access the value at index 0
        value_2 = int(first_element[1])  # Access the value at index 1

        genero = sexo_options[value_2] #Get the value from the respective position in the list
        edad = grupo_edad[value_1]

        st.write('Género de la víctima:', genero)
        st.write('Edad de la víctima:', edad)
