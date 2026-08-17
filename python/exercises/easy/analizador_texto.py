# ==============================================================================
# ANALIZADOR DE TEXTO Y CONTADOR DE VOCALES
# Tiempo estimado: 30 minutos
# Temas clave: Strings, Loops (for/while), Condicionales, Listas, Métodos de Strings
# ==============================================================================
#
# DESCRIPCIÓN DEL PROBLEMA:
# Crea un programa que analice un texto ingresado por el usuario. El programa 
# debe contar cuántas vocales (a, e, i, o, u) tiene el texto, cuántas palabras 
# en total contiene, y generar una versión del texto donde todas las vocales 
# estén en mayúsculas y las consonantes en minúsculas.
#
# REQUISITOS DEL RESULTADO ESPERADO (DETALLADO):
# 1. Solicitar por consola al usuario que ingrese una frase o texto libre.
# 2. Contar la cantidad de apariciones de cada una de las vocales (independientemente 
#    de si están en mayúsculas o minúsculas en el texto original, ej: 'A' o 'a' cuentan igual).
# 3. Calcular la cantidad de palabras del texto (pista: las palabras suelen estar 
#    separadas por espacios).
# 4. Construir y mostrar una nueva cadena de texto a partir de la original donde:
#    - Toda vocal aparezca en MAYÚSCULA.
#    - Toda consonante aparezca en minúscula.
#    - Los espacios y signos de puntuación se mantengan igual.
# 5. Mostrar en pantalla:
#    - El total de palabras encontradas.
#    - Un desglose de cuántas veces aparece cada vocal (a, e, i, o, u).
#    - El texto modificado.
#
# EJEMPLO DE EJECUCIÓN ESPERADO:
# Introduce un texto: Aprendiendo Python en la tarde
#
# --- RESULTADO ---
# Total de palabras: 5
# Desglose de vocales:
#   A: 2
#   E: 4
#   I: 1
#   O: 1
#   U: 0
# Texto transformado: AprEndIEndO pythOn En lA tArdE
# ==============================================================================

# Escribe tu solución a partir de aquí:

texto = input("Introduce un texto: ")

#1. contar aparicion de cada vocal 
vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0} #asociar cantidad con vocal, en apres, la mejor estructura es un diccionario

for i in texto:
    if i.lower() in vocales: #se convierte el caracter a minuscula y se verifica si esta en el diccionario
        vocales[i.lower()] += 1 # si esta, se incrementa en 1, entre los corchetes se usa la letra en minuscula para acessar al valor de la llave

#2. calcular cantidad de palabras
cantidad_palabras = texto.split() #divide el texto en palabras. metodo split() divide la cadena de texto en una lista de palabras
cantidad_palabras = len(cantidad_palabras) #cuenta la cantidad de palabras

#3. contruir texto
texto = texto.lower() #convierte el texto a minusculas

# Optimización: Se itera sobre las 5 vocales en el diccionario (complejidad constante de 5 vueltas)
# en lugar de recorrer cada caracter del texto (que dependía del largo de la frase).
for vocal in vocales:
    if vocal in texto:
        texto = texto.replace(vocal, vocal.upper()) #reemplaza la vocal por su mayuscula. replace(cadena_original, cadena_reemplazada), upper(caracter): convierte a mayuscula

print(f"Desglose de vocales: {vocales}")
print(f"Total de palabras: {cantidad_palabras}")
print(f"Texto transformado: {texto}")