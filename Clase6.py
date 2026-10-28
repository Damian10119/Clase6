
# -- PROBLEMA 1: Control de temperatura en un edificio inteligente --

def leer_datos_sensores():
    # Simula la lectura de los sensores de cada zona.
    return [
        {"zona": "Oficina", "temperatura": 28,
         "ocupacion": True, "exterior": 32},
        {"zona": "Sala de reuniones", "temperatura": 19,
         "ocupacion": False, "exterior": 12}
    ]


def calcular_temperatura_optima(hora, ocupacion, exterior):
    # Ajusta la temperatura objetivo según la hora y la ocupación.
    if ocupacion:
        objetivo = 22 if 8 <= hora < 18 else 24
    else:
        objetivo = 26

    # Si hace mucho frío o calor afuera, se mantiene
    # el objetivo definido según el uso de la zona.
    return objetivo


def enviar_ajuste(zona, actual, objetivo):
    # Simula el envío de una orden de calefacción o refrigeración.
    if actual < objetivo:
        print(f"{zona}: activar calefacción hasta {objetivo} °C.")
    elif actual > objetivo:
        print(f"{zona}: activar refrigeración hasta {objetivo} °C.")
    else:
        print(f"{zona}: temperatura adecuada.")


def registrar_consumo(zona, kwh):
    # Registra y presenta el consumo energético de una zona.
    print(f"{zona}: consumo registrado de {kwh} kWh.")
    if kwh > 10:
        print("Advertencia: consumo energético elevado.")


# Programa principal: coordina las funciones.
if __name__ == "__main__":
    hora_actual = 10
    sensores = leer_datos_sensores()

    for sensor in sensores:
        objetivo = calcular_temperatura_optima(
            hora_actual,
            sensor["ocupacion"],
            sensor["exterior"]
        )

        enviar_ajuste(
            sensor["zona"],
            sensor["temperatura"],
            objetivo
        )

        # Consumo simulado para el ejemplo.
        registrar_consumo(sensor["zona"], 8.5)






# -- PROBLEMA 2: Gestión de inventario en un almacén --

def registrar_entrada(inventario, producto, cantidad):
    # Aumenta las existencias de un producto.
    if cantidad <= 0:
        print("La cantidad de entrada debe ser positiva.")
        return False

    inventario[producto] = inventario.get(producto, 0) + cantidad
    print(f"Entrada registrada: {cantidad} unidades de {producto}.")
    return True


def registrar_salida(inventario, producto, cantidad):
    # Reduce las existencias si hay suficiente inventario.
    if cantidad <= 0:
        print("La cantidad de salida debe ser positiva.")
        return False

    disponible = inventario.get(producto, 0)

    if cantidad > disponible:
        print(f"Stock insuficiente para {producto}.")
        return False

    inventario[producto] = disponible - cantidad
    print(f"Salida registrada: {cantidad} unidades de {producto}.")
    return True


def calcular_inventario_optimo(
    demanda_diaria, plazo_reposicion, stock_seguridad
):
    # Calcula el inventario objetivo según la demanda esperada.
    return demanda_diaria * plazo_reposicion + stock_seguridad


def generar_alerta(inventario, producto, nivel_optimo):
    # Advierte si las existencias están por debajo del objetivo.
    disponible = inventario.get(producto, 0)

    if disponible < nivel_optimo:
        faltante = nivel_optimo - disponible
        print(f"Alerta para {producto}: reponer {faltante} unidades.")
        return faltante

    print(f"{producto}: inventario suficiente.")
    return 0


# Programa principal.
if __name__ == "__main__":
    inventario = {"Cuadernos": 50, "Esferos": 20}

    registrar_entrada(inventario, "Cuadernos", 15)
    registrar_salida(inventario, "Esferos", 5)

    # Calculamos el objetivo para los cuadernos.
    objetivo = calcular_inventario_optimo(
        demanda_diaria=10,
        plazo_reposicion=5,
        stock_seguridad=10
    )

    generar_alerta(inventario, "Cuadernos", objetivo)

    print("Inventario final:", inventario)





# -- PROBLEMA 3: Sistema de navegación para un vehículo autónomo --

def leer_sensores():
    # Simula las lecturas de proximidad, cámara y tráfico.
    return {
        "distancia_obstaculo": 8,
        "camara_detecta_obstaculo": False,
        "trafico": "moderado"
    }


def calcular_ruta(origen, destino):
    # Simula la planificación de una ruta entre dos puntos.
    ruta = [origen, "Punto intermedio", destino]
    print("Ruta planificada:", " -> ".join(ruta))
    return ruta


