import requests
import json
import os 
import autoit as a
from json.decoder import JSONDecodeError
from tkinter import messagebox as MessageBox
from time import sleep



#region URL

url = 'http://192.168.50.33/api/Rpa_izzi_depuracion_api/getOrden2'
urlCN = 'http://192.168.50.33/api/Rpa_izzi_depuracion_api/saveCN'
urlOrden = 'http://192.168.50.33/api/Rpa_izzi_depuracion_api/updateOrden'





def get_obterner_datos():
    try:
        response = requests.get(url) 
        if response.status_code == 200:
            reseponseApi = json.loads(response.text)
            return reseponseApi

        elif response.status_code == 401:
            return print("Unauthorized")

        elif response.status_code == 404:
            return print("Not Found")

        elif response.status_code == 500:
            return print("Internal Server Error")

    except JSONDecodeError:
        return response.body_not_json

#endregion


#region Orden de Servicio 

def update(datos):

    try:
        response = requests.put(urlOrden, data=datos)
        if response.status_code == 200:
            responseApi = json.loads(response.text)
            return responseApi

        elif response.status_code == 401:
            return print("Unauthorized")

        elif response.status_code == 404:
            return print("Not Found")

        elif response.status_code == 500:
            return print("Internal Server Error")

    except JSONDecodeError:
            return response.body_not_json

def orden_cerrada(id_lead,source_id):
    datos = {
        "source_id":source_id,
        "lead_id":id_lead,
        "error": False,
        "code": 1
        }                      
    return update(datos)

def cuenta_erronea(id_lead,source_id):
    datos = {
        "source_id":source_id,
        "lead_id":id_lead,
        "error": False,
        "code": 3
        }                     
    return update(datos)

def cuenta_trabaja_izzi(id_lead,source_id):
    datos = {
        "source_id":source_id,
        "lead_id":id_lead,
        "error": False,
        "code": 4
        }                      
    return update(datos)

def cuenta_errorsiebel(id_lead,source_id):
    datos = {
        "source_id":source_id,
        "lead_id":id_lead,
        "error": False,
        "code": 5
        }                      
    return update(datos)

def api_sin_datos():
    datos = {
            "lead_id":0,
            "error": False,
            "code": 4}                       
    return update(datos)
#endregion


#region Caso de Negocio Apis

def update_cn(datos):

    try:
        response = requests.put(urlCN, data=datos)
        if response.status_code == 200:
            print(response.text)
            responseApi = json.loads(response.text)
            return responseApi

        elif response.status_code == 401:
            return print("Unauthorized")

        elif response.status_code == 404:
            return print("Not Found")

        elif response.status_code == 500:
            return print("Internal Server Error")

    except JSONDecodeError:
            return response.body_not_json

def caso_negocio_cerrado(id_lead,source_id,cn):
    datos = {
        "source_id":source_id,
        "lead_id":id_lead,
        "cn_generado":cn,
        "error": False,
        "code": 1
        }                      
    return update_cn(datos)

def caso_negocio_existe(id_lead,source_id,cn):
    datos = {
        "source_id":source_id,
        "lead_id":id_lead,
        "cn_generado":cn,
        "error": True,
        "code": 2
        }                      
    return update_cn(datos)

#endregion