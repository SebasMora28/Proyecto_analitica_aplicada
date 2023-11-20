import streamlit as st
import requests
import json
from PIL import Image
import pandas as pd
import altair as alt

# URL de la API Flask

api_url = 'http://127.0.0.1:5000/predict' # Ajusta la URL según la dirección de tu API Flask

# Crear una interfaz de usuario con Streamlit
tab1, tab2 = st.tabs(["Implementación del modelo", "¿Un vistazo global de los datos?"])

with tab1:

    st.header('Clasificación :red[poblacional] según el riesgo de :red[hurto] en transporte :red[público] en :red[Medellín]', divider='red')
    col1, col2 = st.columns([0.44,0.50],gap="small")
    with col2:
        st.caption('Dadas ciertas características, buscamos poder **clasificar** a la **víctima** de hurto. En este caso, **identificar** su **sexo** y **grupo de edad**. Con esto se buscamos poder **identificar** al grupo con mayor **probabilidad** de ser **víctima** de **hurto** en el **transporte público** para que la alcaldía de Medellín pueda tomar acciones efectivas al respecto.')
        st.caption('Tomada de: https://medata.gov.co/dataset/1-027-23-000308')
    with col1:
        st.image('../api_generation/image.png', width=310, output_format="always" )
    st.divider()
    
    st.caption(':red[**Creación e implementación del modelo**]\n\nSe utilizó el algoritmo de **KModes** para hacer **clusterización** e identificar a los **inputs** más representativos de la muestra, con esto se buscó **identificar** que categorías en cada **variable** eran aquellas que se **relacionaban** con la **incidencia** del **crimen**.')
    genero = None
    edad = None
    st.caption(":white[Como se mencionaba anteriormente éste modelo permite definir el :red[Género:] Hombre o Mujer y :red[Edad:] Niño (0-12), Adolescente (13-18), Adulto joven (19-30), Adulto (31-60) o Adulto Mayor (60+).]")
    st.caption('Puedes experimentar el modelo presionando "Cargar valores" en el cuadro inferior y asignando variabes según tu interés.')

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