def detectar_obstaculos(datos):
    # Combina las lecturas para decidir si existe un obstáculo.
    hay_obstaculo = (
        datos["distancia_obstaculo"] < 5
        or datos["camara_detecta_obstaculo"]
    )

    if hay_obstaculo:
        print("Obstáculo detectado: detener o cambiar la ruta.")
    else:
        print("Ruta despejada.")

    return hay_obstaculo


def ajustar_velocidad(trafico):
    # Selecciona una velocidad de ejemplo según el tráfico.
    velocidades = {
        "fluido": 60,
        "moderado": 40,
        "intenso": 20
    }

    velocidad = velocidades.get(trafico, 20)
    print(f"Velocidad recomendada: {velocidad} km/h.")
    return velocidad


# Programa principal.
if __name__ == "__main__":
    datos = leer_sensores()
    calcular_ruta("Punto A", "Punto B")

    obstaculo = detectar_obstaculos(datos)

    if not obstaculo:
        ajustar_velocidad(datos["trafico"])
    else:
        print("La velocidad debe ajustarse de forma segura.")
        




# -- PROBLEMA 4: Optimización de la producción en una fábrica

def monitorear_maquina(nombre, temperatura, horas_trabajo):
    # Evalúa indicadores básicos del estado de una máquina.
    estado = "Normal"

    if temperatura > 80 or horas_trabajo >= 500:
        estado = "Requiere revisión"

    print(f"Máquina {nombre}: {estado}.")
    return estado


def planificar_mantenimiento(nombre, estado):
    # Recomienda mantenimiento cuando se detecta una condición.
    if estado == "Requiere revisión":
        print(f"Programar mantenimiento para {nombre}.")
    else:
        print(f"{nombre}: no requiere mantenimiento inmediato.")


def analizar_rendimiento(unidades_producidas, horas_trabajo):
    # Calcula la producción promedio por hora.
    if horas_trabajo <= 0:
        print("Las horas de trabajo deben ser positivas.")
        return 0

    rendimiento = unidades_producidas / horas_trabajo
    print(f"Rendimiento: {rendimiento:.2f} unidades por hora.")
    return rendimiento


def ajustar_produccion(demanda, capacidad_actual):
    # Compara la demanda con la capacidad de producción.
    if demanda > capacidad_actual:
        print("Aumentar la programación de producción.")
    elif demanda < capacidad_actual:
        print("Reducir la programación para evitar excedentes.")
    else:
        print("Mantener la programación actual.")


# Programa principal.
if __name__ == "__main__":
    estado = monitorear_maquina("M1", 85, 300)
    planificar_mantenimiento("M1", estado)

    analizar_rendimiento(
        unidades_producidas=1200,
        horas_trabajo=40
    )

    ajustar_produccion(demanda=1500, capacidad_actual=1200)





# -- PROBLEMA 5: Sistema de riego automatizado --

def leer_humedad_suelo():
    # Simula las lecturas de humedad de varias secciones.
    return {
        "Sección A": 25,
        "Sección B": 45,
        "Sección C": 30
    }


def consultar_prevision():
    # Simula la previsión de lluvia para las próximas horas.
    return {"probabilidad_lluvia": 80, "lluvia_mm": 8}


def calcular_riego(humedad, lluvia_mm):
    # Decide la cantidad aproximada de agua que se aplicará.
    # Si el suelo ya está húmedo o se espera lluvia abundante,
    # se evita o reduce el riego.
    if humedad >= 40:
        return 0

    if lluvia_mm >= 5:
        return 0

    # Cada punto por debajo de 40 representa 0.5 litros/m²
    # en este modelo didáctico simplificado.
    return (40 - humedad) * 0.5


def controlar_valvula(seccion, litros_por_m2):
    # Simula la apertura o el cierre de la válvula de riego.
    if litros_por_m2 > 0:
        print(
            f"{seccion}: abrir válvula; "
            f"aplicar {litros_por_m2:.1f} litros/m²."
        )
        return True

    print(f"{seccion}: válvula cerrada; no regar.")
    return False


# Programa principal.
if __name__ == "__main__":
    humedades = leer_humedad_suelo()
    prevision = consultar_prevision()

    lluvia = prevision["lluvia_mm"]

    # Recorremos las secciones y calculamos su riego.
    for seccion, humedad in humedades.items():
        cantidad = calcular_riego(humedad, lluvia)
        controlar_valvula(seccion, cantidad)
