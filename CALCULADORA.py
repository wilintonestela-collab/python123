# ----------------------------------------------
# Autor: Wilinton Estela
# Programa: Calculadora interactiva con manejo de errores
# Descripción:
#   Este programa permite al usuario realizar operaciones matemáticas básicas:
#   suma, resta, multiplicación, división normal, división entera, potencia y resto de división.
#   Además, valida los datos ingresados por el usuario y controla errores como la división por cero.
# ----------------------------------------------

# Función que muestra el menú de operaciones disponibles
def mostrar_menu():
    print("\n=== CALCULADORA INTERACTIVA ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. División entera")
    print("6. Potencia")
    print("7. Resto de división")
    print("0. Salir")

# Función que pide un número al usuario y valida que sea un valor numérico
def pedir_numero(mensaje):
    while True:
        try:
            # El float permite ingresar números decimales
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("❌ Error: Debes ingresar un número válido. Intenta nuevamente.")

# Función principal de la calculadora
def calculadora():
    while True:
        mostrar_menu()
        
        # Pedimos la opción al usuario
        opcion = input("Elige una opción (0-7): ")

        # Si elige salir
        if opcion == "0":
            print("👋 Gracias por usar la calculadora. ¡Hasta pronto!")
            break

        # Validamos que la opción sea válida
        if opcion not in ["1","2","3","4","5","6","7"]:
            print("⚠️ Opción inválida. Por favor, elige una opción del menú.")
            continue

        # Pedimos los dos operandos
        num1 = pedir_numero("Ingresa el primer número: ")
        num2 = pedir_numero("Ingresa el segundo número: ")

        # Procesamos la operación seleccionada
        if opcion == "1":
            resultado = num1 + num2
            operacion = "Suma"
        elif opcion == "2":
            resultado = num1 - num2
            operacion = "Resta"
        elif opcion == "3":
            resultado = num1 * num2
            operacion = "Multiplicación"
        elif opcion == "4":
            # Manejo de error: división por cero
            while num2 == 0:
                print("❌ Error: No se puede dividir entre cero.")
                num2 = pedir_numero("Por favor, ingresa un nuevo divisor: ")
            resultado = num1 / num2
            operacion = "División"
        elif opcion == "5":
            # División entera (sin decimales)
            while num2 == 0:
                print("❌ Error: No se puede dividir entre cero.")
                num2 = pedir_numero("Por favor, ingresa un nuevo divisor: ")
            resultado = num1 // num2
            operacion = "División entera"
        elif opcion == "6":
            resultado = num1 ** num2
            operacion = "Potencia"
        elif opcion == "7":
            # Resto o módulo
            while num2 == 0:
                print("❌ Error: No se puede dividir entre cero.")
                num2 = pedir_numero("Por favor, ingresa un nuevo divisor: ")
            resultado = num1 % num2
            operacion = "Resto de división"

        # Mostramos el resultado al usuario
        print(f"\n✅ Resultado de la {operacion}: {resultado}")

        # Preguntamos si desea continuar
        continuar = input("\n¿Deseas realizar otra operación? (s/n): ").lower()
        if continuar != "s":
            print("👋 Programa finalizado. ¡Gracias por usar la calculadora!")
            break

# Ejecutamos el programa principal
if __name__ == "__main__":
    calculadora()
