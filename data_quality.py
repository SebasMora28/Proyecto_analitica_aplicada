import pandas as pd
import numpy as np
from global_variables import casos_ruta
from global_variables import edu_vial2018_ruta
from global_variables import encuesta_calidad_ruta
from global_variables import encuesta_cultura_ruta
from global_variables import hurto_tp_ruta
from global_variables import lesion_nf_ruta
from global_variables import mede_victimas_ruta
from global_variables import traffic_ruta
from global_variables import compar_ruta


def cargue_datasets():
    casos=pd.read_csv(casos_ruta, delimiter=";", encoding="utf-8")
    edu_vial2018=pd.read_csv(edu_vial2018_ruta, delimiter=";", encoding="utf-8")
    encuesta_calidad=pd.read_csv(encuesta_calidad_ruta, delimiter=";", encoding="utf-8")
    encuesta_cultura=pd.read_csv(encuesta_cultura_ruta, delimiter=";", encoding="utf-8")
    hurto_tp=pd.read_csv(hurto_tp_ruta, delimiter=";", encoding="utf-8")
    lesion_nf=pd.read_csv(lesion_nf_ruta, delimiter=";", encoding="utf-8")
    mede_victimas=pd.read_csv(mede_victimas_ruta, delimiter=";", encoding="utf-8")
    traffic=pd.read_csv(traffic_ruta, delimiter=";", encoding="utf-8")
    compar=pd.read_csv(compar_ruta, delimiter=";", encoding="utf-8")
    return casos, edu_vial2018, encuesta_calidad, encuesta_cultura, hurto_tp, lesion_nf, mede_victimas, traffic, compar

def casos_treatment(df):
    df=df.drop(df[df["Codigo_comuna"]=="SIN DATO"].index)
    df["Codigo_comuna"]=df["Codigo_comuna"].astype(float)
    df["Codigo_comuna"]=df["Codigo_comuna"].astype(int)
    return df

def edu_vial2018(df):
    df = df.drop(df.columns[[0,2,3,5,7,8,10,11,31,32,33,34,35]], axis=1)

def medevic_treatment():
    return 2
