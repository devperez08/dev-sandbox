# ==============================================================================
# SIMULADOR DE CUENTA BANCARIA (INTRODUCCIÓN A CLASES)
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

#clase define el comportamiento 
class BankAccount:
    #constructor de clase, siempre usar self: representa el objeto especifico que esta manipuilando en el momento
    #lugar donde establecer valores asociados a una cuenta bancaria (BankAccount), la clase
    def __init__(self, titular, num_cuenta, saldo = 0.0): #para un valor por defecto u opcional se pone el = y luego el valor
        self.titular = titular
        self.num_cuenta = num_cuenta
        self.saldo = saldo

    def deposit(self, amount):
        if amount <= 0:
            print("ingrese un valor valido")
        else:
            self.saldo += amount
            print(f"deposito exitoso por {amount}")
    
    def withdraw(self, amount):
        valor = amount
        if valor > self.saldo or valor <= 0:
            print("no tiene saldo suficiente o valor incorrecto")
            return False #para validar que no haya fondos suficientes y no se completo la transaccion
        else:
            print(f"retiraste {valor} de tu cuenta")
            self.saldo -= valor
            return True #para validar que se completó la transaccion y se completó correctamente

    def get_balance(self):
        return self.saldo

    def display_info(self):
        print(f"Titular: {self.titular}\nNúmero de cuenta: {self.num_cuenta}\nSaldo disponible: {self.saldo}")

    
    # REUTILIZACIÓN DE MÉTODOS Y PASO POR REFERENCIA:
    # 'target_acount' es una variable que recibe un OBJETO completo de tipo BankAccount.
    # Python no busca un número de cuenta en una base de datos aquí; en su lugar, recibe la
    # referencia directa en memoria del objeto (como pasar a la persona real cara a cara).
    def transfer(self, target_acount, amount):
        # 1. 'self' aquí representa a la cuenta que envia (la que está antes del punto en la llamada).
        # Ejecutamos el retiro en nuestra propia cuenta y guardamos si fue exitoso (True o False).
        estado = self.withdraw(amount) 
        
        # 2. Si el retiro fue exitoso, depositamos en la cuenta destino.
        if estado is True:
            # Al hacer 'target_acount.deposit', le decimos al objeto destino que ejecute su método 'deposit'.
            # Dentro de esa ejecución de 'deposit', el parámetro 'self' de ese método pasará a ser 'target_acount'.
            target_acount.deposit(amount)

# --- CÓDIGO DE PRUEBA ---
# 1. Creamos una cuenta para 'Yarley' con saldo inicial de 20000
cuenta = BankAccount("Yarley", 123, 20000)

# 2. Mostramos la información inicial
print("--- Información Inicial ---")
cuenta.display_info()

# 3. Hacemos un depósito exitoso
print("\n--- Realizando Depósito ---")
cuenta.deposit(5000)

# 4. Hacemos un retiro exitoso (dentro de los fondos)
print("\n--- Realizando Retiro Exitoso ---")
cuenta.withdraw(10000)

# 5. Hacemos un retiro fallido (supera el saldo disponible)
print("\n--- Intentando Retiro Mayor al Saldo ---")
cuenta.withdraw(30000)

# 6. Mostramos la información final de la cuenta
print("\n--- Información Final ---")
cuenta.display_info()

# 7. Probando la Transferencia
print("\n--- Probando Transferencia ---")
cuenta_destino = BankAccount("Maria", 456, 1000)
print("Estado inicial de la cuenta de María:")
cuenta_destino.display_info()

print("\nTransfiriendo 5000 a la cuenta de María...")
cuenta.transfer(cuenta_destino, 5000)

print("\nEstado final después de la transferencia:")
cuenta.display_info()
cuenta_destino.display_info()

# 8. Transferencia a Carlos (propuesta por el usuario)
print("\n--- Transferencia a Carlos ---")
carlos = BankAccount("Carlos", 789, 10000)
print("Estado inicial de la cuenta de Carlos:")
carlos.display_info()

print("\nTransfiriendo 1000 a la cuenta de Carlos...")
cuenta.transfer(carlos, 1000)

print("\nEstado final después de transferir a Carlos:")
cuenta.display_info()
carlos.display_info()




# --- EXTRA: SIMULACIÓN DE CAJERO AUTOMÁTICO INTERACTIVO ---
# Esta función es el "aparato externo" (el cajero) que utiliza la tarjeta (la clase)
def cajero_automatico():
    print("\n=== BIENVENIDO AL CAJERO AUTOMÁTICO ===")
    nombre = input("Ingrese su nombre para registrarse: ")
    num_cta = input("Ingrese su número de cuenta: ")
    
    # Instanciamos la clase con los datos ingresados
    mi_cuenta = BankAccount(nombre, num_cta)
    
    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Mostrar información completa")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            # Usamos get_balance para obtener el valor y poder imprimirlo aquí
            saldo_actual = mi_cuenta.get_balance()
            print(f"Su saldo actual es: ${saldo_actual}")
        elif opcion == "2":
            try:
                monto = float(input("Ingrese monto a depositar: "))
                mi_cuenta.deposit(monto)
            except ValueError:
                print("Error: Ingrese un número válido.")
        elif opcion == "3":
            try:
                monto = float(input("Ingrese monto a retirar: "))
                mi_cuenta.withdraw(monto)
            except ValueError:
                print("Error: Ingrese un número válido.")
        elif opcion == "4":
            mi_cuenta.display_info()
        elif opcion == "5":
            print("Gracias por usar el Cajero Automático. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente nuevamente.")

# Si quieres jugar con el cajero interactivo en tu terminal,
# solo descomenta la siguiente línea y ejecuta el archivo:
# cajero_automatico()


