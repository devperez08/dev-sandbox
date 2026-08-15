# ==============================================================================
# CALCULADORA INTERACTIVA DE DESCUENTOS
# Tiempo estimado: 30 minutos
# Temas clave: Variables, Tipos de datos, Operadores, Condicionales, Input/Output
# ==============================================================================
#
# DESCRIPCIÓN DEL PROBLEMA:
# Crea un programa interactivo en el que un usuario introduce el precio original 
# de un artículo y la categoría a la que pertenece ("Ropa", "Electrónica", 
# "Alimentos", "Otros"). 
# Dependiendo de la categoría, el programa debe aplicar un porcentaje de 
# descuento diferente al precio original:
# - "Ropa": 15% de descuento
# - "Electrónica": 10% de descuento
# - "Alimentos": 5% de descuento
# - "Otros": 0% de descuento (sin descuento)
#
# Además, si el precio final después del descuento supera los $100, se debe aplicar 
# un descuento adicional fijo de $5 sobre el total de la compra.
#
# REQUISITOS DEL RESULTADO ESPERADO (DETALLADO):
# 1. Solicitar por consola al usuario el precio original del producto (debe permitir decimales).
# 2. Solicitar por consola la categoría del producto (no debe ser sensible a mayúsculas/minúsculas,
#    por ejemplo, "ropa" o "ROPA" deben ser válidas).
# 3. Validar las entradas del usuario:
#    - Si el precio es menor o igual a 0, el programa debe mostrar un mensaje de error y terminar.
#    - Si la categoría no es una de las cuatro opciones válidas, se debe asumir la categoría "Otros" 
#      e informar de ello al usuario mediante un mensaje.
# 4. Mostrar de forma clara en pantalla:
#    - El precio original.
#    - El descuento aplicado por categoría (porcentaje y valor en dinero).
#    - Si califica para el descuento adicional de $5 por superar los $100 finales.
#    - El precio final neto a pagar.
#
# EJEMPLO DE EJECUCIÓN ESPERADO:
# Precio original: 120
# Categoría: Ropa
#
# --- RESULTADO ---
# Precio original: $120.0
# Descuento por categoría (Ropa - 15%): $18.0
# Descuento adicional ($5 por compra > $100): Sí aplicado
# Precio Final: $97.0
# ==============================================================================

# Escribe tu solución a partir de aquí:

while True:

    precio = 0
    categoria = ""

    try:    
        precio = float(input("Ingresar precio: "))
        categoria = input("ingrese categoria: ").lower()
    except ValueError:
        print("el precio no es valido")
        continue

    if precio <= 0:
        print("el precio no es valido")
        precio = float(input("ingrese un precio valido: "))
    elif categoria not in ["ropa", "electronica", "alimentos", "otros"]: # not in es para validar que no este en la lista
        descuento = 0
        print("categoria no encontrada, se asume como otros")
        categoria = "otros"
    elif categoria == "ropa":
        descuento = precio * 0.15
    elif categoria == "electronica":
        descuento = precio * 0.10
    elif categoria == "alimentos":
        descuento = precio * 0.05
    else:
        descuento = 0

    precio_final = precio - descuento

    if precio_final > 100:
        descuento += 5
        precio_final -= 5

    print("Precio original: ", precio)
    print("Descuento por categoria: ", categoria," - ", descuento)
    print("Precio final: ", precio_final)

    opcion = input("desea salir? (y/n): ").lower()
    if opcion == "y":
        break

# ==============================================================================
# SUGERENCIAS TUTOR - RETROALIMENTACIÓN FINAL:
# ¡Excelente trabajo! Lograste resolver de manera muy efectiva todos los puntos.
# 
# Puntos clave logrados:
# 1. Uso de `try/except` para prevenir que letras crashearan el programa.
# 2. Control de salida del bucle con el menú `desea salir?`.
# 3. Inicialización previa de `precio = 0` y `categoria = ""` para evitar errores de ámbito.
#
# Observación final para reflexionar (UX - Experiencia de Usuario):
# 1. En la línea `if precio <= 0:`, usaste `break`. Esto significa que si el usuario
#    se equivoca y pone `-5`, el programa se cierra de inmediato en vez de darle
#    otra oportunidad. ¿Qué palabra clave cambiaría este comportamiento para que
#    solo salte a la siguiente iteración? (Pista: Ya la usaste en el `except`).
# 2. Preguntar si se desea salir al principio del bucle puede ser molesto la primera vez.
#    ¿Cómo estructurarías el bucle para que primero calcule y al final pregunte?
# ==============================================================================
