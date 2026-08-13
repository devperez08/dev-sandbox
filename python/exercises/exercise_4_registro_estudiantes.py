# ==============================================================================
# EJERCICIO 4: REGISTRO DE ESTUDIANTES Y CURSOS
# Tiempo estimado: 30 minutos
# Temas clave: Diccionarios, Sets (Conjuntos), Funciones (definición, parámetros, retorno)
# ==============================================================================
#
# DESCRIPCIÓN DEL PROBLEMA:
# Implementa un sistema básico para registrar estudiantes y las materias/cursos a las 
# que están inscritos. Utiliza un diccionario donde la clave es el nombre del estudiante 
# y el valor es un conjunto (set) con los nombres de los cursos que cursa (para evitar 
# que se inscriba dos veces al mismo curso por error).
#
# Debes estructurar tu código usando al menos las siguientes funciones:
# 1. registrar_estudiante(registro, nombre_estudiante): Agrega un estudiante con un conjunto de cursos vacío.
# 2. inscribir_curso(registro, nombre_estudiante, nombre_curso): Agrega el curso al conjunto del estudiante.
# 3. obtener_cursos(registro, nombre_estudiante): Retorna la lista o conjunto de cursos del estudiante.
# 4. estudiantes_en_comun(registro, estudiante1, estudiante2): Retorna un conjunto con los cursos que comparten ambos estudiantes (intersección).
#
# REQUISITOS DEL RESULTADO ESPERADO (DETALLADO):
# 1. El diccionario principal de registro debe comenzar vacío.
# 2. Al registrar un estudiante:
#    - Si ya existe en el diccionario, mostrar un aviso de que ya está registrado.
#    - Si no existe, agregarlo con un conjunto vacío `set()`.
# 3. Al inscribir en un curso:
#    - Si el estudiante no existe en el registro, registrarlo automáticamente primero.
#    - Agregar el curso a su conjunto.
# 4. Al buscar cursos en común:
#    - Usar la operación de intersección de sets (`&` o el método `.intersection()`) para
#      determinar qué cursos tienen en común dos estudiantes específicos y mostrar el resultado.
#
# Escribe un pequeño flujo al final del archivo para probar tus funciones, registrando 
# al menos a dos estudiantes (ej: "Juan" y "Maria"), inscribiéndolos en materias
# (algunas compartidas y otras no) y mostrando la intersección de materias en común.
# ==============================================================================

# Escribe tu solución a partir de aquí:

