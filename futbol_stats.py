"""
=================================================
ACTIVIDAD 1: SIMULADOR BÁSICO DE ESTADÍSTICAS DE FÚTBOL
=================================================

TÓPICO: Fútbol 

DESCRIPCIÓN: Este programa simula el análisis de un partido de fútbol
pidiendo al usuario el resultado (goles y tiros a puerta) y calculando
el porcentaje de efectividad de los tiros y la diferencia de goles.
Además, determina si el resultado es una 'Victoria Grande' o un 'Clásico'.

VARIABLES UTILIZADAS:
- nombre_equipo (str): Nombre del equipo analizado. Pide datos al usuario.
- goles_favor (int): Goles marcados por el equipo. Pide datos al usuario.
- tiros_a_puerta (int): Tiros que fueron a portería. Pide datos al usuario.
- es_clasico (bool): Variable booleana que indica si el partido fue un clásico.
- efectividad_tiros (float): Almacena el porcentaje de goles sobre tiros a puerta.
- diferencia_goles (int): Almacena la diferencia entre goles_favor y 
MAX_GOLES_RIVAL.

CONSTANTES:
- MAX_GOLES_RIVAL (int): Máximo de goles que el equipo rival
 puede haber metido (3).
- PORCENTAJE_MINIMO_EFECTIVO (int): El porcentaje mínimo de efectividad para
 considerarse 'bueno' (20).

OPERADORES USADOS: Aritméticos, Comparación (>, <=), Lógicos (and).
CONVERSIÓN DE DATOS: Uso de int() para convertir la entrada del usuario
 (str) a números enteros.
"""

# --- CONSTANTES ---
# Nombres de constantes en MAYÚSCULAS por convención
MAX_GOLES_RIVAL = 3 
PORCENTAJE_MINIMO_EFECTIVO = 20 # 20%

# --- 1. PEDIR DATOS AL USUARIO Y VARIABLES (str, int) ---
print("--- ANÁLISIS RÁPIDO DE PARTIDO DE FÚTBOL ---")

# Variable tipo string (str)
nombre_equipo = input("Ingresa el nombre de tu equipo: ")

# Variables tipo entero (int). Se usa la función int() para CONVERSIÓN DE DATOS.
goles_favor_str = input(f"¿Cuántos goles anotó {nombre_equipo}? ")
tiros_a_puerta_str = input("¿Cuántos tiros a puerta realizó el equipo? ")

goles_favor = int(goles_favor_str)
tiros_a_puerta = int(tiros_a_puerta_str)

# Variable booleana (bool) - Pide datos
respuesta_clasico = input("¿Fue un partido clásico o derbi? (S/N): ").upper()
es_clasico = (respuesta_clasico == 'S')

# --- 2. OPERACIONES ENTRE VARIABLES ---

# Operación Aritmética 1: Cálculo de la diferencia de goles (Variable int)
diferencia_goles = goles_favor - MAX_GOLES_RIVAL 

# Operación Aritmética 2: Cálculo de Efectividad (Variable float)
# Se usa float() para asegurar que la división sea decimal
if tiros_a_puerta > 0:
    efectividad_tiros = (float(goles_favor) / tiros_a_puerta) * 100
else:
    efectividad_tiros = 0.0

# Operación Lógica y de Comparación (Variable bool)
# Se usa una expresión compleja que combina comparación y lógica 'and'
es_victoria_grande = (diferencia_goles > 0) and (efectividad_tiros > PORCENTAJE_MINIMO_EFECTIVO)
clasificado_directo = (goles_favor > 4) or es_clasico # Ejemplo de 'or'

# --- 3. ENSEÑAR DATOS AL USUARIO ---
print("\n========== RESULTADOS DEL ANÁLISIS ==========")
print(f"Equipo analizado: {nombre_equipo}")
print(f"Goles anotados: {goles_favor}")
print(f"Tiros a puerta: {tiros_a_puerta}")
print(f"Máximo de goles del rival (Constante): {MAX_GOLES_RIVAL}")

print("\n--- Estadísticas ---")
print(f"Efectividad de tiros a puerta: {efectividad_tiros:.2f}%")
print(f"Diferencia de goles calculada: {diferencia_goles}")
print(f"¿Clásico? {es_clasico}")

# Uso de la operación lógica/comparación para dar un mensaje
if es_victoria_grande:
    print("¡VICTORIA GRANDE!  Tuve una buena efectividad en ataque.")
elif clasificado_directo:
    print("¡Gran resultado! (Cumple criterio de clasificación o es un Clásico).")
else:
    print("Resultado estándar. Intentare aumentar la efectividad en el próximo partido.")

print("============================================")