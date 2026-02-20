import sqlite3
from models.cliente import Cliente
from models.tipos_clientes import ClienteVIP, ClienteCorporativo, ClienteNormal

def conectar():
    return sqlite3.connect('gestion_clientes.db')

def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            saldo REAL NOT NULL,
            tipo TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def guardar_cliente_db(cliente):
    conn = conectar()
    cursor = conn.cursor()
    tipo = type(cliente).__name__
    try:
        cursor.execute('''
            INSERT INTO clientes (nombre, email, saldo, tipo)
            VALUES (?, ?, ?, ?)
        ''', (cliente.nombre, cliente.email, cliente.saldo, tipo))
        conn.commit()
    except sqlite3.IntegrityError:
        raise ValueError(f"El email '{cliente.email}' ya está registrado.")
    finally:
        conn.close()

def obtener_clientes_db():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT nombre, email, saldo, tipo FROM clientes')
    filas = cursor.fetchall()
    
    lista = []
    for f in filas:
        n, e, s, t = f
        if t == 'ClienteVIP':
            lista.append(ClienteVIP(n, e, s))
        elif t == 'ClienteCorporativo':
            lista.append(ClienteCorporativo(n, e, s, "RUT-EMPRESA"))
        elif t == 'ClienteNormal':
            lista.append(ClienteNormal(n, e, s))
        else:
            lista.append(Cliente(n, e, s))
    conn.close()
    return lista