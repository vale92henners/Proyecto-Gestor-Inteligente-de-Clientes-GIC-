import logging
from models.cliente import Cliente
from models.tipos_clientes import ClienteVIP, ClienteCorporativo, ClienteNormal
from database.db_sqlite import crear_tabla, guardar_cliente_db, obtener_clientes_db
from utils.validaciones import validar_nombre, validar_email, validar_saldo_positivo
from database.gestor_archivos import guardar_datos_json, cargar_datos_json


logging.basicConfig(
    filename='actividad.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def ejecutar_gic():
    """Función principal del Gestor Inteligente de Clientes (GIC)."""
    
    crear_tabla() 
    
    
    clientes = obtener_clientes_db()
    if not clientes:
        clientes = cargar_datos_json()
        if clientes:
            print("📂 Datos recuperados desde el respaldo JSON.")

    while True:
        
        print("\n" + "═"*45)
        print("   🚀 SISTEMA GESTOR DE CLIENTES (GIC)")
        print("═"*45)
        print(" 1. 👤 Registrar Nuevo Cliente")
        print(" 2. 📋 Listar Clientes (Vista Polimórfica)")
        print(" 3. 📂 Sincronizar Respaldo JSON")
        print(" 4. ❌ Salir del Sistema")
        print("═"*45)
        
        opcion = input("➤ Seleccione una opción: ").strip()

        if opcion == "1":
            try:
               
                nom = input("Nombre completo: ").strip()
                validar_nombre(nom)
                
                ema = input("Email de contacto: ").strip()
                validar_email(ema)
                
                sal_raw = input("Saldo inicial: ").strip()
                sal = float(sal_raw)
                validar_saldo_positivo(sal)

                print("\nTipos: [N] Normal, [V] VIP, [C] Corporativo [cite: 28]")
                tipo_input = input("Seleccione tipo: ").upper().strip()
                
                
                if tipo_input == "V":
                    nuevo = ClienteVIP(nom, ema, sal)
                elif tipo_input == "C":
                    rut = input("RUT Empresa: ").strip()
                    nuevo = ClienteCorporativo(nom, ema, sal, rut)
                else:
                    nuevo = ClienteNormal(nom, ema, sal)

               
                guardar_cliente_db(nuevo)   
                clientes.append(nuevo)      
                logging.info(f"Registro exitoso: {ema} (Tipo: {tipo_input})")
                
                print(f"\n✅ Cliente '{nom}' registrado correctamente.")

            except ValueError as e:
                logging.warning(f"Error de validación: {e}") 
                print(f"\n⚠️ Error de validación: {e}") 
            except Exception as e:
                logging.error(f"Error crítico: {e}") 
                print(f"\n❌ Error inesperado: {e}")
                    
        elif opcion == "2":
            print("\n" + "─"*45)
            print("         INVENTARIO DE CLIENTES")
            print("─"*45)
            if not clientes:
                print("   (No hay clientes registrados)")
            else:
               
                for c in clientes:
                    print(c) 
            print("─"*45)

        elif opcion == "3":
           
            if clientes:
                guardar_datos_json(clientes)
                print("\n📂 Archivo 'lista clientes.json' actualizado correctamente.")
                logging.info("Sincronización manual de JSON realizada.")
            else:
                print("\n⚠️ No hay datos para exportar.")

        elif opcion == "4":
            print("\n👋 Cerrando sesión. ¡Éxitos en SolutionTech!")
            logging.info("Sistema cerrado por el usuario.")
            break
        
        else:
            print("\n⚠️ Opción no válida. Intente del 1 al 4.")

if __name__ == "__main__":
    ejecutar_gic()