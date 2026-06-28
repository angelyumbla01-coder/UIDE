# =====================================================================
# ASIGNATURA: LÓGICA DE PROGRAMACIÓN
# ESTUDIANTE: ANGEL GABRIEL YUMBLA OCHOA
# ENTORNO: VISUAL STUDIO CODE + PYTHON
# TRABAJO: DESARROLLO DEL PROGRAMA AL 100% (PASO 2)
# =====================================================================

def mostrar_bienvenida():
    """
    Capa de Interfaz: Muestra las instrucciones iniciales del juego.
    """
    print("\n" + "="*55)
    print("      BIENVENIDO AL JUEGO: ¡ADIVINA EL NÚMERO!      ")
    print("="*55)
    print(" Piensa en un número entero entre 1 y 100.")
    print(" El computador intentará adivinarlo basándose en tus pistas.")
    print(" Contesta de forma honesta con:")
    print("   -> 'mayor'    (si tu número es más alto)")
    print("   -> 'menor'    (si tu número es más bajo)")
    print("   -> 'correcto' (si el computador acertó)")
    print("="*55 + "\n")


def obtener_respuesta_valida(contador):
    """
    Control de Excepciones y Validación: Asegura que el usuario ingrese
    únicamente opciones válidas, evitando fallas por tipeo.
    """
    opciones_validas = ["mayor", "menor", "correcto"]
    while True:
        # Captura de datos eliminando espacios y convirtiendo a minúsculas
        entrada = input(f"Intento N° {contador} | Escribe (mayor / menor / correcto): ").strip().lower()
        
        if entrada in opciones_validas:
            return entrada
        
        # Alerta de error si introduce un comando inexistente
        print("[Alerta] Entrada no válida. Por favor, verifica tu escritura.\n")


def ejecutar_logica_juego():
    """
    Capa de Lógica y Datos: Controla el núcleo del algoritmo de búsqueda binaria
    y gestiona las variables de control y contradicciones.
    """
    # Inicialización de variables (Capa de Datos)
    rango_minimo = 1
    rango_maximo = 100
    contador_intentos = 0
    respuesta = ""

    # Bucle principal de control
    while rango_minimo <= rango_maximo:
        # Cálculo matemático del intento por división entera (Búsqueda Binaria)
        intento_actual = (rango_minimo + rango_maximo) // 2
        contador_intentos += 1

        print(f"¿El número que pensaste es el: {intento_actual}?")
        
        # Invocación de la función de validación de interfaz
        respuesta = obtener_respuesta_valida(contador_intentos)
        print("-" * 55)

        # Estructuras lógicas condicionales
        if respuesta == "correcto":
            print(f"\n🎯 ¡LOGRADO! El sistema adivinó tu número en {contador_intentos} intentos.")
            return  # Finalización exitosa del juego
            
        elif respuesta == "mayor":
            # Descarta el segmento inferior reajustando el límite mínimo
            rango_minimo = intento_actual + 1
            
        elif respuesta == "menor":
            # Descarta el segmento superior reajustando el límite máximo
            rango_maximo = intento_actual - 1

    # --- CONTROL DE CONTRADICCIONES (Criterio de Evaluación Evaluado) ---
    # Si los límites se cruzan, significa que hubo respuestas contradictorias del usuario
    if rango_minimo > rango_maximo:
        print("\n❌ [Error de Contradicción] Es imposible adivinar el número.")
        print("Las pistas proporcionadas se contradicen entre sí (ej. decir que es mayor y menor a la vez).")


def main():
    """
    Controlador Principal: Administra la ejecución secuencial del programa.
    """
    mostrar_bienvenida()
    ejecutar_logica_juego()
    print("\n=====================================================")
    print("  Programa finalizado con éxito. ¡Gracias por jugar!  ")
    print("=====================================================\n")


if __name__ == "__main__":
    main()
    