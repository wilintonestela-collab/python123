

import random  # Importamos la librería random para generar números aleatorios

# Generamos un número secreto entre 1 y 20 usando randint()
numero_secreto = random.randint(1, 20)

# Número máximo de intentos que tendrá el usuario
intentos = 3

# Esta variable llevará la cuenta de cuántos intentos lleva el usuario
contador = 1

# Variable booleana (True/False) que indica si el usuario adivinó o no
acerto = False

print("Bienvenido al juego")
print("Debes adivinar un número entre 1 y 20.")
print("Tienes 3 intentos para lograrlo.\n")

# BUCLE WHILE:
# Se repetirá mientras el usuario tenga intentos
# y mientras aún NO haya adivinado el número

while contador <= intentos and acerto == False:

    # Informamos al usuario en qué intento está
    print(f"Intento {contador} de {intentos}")

    # Pedimos al usuario que escriba un número
    numero_usuario = int(input("Ingresa tu número: "))

    # Comprobamos si el número del usuario es igual al número secreto
    if numero_usuario == numero_secreto:
        print("\n¡Correcto! Adivinaste el número")
        acerto = True  # Marcamos que sí adivinó para salir del bucle
    else:
        # El usuario falló el intento
        print("Incorrecto. Intenta otra vez.\n")

    # Sumamos +1 al contador para pasar al siguiente intento
    contador = contador + 1
# FIN DEL JUEGO:
# Se ejecuta cuando se sale del while
# (ya sea porque adivinó o porque se acabaron los intentos)

if acerto == False:
    # Si el usuario NO acertó:
    print("Se terminaron los intentos")
    print(f"El número correcto era: {numero_secreto}")
else:
    # Si acertó:
    print("¡Bien hecho! Gracias por jugar.")