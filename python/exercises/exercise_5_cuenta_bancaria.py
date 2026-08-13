# ==============================================================================
# EJERCICIO 5: SIMULADOR DE CUENTA BANCARIA (INTRODUCCIÓN A CLASES)
# Tiempo estimado: 30 minutos
# Temas clave: Clases, Objetos, Constructor (__init__), Métodos de instancia, Atributos
# ==============================================================================
#
# DESCRIPCIÓN DEL PROBLEMA:
# Crea una clase llamada `BankAccount` (Cuenta Bancaria) que permita modelar el 
# comportamiento de una cuenta financiera básica. Cada cuenta debe tener un 
# titular de la cuenta, un número de cuenta y un saldo inicial.
#
# La clase debe contar con los siguientes métodos:
# 1. Constructor `__init__`: inicializa los atributos `titular`, `numero_cuenta` y `saldo`.
# 2. `deposit(amount)`: añade una cantidad positiva al saldo y muestra el nuevo saldo.
# 3. `withdraw(amount)`: retira una cantidad positiva del saldo siempre y cuando haya 
#    fondos suficientes. Si no los hay, muestra un mensaje de error y no realiza el retiro.
# 4. `get_balance()`: retorna el saldo actual.
# 5. `display_info()`: imprime un resumen ordenado de la cuenta (titular, número de cuenta y saldo).
#
# REQUISITOS DEL RESULTADO ESPERADO (DETALLADO):
# 1. Al instanciar una cuenta, el saldo inicial por defecto debe ser 0.0 si el usuario no especifica otro valor.
# 2. Validar las transacciones:
#    - No se pueden depositar cantidades negativas o iguales a cero.
#    - No se pueden retirar cantidades negativas o iguales a cero.
#    - No se puede retirar más dinero del saldo disponible.
# 3. Cada método que realice un cambio (depósito/retiro exitoso) debe imprimir una confirmación legible.
# 4. Al final del archivo, escribe código de prueba para instanciar al menos una cuenta, 
#    hacer un depósito, un retiro exitoso, un retiro fallido por falta de fondos y mostrar 
#    la información final de la cuenta.
# ==============================================================================

# Escribe tu solución a partir de aquí:

