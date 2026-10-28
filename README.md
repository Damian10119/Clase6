# Actividad 4: Funciones y procedimientos en Python

## 1. Introducción

Esta actividad aplica los conceptos de modularidad, funciones y procedimientos mediante cinco problemas relacionados con sistemas inteligentes, inventarios, navegación, producción industrial y agricultura.

La modularidad consiste en dividir un programa en funciones independientes, cada una encargada de una tarea específica. Esto facilita la reutilización del código, su mantenimiento y la detección de errores.



## 2. Descripción de los problemas

### Problema 1: Control de temperatura

- `leer_datos_sensores()`: obtiene las lecturas simuladas de temperatura y ocupación.
- `calcular_temperatura_optima()`: determina la temperatura objetivo según la hora y la ocupación.
- `enviar_ajuste()`: simula la activación de calefacción o refrigeración.
- `registrar_consumo()`: presenta el consumo y genera advertencias.

La separación de estas funciones facilita actualizar los criterios de climatización y analizar el consumo por zona.

### Problema 2: Gestión de inventario

- `registrar_entrada()`: incrementa las existencias y valida la cantidad ingresada.
- `registrar_salida()`: comprueba el stock disponible antes de descontar unidades.
- `calcular_inventario_optimo()`: calcula el nivel objetivo según la demanda, el plazo de reposición y el stock de seguridad.
- `generar_alerta()`: calcula las unidades necesarias para alcanzar el nivel objetivo.

El uso de un diccionario permite consultar y modificar las existencias por producto con un costo promedio constante.

### Problema 3: Sistema de navegación

- `leer_sensores()`: simula las lecturas de proximidad, cámara y tráfico.
- `calcular_ruta()`: genera una ruta de ejemplo entre un origen y un destino.
- `detectar_obstaculos()`: evalúa las lecturas para determinar si existe un obstáculo.
- `ajustar_velocidad()`: recomienda una velocidad según las condiciones del tráfico.

La modularidad permite mejorar cada componente de navegación de forma independiente. El ejemplo es didáctico y no constituye un sistema de conducción autónoma real.

### Problema 4: Optimización de producción

- `monitorear_maquina()`: evalúa la temperatura y las horas de trabajo.
- `planificar_mantenimiento()`: recomienda mantenimiento cuando la máquina necesita revisión.
- `analizar_rendimiento()`: calcula las unidades producidas por hora.
- `ajustar_produccion()`: compara la demanda con la capacidad actual.

Esta organización facilita reutilizar las funciones con distintas máquinas y modificar los criterios de producción.

### Problema 5: Sistema de riego automatizado

- `leer_humedad_suelo()`: simula la lectura de humedad de varias secciones.
- `consultar_prevision()`: devuelve datos meteorológicos simulados.
- `calcular_riego()`: estima la cantidad de agua necesaria según la humedad y la lluvia prevista.
- `controlar_valvula()`: simula la apertura o el cierre de las válvulas.

La separación de tareas permite cambiar los criterios de riego y añadir nuevos sensores sin reescribir el programa completo.

## 4. Modularidad y rendimiento

Las funciones evitan duplicar lógica y facilitan las pruebas independientes. Cuando una función procesa una sola zona, producto, máquina o sección, normalmente realiza una cantidad constante de operaciones, es decir, O(1).

Cuando el programa recorre una colección de n elementos y ejecuta un número constante de operaciones por elemento, el tiempo de procesamiento suele ser O(n).

La modularidad no garantiza por sí sola que un programa sea más rápido, pero ayuda a identificar operaciones redundantes, elegir estructuras de datos adecuadas y mantener un código organizado.

