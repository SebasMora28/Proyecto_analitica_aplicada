import numpy as np
import pandas as pd

def medevic_treatment():
    print(mede_victimas['Gravedad_victima'].value_counts())
    mede_victimas = mede_victimas.dropna()
    columns_to_check = ['Sexo', 'Edad']
    for column in columns_to_check:
        mede_victimas = mede_victimas[(mede_victimas[column] != 'Sin Inf') & (mede_victimas[column] != 'Sin inf')]
    import re
    def convert_age_to_int(age_str):
        
        if isinstance(age_str, str) and '-' in age_str:
            ages = re.findall(r'\d+', age_str)  # Extraer los números del rango
            return (int(ages[0]) + int(ages[1])) // 2  # Promedio de los valores del rango
        else:
            return int(age_str)  # Si es un valor único, simplemente conviértelo a entero
    # Eliminar filas con valores NaN en la columna 'Edad'
    mede_victimas['Edad'] = mede_victimas['Edad'].apply(convert_age_to_int)
    mede_victimas = mede_victimas.drop(mede_victimas[mede_victimas['Edad'] > 100].index)
    mede_victimas['Condicion'] = mede_victimas['Condicion'].replace({'Acompañante de Motocicleta': 'Acompañante de motocicleta'})
    