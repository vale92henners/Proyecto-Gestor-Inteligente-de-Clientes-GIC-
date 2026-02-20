import re

def validar_nombre(nombre):
    if len(nombre.strip()) < 3:
        raise ValueError("El nombre debe tener al menos 3 caracteres.")
    return True

def validar_email(email):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(patron, email):
        raise ValueError(f"El formato de correo '{email}' no es válido.")
    return True

def validar_saldo_positivo(monto):
    if monto < 0:
        raise ValueError("El monto no puede ser negativo.")
    return True