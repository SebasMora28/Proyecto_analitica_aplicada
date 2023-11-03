import streamlit as st
import requests
import json
from PIL import Image

# URL de la API Flask
api_url = 'http://127.0.0.1:5000/predict' # Ajusta la URL según la dirección de tu API Flask

# Crear una interfaz de usuario con Streamlit
#st.title('Clasificación de la población con mayor riesgo de hurto en transporte público en Medellín')
#st.title('Clasificación :red[poblacional]')
st.header('Clasificación :red[poblacional] según el riesgo de :red[hurto] en transporte :red[público] en :red[Medellín]', divider='red')
col1, col2 = st.columns([0.44,0.50],gap="small")
with col2:
    st.caption('Dadas ciertas características, buscamos poder **clasificar** a la **víctima** de hurto. En este caso, **identificar** su **sexo** y **grupo de edad**. Con esto se buscamos poder **identificar** al grupo con mayor **probabilidad** de ser **víctima** de **hurto** en el **transporte público** para que la alcaldía de Medellín pueda tomar acciones efectivas al respecto.')
    st.caption('Tomada de: https://medata.gov.co/dataset/1-027-23-000308')
with col1:
    st.image('../api_generation/image.png', width=310, output_format="always" )
st.divider()
st.caption(':red[**Descripción de la base de datos**]\n\nEl modelo unificado de seguridad y convivencia permite acceder a información de hechos relacionados con la seguridad, la convivencia, derechos humanos y justificia que han ocurrido en la ciudad de Medellín y que han sido recopilados por el proyecto municipal Sistema de Información para la Seguridad y la Convivencia SISC. Éste DataSet busca presentar el consolidado de la cantidad de casos de hurto en transporte público en las diferentes comunas de la ciudad de Medellín.')
st.divider()
st.caption(':red[**Creación e implementación del modelo**]\n\nSe utilizó el algoritmo de **KModes** para hacer **clusterización** e identificar a los **inputs** más representativos de la muestra, con esto se buscó **identificar** que categorías en cada **variable** eran aquellas que se **relacionaban** con la **incidencia** del **crimen**.')
genero = None
edad = None

with st.form('myform', clear_on_submit=True):

    with st.expander("Cargar valores"):

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

        col1, col2, col3 = st.columns([1,1,1],gap="medium")
        
        # Crear listas desplegables para que el usuario seleccione las features

        with col1:
            Feature1 = st.selectbox('Estado civil', estado_civil_options,help='Característica de la víctima')
            Feature2 = st.selectbox('Medio de transporte público', transporte_options)
            Feature3 = st.selectbox('Modalidad de robo', modalidad_options,help='Estrategia empleada')
        with col2:
            Feature4 = st.selectbox('Conducta', conducta_options,help='Circunstancia y/o actuar del delito')
            Feature5 = st.selectbox('Comuna', comuna_options)
        with col3: 
            Feature6 = st.selectbox('Lugar', lugar_options,help='Espacio donde se ejecutó el hurto')  
            Feature7 = st.selectbox('Bien', bien_options,help='Propiedad hurtada')
        

        def encontrar_posicion(valor, lista):
            for i, elemento in enumerate(lista):
                if elemento == valor:
                    return i
            return -1  # Valor no encontrado
    submitted = st.form_submit_button('Realizar Predicción')

    if submitted:
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

        st.success("¡Identificación de grupo social realizada exitosamente!")


st.write('▸ :orange[Género de la víctima: ]', genero)
st.write('▸ :orange[Edad de la víctima: ] ', edad)
