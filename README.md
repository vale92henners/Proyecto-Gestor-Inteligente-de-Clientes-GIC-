# 🛠️ Documentación Técnica: Sistema GIC

## 1. Arquitectura y Diseño Orientado a Objetos
El sistema **GIC** se fundamenta en el paradigma de **Programación Orientada a Objetos (POO)** , utilizando una estructura modular que separa la lógica de negocio de la persistencia. 

* **Núcleo del Software**: Se define en la clase base `Cliente`, la cual implementa el **encapsulamiento** mediante el atributo privado `__saldo` para proteger la integridad financiera de los registros. 
* **Estructura de Herencia**: A partir de esta base, se aplica la herencia para crear las subclases `ClienteNormal`, `ClienteVIP` y `ClienteCorporativo`.
* **Escalabilidad**: Esta arquitectura permite que cada subclase gestione atributos específicos, como el descuento premium o el RUT de empresa, de manera eficiente.



---

## 2. Estrategia de Persistencia y Base de Datos
Siguiendo los principios de las **bases de datos relacionales** , el sistema organiza la información en tablas compuestas por filas (**tuplas**) y columnas (**atributos**) , donde cada registro es identificado unívocamente mediante una **clave primaria**.

## 📊 Modelos de Almacenamiento
1. **SQLite (Principal)**: Garantiza la integridad referencial y permite consultas eficientes mediante el lenguaje **SQL**.
2. **JSON (Secundaria)**: Implementada para facilitar el intercambio de datos semiestructurados y asegurar la portabilidad de los respaldos fuera del motor de base de datos.

---

## 3. Interfaz, Validación y Control de Actividad
[cite_start]La interacción con el usuario se gestiona a través de una interfaz dinámica (**CLI o Flask**) que comunica las peticiones hacia los módulos de validación. 

* **Validaciones Avanzadas**: Antes de que cualquier dato sea procesado por el **RDBMS** , el sistema verifica el formato de los correos electrónicos y la positividad de los saldos.
* **Gestión de Errores**: Se capturan anomalías mediante un manejo de excepciones estructurado.
* **Auditoría y Continuidad**: Para garantizar la seguridad, se integra un registro de actividad (**Logs**) que documenta cada inserción, error o consulta realizada en el inventario de clientes.

* ![Diagrama de Clases - Sistema de Clientes](diagrama%20uml.png)
