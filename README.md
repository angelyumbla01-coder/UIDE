# EVALUACION EN CONTACTO CO EL DOCENTE

# Proyecto: Juego "Adivina el Número" 

##  INTEGRANTES
* **ESTUDIANTE:** Angel Gabriel Yumbla Ochoa
* **DOCENTE:** Monica Patricia Salazar Tapia

##  Objetivo del Sistema
El propósito de este software es implementar un algoritmo optimizado e interactivo basado en la **Búsqueda Binaria**, donde el computador tiene la tarea de adivinar un número entero pensado por el usuario dentro de un rango preestablecido de 1 a 100. Reduciendo dinámicamente el espacio de búsqueda a la mitad en cada ciclo según la retroalimentación provista ("mayor", "menor" o "correcto"), el sistema garantiza resolver el juego en la menor cantidad de intentos posibles, minimizando fallas operativas y manejando escenarios lógicos complejos.

##  Descripción de Funcionalidades
El software desarrollado al 100% integra las siguientes capacidades lógicas y estructurales:
1. **Cálculo Matemático Optimizado:** Aplica una división entera (// 2) sobre los límites del juego para proponer de forma exacta el número medio remanente, asegurando la eficiencia matemática del algoritmo.
2. **Conteo Dinámico de Intentos:** Almacena un registro incremental cada vez que el computador propone una solución, permitiendo medir de forma exacta el desempeño en la ejecución final.
3. **Escudo de Validación de Respuestas:** Filtra de forma estricta las entradas del usuario. Si este escribe comandos con errores ortográficos o caracteres extraños, la interfaz limpia el texto y vuelve a solicitarlo sin penalizar el conteo de intentos.
4. **Manejo Explícito de Contradicciones:** Si las pistas otorgadas por el usuario se cruzan de forma ilógica (ej. cuando el valor mínimo calculado supera al máximo), el programa intercepta esta condición de frontera, detiene el bucle y emite una alerta detallada de error para evitar ciclos infinitos.
5. **Arquitectura Modular Separada:** El código en Python se ha construido de manera organizada en funciones independientes (mostrar_bienvenida, "obtener_respuesta_valida", "ejecutar_logica_juego") para cumplir con altos estándares de mantenimiento y legibilidad de software.

## FECHA DE ENTREGA 
28 DE JUNIO DEL 2026
