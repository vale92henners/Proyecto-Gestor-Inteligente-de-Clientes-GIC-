import json
import os
from models.tipos_clientes import ClienteVIP, ClienteCorporativo, ClienteNormal

# Definimos la ruta del archivo
FILE_NAME = "database/lista clientes.json"

def guardar_datos_json(lista_clientes):
    """Transforma objetos de Python a un archivo JSON estructurado."""
    try:
        # Creamos una lista de diccionarios para el JSON
        data_serializada = []
        for c in lista_clientes:
            datos = {
                "nombre": c.nombre,
                "email": c.email,
                "saldo": c.saldo,
                "tipo": type(c).__name__ # Guardamos el nombre de la clase
            }
            # Si es corporativo, incluimos su atributo único
            if isinstance(c, ClienteCorporativo):
                datos["rut_empresa"] = c.rut_empresa
            
            data_serializada.append(datos)

       
        with open(FILE_NAME, "w", encoding='utf-8') as f:
            json.dump(data_serializada, f, indent=4, ensure_ascii=False)
        print(f"✅ Sincronización exitosa en: {FILE_NAME}")
        
    except Exception as e:
        print(f"❌ Error al exportar JSON: {e}")

def cargar_datos_json():

    lista_objetos = []
    if not os.path.exists(FILE_NAME):
        return lista_objetos

    try:
        with open(FILE_NAME, "r", encoding='utf-8') as f:
            datos = json.load(f)
            for d in datos:
                
                if d["tipo"] == 'ClienteVIP':
                    lista_objetos.append(ClienteVIP(d["nombre"], d["email"], d["saldo"]))
                elif d["tipo"] == 'ClienteCorporativo':
                    lista_objetos.append(ClienteCorporativo(d["nombre"], d["email"], d["saldo"], d.get("rut_empresa", "N/A")))
                else:
                    lista_objetos.append(ClienteNormal(d["nombre"], d["email"], d["saldo"]))
    except Exception as e:
        print(f"❌ Error al cargar JSON: {e}")
    return lista_objetos
