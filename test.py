import streamlit as st
import requests

import streamlit as st
import requests
import json

# URL de la API Flask
api_url = 'http://127.0.0.1:5000/predict'  # Ajusta la URL según la dirección de tu API Flask

# Crear una interfaz de usuario con Streamlit
st.title('Modelo de Predicción')

# Crear listas desplegables para que el usuario seleccione las features
Estado_civil = st.selectbox('Feature 1', ['Casado(a)', 'Unión marital de hecho', 'Soltero(a)', 'Sin dato','Divorciado(a)', 'Viudo(a)'])  # Opciones de Estado civil
Trasnporte = st.selectbox('Feature 2', ['Taxi', 'Metro', 'Autobus'])  # Opciones de Trasnporte
Modalidad = st.selectbox('Feature 3', ['Atraco', 'Descuido', 'Cosquilleo', 'Raponazo', 'Sin dato',
       'Comisión de delito', 'Engaño', 'Escopolamina','Clonación de tarjeta', 'Rompimiento cerraduta', 'Suplantación',
       'Miedo o terror', 'Forcejeo', 'Halado', 'Llamada millonaria','Rompimiento de ventana', 'Retención de tarjeta','Simulando necesidad', 'Fleteo'])  # Opciones de Modalidad
Conducta = st.selectbox('Feature 4',  ['De celular', 'No', 'A taxista', 'Sin dato',
       'A bus de servicio público', 'Fleteo', 'Paseo millonario',
       'Grupo delincuencial', 'Muerte o lesión de delincuente',
       'Vehículo servicio público', 'Violencia contra la mujer',
       'Homicidio', 'Secuestro', 'Adulteración'])  # Opciones de Conducta
Comuna = st.selectbox('Feature 5',  [ 4., 16.,  8., 15.,  5., 14.,  7., 10.,  9.,  2., 11.,  6., 12.,
        3., 90., 13., 60., 80.,  1., 70., 50.])  # Opciones de Comuna
Lugar = st.selectbox('Feature 6',  ['Vía pública', 'Estación del Metro', 'Bus de servicio público',
       'Vehículo particular', 'Estación del Metro plus', 'Metro Plus',
       'Residencia', 'Hotel, motel y hostal', 'Paradero de bus', 'Parque',
       'Edificio', 'Casa o apartamento', 'Terminal de transporte',
       'Bar o cantina', 'Cementerio', 'Restaurante', 'Turístico',
       'Centro comercial', 'Biblioteca', 'Fábrica o empresa',
       'Montallanta', 'Corporación', 'Institución de educación superior',
       'Estación de gasolina', 'Oficina', 'Parqueadero',
       'Almacén tienda y otro', 'Sin dato', 'Escenario deportivo',
       'Iglesia', 'Quebrada o rio', 'Hospital o centro de salud',
       'Instalación gubernamental', 'Supermercado', 'Plaza de mercado',
       'Puente peatonal',
       'Institución educativa (jardín, primaria o secundaria)',
       'Cafetería', 'Local comercial',
       'Sede social, club, auditorio o similar', 'Cajero electrónico',
       'Banco', 'Potrero', 'Conjunto residencial', 'Finca', 'Lote baldío',
       'Bodega', 'Aeropuerto', 'Billar', 'Reserva natural', 'Panadería',
       'Casino', 'Caseta vigilancia conjunto residencial',
       'Droguería o farmacia', 'Gimnasio', 'Teatro',
       'Caseta de vigilancia empresa', 'Puesto de trabajo', 'Metro',
       'Obra en construcción', 'Cárcel', 'Casa de apuesta',
       'Zona boscosa', 'Peaje', 'Feria de ganado',
       'Instalación fuerza pública', 'Albergue', 'Baño', 'Plaza de toros',
       'Matadero, carnicería y similar', 'Café internet'])  # Opciones de Lugar
