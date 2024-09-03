""" Modulo 1 - Gestion de paquetes turisticos (Creacion, edicion, reserva y eliminación)"""
# Inicialización de la lista de paquetes ya quemados
lista_paquetes = [
    {"destino": "París",
    "fechas": "01/10/2024 - 10/10/2024", 
    "precio": 1200.00, 
    "descripcion": "Paquete de 10 días en París"
    },
    {"destino": "Londres",
    "fechas": "05/11/2024 - 15/11/2024", 
    "precio": 1500.00, 
    "descripcion": "Paquete de 10 días en Londres"
    },
    {"destino": "Tokio",
    "fechas": "20/12/2024 - 30/12/2024", 
    "precio": 1800.00, 
    "descripcion": "Paquete de 10 días en Tokio"},
    {"destino": "Nueva York",
    "fechas": "10/01/2025 - 20/01/2025", 
    "precio": 1600.00, 
    "descripcion": "Paquete de 10 días en Nueva York"
    },
    {"destino": "Sídney",
    "fechas": "15/02/2025 - 25/02/2025", 
    "precio": 2000.00, 
    "descripcion": "Paquete de 10 días en Sídney"},
    {"destino": "Barcelona",
    "fechas": "01/03/2025 - 10/03/2025", 
    "precio": 1400.00, 
    "descripcion": "Paquete de 10 días en Barcelona"}
]
# Lista donde se guardaran todos los datos de un paquete que se haya reservado
lista_reservas = []
claveAdministrador = 1234

while True:
    # Mostrar menú de opciones
    print("\n1. Crear Paquete Turístico")
    print("2. Buscar Paquete Turístico")
    print("3. Eliminar Paquete Turístico")
    print("4. Reservar Paquete Turístico")
    print("5. Ver Reservas")
    print("6. Salir")
    # Seleccionar un numero para ingresar a ese menu
    opcion = input("Selecciona una opción: ")
#*------------------------------------------------------------------
    # Creación de nuevos paquetes por parte del administrador
    if opcion == "1":
        # verificar que es el administrador es quien desea crear un paquete
        claveIngresada = int(input("Ingrese la clave de administrador: "))
        if claveIngresada == claveAdministrador:
            print("\nPor favor, ingrese la información para el nuevo paquete turístico.")
            destino = input("Ingrese el destino: ").strip()
            fechas = input("Ingrese las fechas con formato DD/MM/AA: ").strip()
            precio = input("Ingrese el precio: ").strip()
            descripcion = input("Ingrese la descripcion: ").strip()
            # Validar que todos los campos estén completos
            # Si al menos uno de los campos está vacío, se muestra un mensaje de error y el paquete no se crea.
            if not destino or not fechas or not precio or not descripcion:
                print("Error: Todos los campos son obligatorios. Intente nuevamente.")
                continue
            else:
                # Convertir precio a un número flotante
                try:
                    precio = float(precio)
                except ValueError:
                    print("Error: El precio debe ser un número.")
                    continue

            paquete = {
                "destino": destino,
                "fechas": fechas,
                "precio": precio,
                "descripcion": descripcion
            }

            lista_paquetes.append(paquete)
            print("Paquete creado exitosamente.")
        else:
            print("Clave incorrecta")
#*------------------------------------------------------------------
    # Busqueda de paquetes disponibles por parte del usuario
    elif opcion == "2":
    # Visualizar todos los destinos actuales
    # Para facilitar la selección y búsqueda del paquete al usuario.
        if lista_paquetes:
            print("\nDestinos disponibles:")
            for paquete in lista_paquetes:
                print(f"- {paquete['destino']}")
        # Buscar Paquete.
        destino_busqueda = input("Ingrese el destino para ver el paquete: ")
        # La variable "encontrado" la utilizamos para verificar si se encontro o no el paquete e imprimir el mensaje de paquete no encontrado
        encontrado = False

        for paquete in lista_paquetes:
            if paquete["destino"].lower() == destino_busqueda.lower():
                print(f"Destino: {paquete['destino']}, Fechas: {paquete['fechas']}, Precio: {paquete['precio']}")
                print(f"Descripción: {paquete['descripcion']}")
                encontrado = True
                break
        if not encontrado:
            print("Paquete no encontrado.")
#*------------------------------------------------------------------
    elif opcion == "3":
        # Eliminar paque turistico por parte del administrador
        # verificar que es el administrador quien desea eliminar un paquete
        claveIngresada = int(input("Ingrese la clave de administrador: "))
        if claveIngresada == claveAdministrador:
            destino_eliminar = input("Ingrese el destino del paquete a eliminar")
            eliminado = False

            for paquete in lista_paquetes:
                if paquete["destino"].lower() == destino_eliminar.lower():
                    lista_paquetes.remove(paquete)
                    print(f"paquete {destino_eliminar} eliminado exitosamente.")
                    eliminado = True
                    break
            if not eliminado:
                print("Paquete no encontrado")
        else:
            print("Clave incorrecta")
# Fin