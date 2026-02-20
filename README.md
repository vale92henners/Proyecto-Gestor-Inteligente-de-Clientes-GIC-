Arquitectura y Diseño Orientado a Objetos
El sistema GIC se fundamenta en el paradigma de Programación Orientada a Objetos (POO), utilizando una estructura modular que separa la lógica de negocio de la persistencia. El núcleo del software es la clase base Cliente, la cual implementa el encapsulamiento mediante el atributo privado __saldo para proteger la integridad financiera de los registros. A partir de esta base, se aplica la herencia para crear las subclases ClienteNormal, ClienteVIP y ClienteCorporativo, permitiendo que cada una gestione atributos específicos, como el descuento premium o el RUT de empresa, de manera escalable.


Estrategia de Persistencia y Base de Datos
Siguiendo los principios de las bases de datos relacionales, el sistema organiza la información en tablas compuestas por filas (tuplas) y columnas (atributos), donde cada registro es identificado unívocamente mediante una clave primaria. La persistencia principal se realiza en SQLite, garantizando la integridad referencial y permitiendo consultas eficientes mediante SQL. Como complemento técnico, se ha implementado una persistencia secundaria en archivos JSON, lo que facilita el intercambio de datos semiestructurados y asegura la portabilidad de los respaldos fuera del motor de base de datos.


Interfaz, Validación y Control de Actividad
La interacción con el usuario se gestiona a través de una interfaz dinámica (CLI o Flask) que comunica las peticiones hacia los módulos de validación. Antes de que cualquier dato sea procesado por el RDBMS, el sistema ejecuta validaciones avanzadas para verificar el formato de los correos electrónicos y la positividad de los saldos, capturando cualquier anomalía mediante un manejo de excepciones estructurado. Finalmente, para garantizar la continuidad del negocio y la auditoría, se integra un registro de actividad (Logs) que documenta cada inserción, error o consulta realizada en el inventario de clientes.
