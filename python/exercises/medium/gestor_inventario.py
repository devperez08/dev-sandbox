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