with tab2:

    st.caption(':red[**Descripción de la base de datos**]\n\nEl modelo unificado de seguridad y convivencia permite acceder a información de hechos relacionados con la seguridad, la convivencia, derechos humanos y justificia que han ocurrido en la ciudad de Medellín y que han sido recopilados por el proyecto municipal Sistema de Información para la Seguridad y la Convivencia SISC. Éste DataSet busca presentar el consolidado de la cantidad de casos de hurto en transporte público en las diferentes comunas de la ciudad de Medellín.')
    st.divider()

    col1,col2 = st.columns(2)

    with col1:
    
        # Load your data from the CSV file
        hurto_tp = pd.read_csv("../datasets_clean/hurto_tpc.csv", delimiter=";", encoding="utf-8")

        # Gráfico de torta: Proporción de sexos en el dataset
        cantidad_por_sexo = hurto_tp['Sexo'].value_counts().reset_index()
        cantidad_por_sexo.columns = ['Sexo', 'Cantidad']

        # Define el tamaño del gráfico (ajusta estos valores según tus necesidades)
        width = 333
        height = 333

        pie_chart = alt.Chart(cantidad_por_sexo).mark_arc().encode(
            theta='Cantidad:Q',
            color='Sexo:N',
            tooltip=['Sexo:N', 'Cantidad:Q']
        ).properties(
            title='Distribución de género',
            width=width,  # Ancho personalizado
            height=height  # Altura personalizada
        )

        # Mostrar el gráfico en la aplicación de Streamlit
        st.write(pie_chart)

    with col2:

        # Contar las ocurrencias de modalidades y encontrar el top 3
        top_modalidades = hurto_tp['Modalidad'].value_counts().nlargest(4).reset_index()
        top_modalidades.columns = ['Modalidad', 'Cantidad']

        # Define el tamaño del gráfico (ajusta estos valores según tus necesidades)
        width = 340
        height = 340

        pie_chart = alt.Chart(top_modalidades).mark_arc().encode(
            theta='Cantidad:Q',
            color='Modalidad:N',
            tooltip=['Modalidad:N', 'Cantidad:Q']
        ).properties(
            title='Top 4 modalidades de hurto',
            width=width,  # Ancho personalizado
            height=height  # Altura personalizada
        )

        # Mostrar el gráfico en la aplicación de Streamlit
        st.write(pie_chart)

    ####################################################

    # Contar las ocurrencias de cada combinación de comuna y sexo
    robos_por_comuna_sexo = hurto_tp.groupby(['Comuna', 'Sexo']).size().reset_index(name='Cantidad')

    # Crear un gráfico Altair de barras apiladas
    chart = alt.Chart(robos_por_comuna_sexo).mark_bar().encode(
        x=alt.X('Comuna:N', title='Comuna', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Cantidad:Q', title='Cantidad de Hurtos'),
        color=alt.Color('Sexo:N', scale=alt.Scale(domain=['Hombre', 'Mujer'], range=['#1f77b4', '#ff7f0e']))
    ).properties(width=700, height=400, title='Hurtos por comuna y género')

    st.altair_chart(chart, use_container_width=True)

    ####################################################

    # Contar las ocurrencias de bienes por comuna
    bienes_por_comuna = hurto_tp.groupby(['Comuna', 'Bien']).size().reset_index(name='Cantidad')

    # Encontrar el top 3 de bienes por comuna
    top_3_bienes = bienes_por_comuna.groupby('Comuna').apply(lambda x: x.nlargest(3, 'Cantidad')).reset_index(drop=True)

    # Crear un gráfico Altair de barras agrupadas
    chart = alt.Chart(top_3_bienes).mark_bar().encode(
        x=alt.X('Comuna:N', title='Comuna', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Cantidad:Q', title='Cantidad de Hurtos'),
        color=alt.Color('Bien:N')
    ).properties(width=700, height=400, title='Top 3 bienes hurtados por comuna')

    st.altair_chart(chart, use_container_width=True)

    ####################################################
        
    # Crear grupos de edades (por ejemplo, grupos de 10 años)
    edades = pd.cut(hurto_tp['Edad'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], labels=['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100'])

    # Agregar la columna 'Edades' al DataFrame original
    hurto_tp['Edades'] = edades

    # Contar las ocurrencias de hurtos por grupos de edad y género
    robos_por_edad_sexo = hurto_tp.groupby(['Edades', 'Sexo']).size().reset_index(name='Cantidad')

    # Crear un gráfico Altair de barras apiladas con apilamiento por género
    chart = alt.Chart(robos_por_edad_sexo).mark_bar().encode(
        x=alt.X('Edades:N', title='Grupos de Edad', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Cantidad:Q', title='Cantidad de Hurtos'),
        color=alt.Color('Sexo:N', scale=alt.Scale(domain=['Hombre', 'Mujer'], range=['#1f77b4', '#ff7f0e']))
    ).properties(width=700, height=400, title='Hurtos por grupos de edad y género')

    st.altair_chart(chart, use_container_width=True)

    ###################################################

    # Convertir la columna de fecha al tipo de fecha
    hurto_tp['Fecha'] = pd.to_datetime(hurto_tp['Fecha'])

    # Filtrar los datos para incluir solo las fechas desde 2018 en adelante
    hurto_tp = hurto_tp[hurto_tp['Fecha'].dt.year >= 2017]

    # Contar las ocurrencias de hurtos por fecha
    hurtos_por_fecha = hurto_tp.groupby('Fecha').size().reset_index(name='Cantidad')

    # Crear un gráfico de líneas con Altair
    #st.write("## Evolución de Hurtos desde 2018")

    # Crear un gráfico Altair de líneas
    chart = alt.Chart(hurtos_por_fecha).mark_line().encode(
        x=alt.X('Fecha:T', title='Fecha'),
        y=alt.Y('Cantidad:Q', title='Cantidad de Hurtos'),
    ).properties(width=700, height=400,title='Frecuencia de hurtos desde 2017')

    st.altair_chart(chart, use_container_width=True)

    ###################################################

    # Calcular el promedio de modalidades por comuna
    promedio_modalidades_por_comuna = hurto_tp.groupby(['Comuna', 'Modalidad']).size().reset_index(name='Cantidad')

    # Encontrar las top 3 modalidades por comuna
    top_3_modalidades = promedio_modalidades_por_comuna.groupby('Comuna').apply(lambda x: x.nlargest(3, 'Cantidad')).reset_index(drop=True)

    # Crear un gráfico de barras apiladas con Altair para el top 3 de modalidades en promedio por comuna

    chart = alt.Chart(top_3_modalidades).mark_bar().encode(
        x=alt.X('Comuna:N', title='Comuna'),
        y=alt.Y('Cantidad:Q', title='Cantidad de Hurtos'),
        color=alt.Color('Modalidad:N', legend=alt.Legend(title="Modalidad")),
        tooltip=['Comuna:N', 'Modalidad:N', 'Cantidad:Q']
    ).properties(
        width=700,
        height=400,
        title='Top 3 modalidades de hurto por comuna'
    )

    st.altair_chart(chart, use_container_width=True)


    