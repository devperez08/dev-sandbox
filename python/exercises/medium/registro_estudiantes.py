# ==============================================================================
# REGISTRO DE ESTUDIANTES Y CURSOS
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

#1. diccionario vacio
registro = {}

#2. Registrar un estudiante
def registrar_estudiante(registro, nombre_estudiante): #Parametros que vamos a recibir
    if nombre_estudiante in registro: #verificar si el estudiante ya existe dentro del registro
        print(f"El estudiante {nombre_estudiante} ya está registrado")

    #2.1 agregar estudiante al registro con un conjunto vacio si no existe
    else: #Si no existe
        registro[nombre_estudiante] = set() #Agregamos el estudiante al registro con un conjunto vacio
        print(f"Estudiante {nombre_estudiante} registrado correctamente")

#3. Inscribir un curso en el registro
def inscribir_curso(registro, nombre_estudiante, nombre_curso): #se entregan aprametros: el registro, el nombre del estudiante y el nombre del curso a inscribir
    #3.1 Si el estudiante no existe en el registro, registrarlo automáticamente primero.
    if nombre_estudiante not in registro: #verificar si el estudiante ya existe dentro del registro
        registrar_estudiante(registro, nombre_estudiante)
    registro[nombre_estudiante].add(nombre_curso) #Agregamos el curso al conjunto del estudiante al nombre correspondiente
    print(f"El estudiante {nombre_estudiante} se ha inscrito al curso {nombre_curso}")


#4. obtener los cursos de un estudiante
def obtener_curso(registro, nombre_estudiante):
    if nombre_estudiante in registro:
        return registro[nombre_estudiante]
    else:
        return None

#4.1 Obtener cursos en comun de dos estudiantes
def cursos_en_comun(registro, estudiante1, estudiante2):
    # Verificar si ambos estudiantes existen
    if estudiante1 not in registro or estudiante2 not in registro:
        return set() # Retorna conjunto vacío si alguno no existe
    
    # Obtener los cursos de cada estudiante
    cursos1 = registro[estudiante1]
    cursos2 = registro[estudiante2]
    
    # Intersección de conjuntos o cursos que estan en ambos conjuntos
    return cursos1 & cursos2


#5. Probar las funciones
# 1. Registrar estudiantes
registrar_estudiante(registro, "Juan")
registrar_estudiante(registro, "Maria")
registrar_estudiante(registro, "Carlos")

# 2. Inscribir cursos
inscribir_curso(registro, "Juan", "Matemáticas")
inscribir_curso(registro, "Juan", "Física")
inscribir_curso(registro, "Maria", "Matemáticas")
inscribir_curso(registro, "Maria", "Química")
inscribir_curso(registro, "Carlos", "Física")
inscribir_curso(registro, "Carlos", "Química")

# 3. Obtener cursos de un estudiante
print(f"\nCursos de Juan: {obtener_curso(registro, 'Juan')}")
print(f"Cursos de Maria: {obtener_curso(registro, 'Maria')}")

# 4. Cursos en común
print(f"\nCursos en común de Juan y Maria: {cursos_en_comun(registro, 'Juan', 'Maria')}")
print(f"\nCursos en común de Juan y Carlos: {cursos_en_comun(registro, 'Juan', 'Carlos')}")


def obtener_catalogo_cursos(registro):
    catalogo = set()
    for curso in registro.values(): #se utiliza el metodo .values() que me devuelve todos los valores del diccionario
        catalogo.update(curso)
    return catalogo

print(f"catalogo de cursos: {obtener_catalogo_cursos(registro)}")