import random   # Importa la librería random, que permite generar números aleatorios

n_intentos = 3  # Cantidad de intentos permitidos
adivina = False # Variable que podría usarse para comprobar si se adivinó (no se usa, pero no da error)

# Lista de números posibles y selección aleatoria
n_aleatorio = random.choice([1, 3, 6, 9, 12, 15, 18, 21])
print(n_aleatorio)  # Solo para pruebas. En la versión final debería eliminarse

# Bucle FOR que controla el número de intentos
for intento in range(n_intentos):
    print(f"\nEstás en el intento {intento + 1}")  # Se suma +1 para que no salga desde 0
    
    # Entrada del usuario
    n_usuario = int(input("Digita un número entre 1 y 21: "))
    
    # Condición para comprobar si acertó
    if n_usuario == n_aleatorio:
        print("¡Enhorabuena! Adivinaste ")
        adivina = True
        break
    else:
        print("Game over, inténtalo otra vez.")

# Mensaje si no acertó en ningún intento
if not adivina:
    print("\nNo lograste adivinar el número.")
    print(f"El número correcto era: {n_aleatorio}")
