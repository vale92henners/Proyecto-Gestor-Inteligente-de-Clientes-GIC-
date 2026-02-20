# 🛠️ Documentación Técnica: Sistema GIC

## 1. Arquitectura y Diseño Orientado a Objetos
El sistema **GIC** se fundamenta en el paradigma de **Programación Orientada a Objetos (POO)** , utilizando una estructura modular que separa la lógica de negocio de la persistencia. 

* **Núcleo del Software**: Se define en la clase base `Cliente`, la cual implementa el **encapsulamiento** mediante el atributo privado `__saldo` para proteger la integridad financiera de los registros. 
* **Estructura de Herencia**: A partir de esta base, se aplica la herencia para crear las subclases `ClienteNormal`, `ClienteVIP` y `ClienteCorporativo`.
* **Escalabilidad**: Esta arquitectura permite que cada subclase gestione atributos específicos, como el descuento premium o el RUT de empresa, de manera eficiente.



---

## 2. Estrategia de Persistencia y Base de Datos
[cite_start]Siguiendo los principios de las **bases de datos relacionales** [cite: 93, 182][cite_start], el sistema organiza la información en tablas compuestas por filas (**tuplas**) y columnas (**atributos**) [cite: 183, 184][cite_start], donde cada registro es identificado unívocamente mediante una **clave primaria**[cite: 131, 245].

> ### 📊 Modelos de Almacenamiento
> [cite_start]1. **SQLite (Principal)**: Garantiza la integridad referencial y permite consultas eficientes mediante el lenguaje **SQL**[cite: 19, 37, 286].
> [cite_start]2. **JSON (Secundaria)**: Implementada para facilitar el intercambio de datos semiestructurados y asegurar la portabilidad de los respaldos fuera del motor de base de datos[cite: 19, 30, 38].

---

## 3. Interfaz, Validación y Control de Actividad
[cite_start]La interacción con el usuario se gestiona a través de una interfaz dinámica (**CLI o Flask**) [cite: 20, 31] que comunica las peticiones hacia los módulos de validación. 

* [cite_start]**Validaciones Avanzadas**: Antes de que cualquier dato sea procesado por el **RDBMS** [cite: 553, 582][cite_start], el sistema verifica el formato de los correos electrónicos y la positividad de los saldos[cite: 18, 29, 61].
* [cite_start]**Gestión de Errores**: Se capturan anomalías mediante un manejo de excepciones estructurado[cite: 18, 40, 71].
* [cite_start]**Auditoría y Continuidad**: Para garantizar la seguridad, se integra un registro de actividad (**Logs**) que documenta cada inserción, error o consulta realizada en el inventario de clientes[cite: 21, 33, 72].
