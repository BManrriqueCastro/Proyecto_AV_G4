import datetime


class Cliente:
    def __init__(self, nombre, correo_electronico):
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.historial_reservas = []
        self.preferencias = {}
        self.comentarios = []
        self.historial_contacto = []

    def agregar_reserva(self, reserva):
        self.historial_reservas.append(reserva)

    def agregar_preferencia(self, clave, valor):
        self.preferencias[clave] = valor

    def agregar_comentario(self, comentario):
        self.comentarios.append(comentario)

    def registrar_contacto(self, tipo_contacto, fecha, detalles):
        self.historial_contacto.append(
            {"tipo_contacto": tipo_contacto, "fecha": fecha, "detalles": detalles}
        )


class Reserva:
    def __init__(self, destino, fecha, tipo_paquete):
        self.destino = destino
        self.fecha = fecha
        self.tipo_paquete = tipo_paquete


class RecordatorioViaje:
    def __init__(self, cliente, reserva):
        self.cliente = cliente
        self.reserva = reserva
        self.fecha_recordatorio = None

    def establecer_recordatorio(self, fecha_recordatorio):
        self.fecha_recordatorio = fecha_recordatorio


class OfertaEspecial:
    def __init__(self, descripcion, condiciones):
        self.descripcion = descripcion
        self.condiciones = condiciones

    def aplicar_oferta(self, cliente):
        # Implementar lógica para aplicar la oferta a un cliente
        pass


class AsesorDeViajes:
    def __init__(self):
        self.clientes_vip = []

    def agregar_cliente_vip(self, cliente):
        self.clientes_vip.append(cliente)

    def recomendar_oferta(self, cliente):
        # Implementar lógica de recomendación personalizada basada en el historial y preferencias
        pass


# Ejemplo de uso

# Crear clientes
cliente1 = Cliente("Juan Pérez", "juan.perez@example.com")
cliente2 = Cliente("Ana Gómez", "ana.gomez@example.com")

# Agregar reservas
reserva1 = Reserva("Cancún", datetime.date(2024, 12, 15), "Todo Incluido")
cliente1.agregar_reserva(reserva1)

# Agregar preferencias
cliente1.agregar_preferencia("actividades_favoritas", ["buceo", "senderismo"])
cliente1.agregar_preferencia("tipo_alojamiento", "resort")

# Registrar comentario
cliente1.agregar_comentario("Excelente servicio en el último viaje.")

# Registrar contacto
cliente1.registrar_contacto(
    "Correo Electrónico",
    datetime.date(2024, 8, 30),
    "Enviado oferta de vacaciones de verano.",
)

# Crear recordatorio de viaje
recordatorio = RecordatorioViaje(cliente1, reserva1)
recordatorio.establecer_recordatorio(datetime.date(2024, 12, 10))

# Crear oferta especial
oferta = OfertaEspecial(
    "Descuento del 20% en el próximo viaje",
    {"requisito": "reservar antes del 30 de septiembre"},
)

# Asesor de viajes
asesor = AsesorDeViajes()
asesor.agregar_cliente_vip(cliente1)

# Ejemplo de recomendaciones (vacío en este caso)
asesor.recomendar_oferta(cliente1)
