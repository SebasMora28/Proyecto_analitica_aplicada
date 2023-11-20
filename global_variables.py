casos_ruta="../datasets/consolidado_casos_criminalidad.csv"
edu_vial2018_ruta="../datasets/educacionvial_2018.csv"
encuesta_calidad_ruta="../datasets/encuesta_calidad_de_vida.csv"
encuesta_cultura_ruta="../datasets/encuesta_cultura_2019.csv"
hurto_tp_ruta="../datasets/hurto_transporte_publico.csv"
lesion_nf_ruta="../datasets/lesion_no_fatal_transito.csv"
mede_victimas_ruta="../datasets/mede_victimas_inci.csv"
traffic_ruta="../datasets/simmtrafficdata.csv"
compar_ruta="../datasets/comparendos.csv"

casos_rutac="../datasets_clean/casosc.csv"
edu_vial2018_rutac="../datasets_clean/eduvial_2018c.csv"
encuesta_calidad_rutac="../datasets_clean/encuesta_calidad_de_vida.csv"
encuesta_cultura_rutac="../datasets_clean/encuesta_cultura_2019.csv"
hurto_tp_rutac="../datasets_clean/hurto_tpc.csv"
lesion_nf_rutac="../datasets_clean/lesion_no_fatal_transito.csv"
mede_victimas_rutac="../datasets_clean/mede_vicc.csv"
traffic_rutac="../datasets_clean/simmtrafficdata.csv"
compar_rutac="../datasets_clean/comparc.csv"

sexo_options = ["Hombre", "Mujer"]
estado_civil_options = ['Casado(a)', 'Unión marital de hecho', 'Soltero(a)', 'Sin dato','Divorciado(a)', 'Viudo(a)']
transporte_options = ['Taxi', 'Metro', 'Autobus']
modalidad_options = ['Atraco', 'Descuido', 'Cosquilleo', 'Raponazo', 'Sin dato','Comisión de delito', 'Engaño', 'Escopolamina','Clonación de tarjeta', 'Rompimiento cerraduta', 'Suplantación',
       'Miedo o terror', 'Forcejeo', 'Halado', 'Llamada millonaria','Rompimiento de ventana', 'Retención de tarjeta','Simulando necesidad', 'Fleteo']
conducta_options = ['De celular', 'No', 'A taxista', 'Sin dato','A bus de servicio público', 'Fleteo', 'Paseo millonario',
       'Grupo delincuencial', 'Muerte o lesión de delincuente','Vehículo servicio público', 'Violencia contra la mujer',
       'Homicidio', 'Secuestro', 'Adulteración']
comuna_options = [4., 16.,  8., 15.,  5., 14.,  7., 10.,  9.,  2., 11.,  6., 12., 3., 90., 13., 60., 80.,  1., 70., 50.]
lugar_options = ['Vía pública', 'Estación del Metro', 'Bus de servicio público',
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
       'Matadero, carnicería y similar', 'Café internet']
bien_options = ['Celular', 'Elementos escolares', 'Computador', 'Peso',
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
       'Vodka']
grupo_edad = ['Niño (0-12 años)','Adolescente (13-18 años)','Adulto joven (19-30 años)','Adulto (31-60 años)','Adulto mayor (60+ años)']