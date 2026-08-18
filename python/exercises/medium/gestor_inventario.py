# ==============================================================================
# GESTOR DE INVENTARIO SIMPLIFICADO
# Tiempo estimado: 30 minutos
# Temas clave: Listas, Tuplas, Loops, Métodos de Listas (append, remove, index), Control de Flujo
# ==============================================================================
#
# DESCRIPCIÓN DEL PROBLEMA:
# Desarrolla un programa interactivo de consola para gestionar un inventario de 
# productos de una tienda pequeña. Cada producto en el inventario estará representado 
# por una tupla con la estructura: (nombre_del_producto, precio, cantidad_en_stock).
# El inventario completo será una lista de estas tuplas.
#
# El programa debe mostrar un menú recurrente (usando un bucle while) con las siguientes opciones:
# 1. Agregar un nuevo producto.
# 2. Ver inventario completo (mostrando cada producto con su índice, precio y cantidad).
# 3. Buscar un producto por nombre (y mostrar su información).
# 4. Eliminar un producto del inventario por nombre.
# 5. Salir del programa.
#
# REQUISITOS DEL RESULTADO ESPERADO (DETALLADO):
# 1. El programa no debe terminar a menos que el usuario seleccione la opción 5 (Salir).
# 2. Al agregar un producto:
#    - Solicitar nombre, precio y cantidad.
#    - Crear la tupla (nombre, precio, cantidad) e insertarla en la lista de inventario.
#    - Evitar duplicados: si el producto ya existe (con el mismo nombre), avisar al usuario 
#      y no agregarlo.
# 3. Al mostrar el inventario:
#    - Si está vacío, indicarlo con un mensaje.
#    - Si contiene productos, mostrarlos numerados en formato legible (ej: "1. Camiseta - $15.50 - Stock: 10").
# 4. Al buscar un producto:
#    - Solicitar el nombre a buscar (ignorando mayúsculas/minúsculas).
#    - Si existe, mostrar sus detalles de precio y stock. Si no, avisar que no se encontró.
# 5. Al eliminar un producto:
#    - Solicitar el nombre del producto a eliminar.
#    - Si existe en la lista, eliminarlo y confirmar la acción. Si no, informar de su ausencia.
#
# ==============================================================================

# Escribe tu solución a partir de aquí:

def agregar_producto(inventario):
    nombre = str(input("nombre producto: "))
    precio = float(input("ingrese precio: "))
    cantidad = int(input("ingrese cantidad: "))
    
    # 1. Bandera (flag): Asumimos inicialmente que el producto NO existe
    existe = False 
    
    # 2. Recorremos todo el inventario para verificar
    for producto in inventario:
        # Comparamos el nombre existente (producto[0]) con el nuevo en minúsculas
        if producto[0] == nombre.lower():
            existe = True # Si lo encuentra, activa la bandera
            break         # Detiene el bucle (ya no necesita seguir buscando)
            
    # 3. Decisión final (la "vista general"):
    if existe == False:
        inventario.append((nombre.lower(), precio, cantidad)) # Se agrega como tupla, es decir las variables en un parentesis a la lista
        print("producto agregado exitosamente")
    else:
        print("producto ya existe")

def ver_inventario(inventario):
    print("inventario completo")
    for producto in inventario:
        print(producto)

def buscar_producto(inventario):
    nombre = input("nombre del producto: ")

    find = False
    position = 0

    for pos, producto in enumerate(inventario):
        # Comparamos el nombre existente (producto[0]) con el nuevo en minúsculas
        if producto[0] == nombre.lower():
            find = True # Si lo encuentra, activa la bandera
            position = pos
            break    

    if find == False:
        print("producto no existente")
    else:
        print(inventario[position])

def eliminar_producto(inventario):
    print("----ELIMINAR PRODUCTO-----") 
    nombre = input("nombre del producto: ")

    find = False
    position = 0

    for pos, producto in enumerate(inventario):
        # Comparamos el nombre existente (producto[0]) con el nuevo en minúsculas
        if producto[0] == nombre.lower():
            find = True # Si lo encuentra, activa la bandera
            position = pos
            break    

    if find == False:
        print("producto no existente")
    else:
        print(f"producto encontrado: {inventario[position]}")
        opcion = input("desea eliminarlo Y/N")

        if opcion.upper() == "Y":
            inventario.pop(position)
            print("producto eliminado")


opcion = 0
inventario = []

while opcion != 5:
    print("---------------menu---------------")
    print("1. Agregar producto")
    print("2. Ver inventario completo")
    print("3. Buscar un producto por nombre")
    print("4. Eliminar un producto del inventario por nombre")
    print("5. Salir del programa")

    opcion = int(input("ingrese opcion: "))

    if opcion == 1:
        agregar_producto(inventario)
    elif opcion == 2:
        ver_inventario(inventario)
    elif opcion == 3:
        buscar_producto(inventario)
    elif opcion == 4:
        eliminar_producto(inventario)