Bien = st.selectbox('Feature 7', ['Celular', 'Elementos escolares', 'Computador', 'Peso',
       'Billetera', 'Cédula', 'Accesorios prendas de vestir', 'Radio',
       'Autopartes', 'Salsa', 'Tarjeta bancaria', 'Cámara', 'Gps',
       'Tarjeta de comunicación', 'Libreta militar', 'Licencia',
       'Equipos varios', 'Llave', 'Ropa exterior', 'Maletín',
       'Accesorios celular',
       'Electrodoméstico video y audio y accesorios', 'Dólar', 'Euro',
       'Carbohidratos y dulces', 'Carne', 'Zapatos', 'Llaveros', 'Soat',
       'Repuestos para maquinaria y equipo', 'Elementos computador',
       'Tablet', 'Ipod', 'Perfumería', 'Pasaporte',
       'Electrodomésticos cocina y limpieza hogar', 'Ventilador',
       'Portadocumentos', 'Artículos de aseo personal',
       'Tarjeta de identidad', 'Dijes', 'Moneda falsa', 'Insumo médico',
       'Casco moto', 'Espejo', 'Paquete de software',
       'Articulos electrónica', 'Estuche', 'Sin dato',
       'Artículo para video', 'Bono', 'Registro civil',
       'Artículos y ropa de cama', 'Revisión técnico mecánica', 'Módem',
       'Real brasilero', 'Acciones', 'Sin dato tecnología',
       'Medicamentos', 'Sellos', 'Expediente', 'Sin dato documentos',
       'Proyector', 'Sin dato joyas', 'Sin dato mercancías', 'Revólver',
       'Sin dato munición', 'Sin dato herramientas', 'Cheques',
       'Sin dato prendas de vestir', 'Sin dato maquinaria y equipo',
       'Máquina', 'Libros', 'Muebles del hogar', 'Pasacintas', 'Placa',
       'Automóvil', 'Monitor', 'Libra esterlina inglesa', 'Telas',
       'Pistola', 'Frutas y verduras', 'Silla', 'Cdt', 'Escarapela',
       'Tarjeta para computador', 'Arma blanca', 'Documentos falsos',
       'Antenas', 'Dvd', 'Caja desbloqueo celulares', 'Cd',
       'Gato hidráulico', 'Loción', 'Sombrilla', 'Instrumento musical',
       'Avión', 'Placa policial', 'Prendas ponal', 'Pistola neumática',
       'Oro', 'Contraseña cédula', 'Cargadores', 'Máquina industrial',
       'Micrófono', 'Lámpara de alumbrado', 'Registradora',
       'Juguete arma bélica', 'Encomiendas', 'Coche para bebe', 'Whiskey',
       'Sin dato electrodomésticos', 'Documentación electoral',
       'Cuenta de ahorro', 'Bicicleta', 'Boleta', 'Interior',
       'Alimentos enlatados y embutidos', 'Carta',
       'Prendas cia. Vigilancia', 'Patente', 'Visa', 'Póliza de seguro',
       'Termos', 'Datáfono', 'Palma', 'Sin dato títulos valor', 'Escrito',
       'Talonario', 'Contrato', 'Papel', 'Taladro',
       'Material de construcción', 'Permiso porte de arma', 'Medidor',
       'Teléfono satelital', 'Línea telefónica',
       'Accesorios de peluquería', 'Aparato médico', 'Morral militar',
       'Glucosa', 'Carátula', 'Escritura', 'Plata', 'Otros animales',
       'Elementos deportivos', 'Sin dato médico', 'Grabadora', 'Calcio',
       'Certificado de gases', 'Archivador', 'Plancha de cabello',
       'Plancha', 'Camándulas', 'Bombas', 'Aguardiente', 'Fotografías',
       'Sin dato articulos electrónica', 'Bolívar venezolano', 'Manual',
       'Cinturón', 'Medicamento trastorno ansiedad y mental', 'Vcd',
       'Diario digital', 'Decoración del hogar', 'Venado', 'Lector',
       'Joyería', 'Amplificador de sonido', 'Guantes', 'Vitrina',
       'Letra de cambio', 'Bota militar', 'Etiquetas', 'Telex',
       'Artículos alimenticios', 'Caja fuerte', 'Vacuna', 'Secador',
       'Factura', 'Alambre', 'Acid-mantle', 'Toalla',
       'Promesa de compraventa', 'Bebidas',
       'Medicamento antiinflamatorio', 'Joyero', 'Aceite', 'Adaptador',
       'Vodka'])  # Opciones de Bien


# Crear mapeos para las características con diferentes rangos
feature1_mapping = {str(i): i for i in range(1, 6)}    # Estado civil
feature2_mapping = {str(i): i for i in range(1, 3)}    # Transporte
feature3_mapping = {str(i): i for i in range(1, 19)}   # Modalidad 
feature4_mapping = {str(i): i for i in range(1, 14)}   # Conducta
feature5_mapping = {str(i): i for i in range(1, 21)}   # Comuna
feature6_mapping = {str(i): i for i in range(1, 71)}   # Lugar
feature7_mapping = {str(i): i for i in range(1, 190)}  # Bien

# Botón para realizar la predicción
if st.button('Realizar Predicción'):
    # Obtener los valores numéricos correspondientes a las opciones seleccionadas
    feature1_value = feature1_mapping.get(Estado_civil, 0)
    feature2_value = feature2_mapping.get(Trasnporte, 0)
    feature3_value = feature3_mapping.get(Modalidad, 0)
    feature4_value = feature4_mapping.get(Conducta, 0)
    feature5_value = feature5_mapping.get(Comuna, 0)
    feature6_value = feature6_mapping.get(Lugar, 0)
    feature7_value = feature7_mapping.get(Bien, 0)

    # Crear el objeto JSON con las features para enviar a la API
    data = {
        'features': [feature1_value, feature2_value, feature3_value,feature4_value,feature5_value,feature6_value,feature7_value]
    }

    # Realizar la solicitud a la API Flask
    response = requests.post(api_url, json=data)

    # Procesar la respuesta de la API
    if response.status_code == 200:
        result = json.loads(response.text)
        st.write('Resultado de la predicción:', result['prediction'])
    else:
        st.error('Error al realizar la predicción. Asegúrate de que la API Flask esté en ejecución y que la URL sea correcta.')

