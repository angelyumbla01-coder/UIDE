# =====================================================================
# ASIGNATURA: LÓGICA DE PROGRAMACIÓN
# ESTUDIANTE: ANGEL GABRIEL YUMBLA OCHOA
# ENTORNO: VISUAL STUDIO CODE + PYTHON
# PROYECTO: JUEGO "ADIVINA EL NÚMERO" (AVANCE CÓDIGO - PASO 1)
# =====================================================================
def jugar_adivina_el_numero():
    # --- CAPA DE DATOS (Variables iniciales del bloque de asignación de Raptor) ---
    rango_minimo = 1
    rango_maximo = 100
    contador_intentos = 0
    respuesta = ""

    # --- CAPA DE INTERFAZ (Mensaje de bienvenida e instrucciones) ---
    print("=====================================================")
    print("      BIENVENIDO AL JUEGO: ¡ADIVINA EL NÚMERO!      ")
    print("=====================================================")
    print("Piensa en un número entero entre 1 y 100.")
    print("El computador intentará adivinarlo basándose en tus respuestas.")
    print("=====================================================\n")
    # --- CAPA DE LÓGICA: BUCLE PRINCIPAL (Mapeo del Loop de Raptor) ---
    # El ciclo se repite hasta que se cumpla la condición de salida de Raptor
    while not (respuesta == "correcto" or rango_minimo > rango_maximo):
        
        # Cálculo del intento (Usa '//' para división entera, equivalente al 'floor' de Raptor)
        intento_actual = (rango_minimo + rango_maximo) // 2
        contador_intentos += 1

        # --- CAPA DE INTERFAZ: Salidas (PUT) y Entrada de datos (GET) ---
        print(f"Intento N° {contador_intentos}")
        print(f"¿Tu número es {intento_actual}?")
        respuesta = input("Escribe mayor, menor o correcto: ").strip().lower()
        print("-" * 50)

        # --- CAPA DE LÓGICA: Selección (Condicionales idénticos a los de Raptor) ---
        if respuesta == "correcto":
            print(f"¡Adivinado en {contador_intentos} intentos!")
            
        elif respuesta == "mayor":
            # Ajuste del límite inferior (camino del 'Yes' en Raptor)
            rango_minimo = intento_actual + 1
            
        elif respuesta == "menor":
            # Ajuste del límite superior (camino del 'Yes' en Raptor)
            rango_maximo = intento_actual - 1
            
        else:
            # Manejo de entradas inválidas y restauración del contador
            print("Por favor, ingresa una respuesta válida.")
            contador_intentos -= 1  # Resta 1 intento tal como pusiste en Raptor

    # --- EVALUACIÓN FINAL DE CONTRADICCIÓN (Fuera del bucle) ---
    if rango_minimo > rango_maximo:
        print("¡Error! Se detectó una contradicción en las respuestas.")

    print("\nFin del programa. ¡Gracias por jugar!")

# Punto de entrada para ejecutar el script directamente
if __name__ == "__main__":
    jugar_adivina_el_numero()