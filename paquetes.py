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
# Fin