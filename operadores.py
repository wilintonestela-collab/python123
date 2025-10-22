# EJERCICIO COMPLETO: DOMINANDO LOS OPERADORES EN PYTHON
# Completa los espacios, responde las preguntas y corrige los errores

# ========== PARTE 1: OPERADORES ARITMÉTICOS ==========
print("=== PARTE 1: Operadores Aritméticos ===")

# Completa las operaciones que faltan
num1 = 20
num2 = 6

resultado_suma = num1 + num2          # Debe dar 26
resultado_resta = num1 - num2         # Debe dar 14
resultado_mult = num1 * num2          # Debe dar 120
resultado_div = num1 / num2           # Debe dar 3.33...
resultado_div_entera = num1 // num2    # Debe dar 3
resultado_modulo = num1 % num2        # Debe dar 2
resultado_potencia = num1 ** num2      # Debe dar 64,000,000?

# Corrige el error en esta expresión
# resultado = 10 + 5 * 2  # Resultado esperado: 20, actual: ¿?
resultado_corregido = 10 + 5 * 2
# ¿Cómo lo corregirías para que dé 30? ________________

# ========== PARTE 2: OPERADORES DE COMPARACIÓN ==========
print("\n=== PARTE 2: Operadores de Comparación ===")

a = 15
b = 10
c = 15

# Escribe el resultado esperado (True/False)
comp1 = a > b          # Esperado: true
comp2 = a == c         # Esperado: true
comp3 = b != a         # Esperado: true
comp4 = a <= c         # Esperado: true
comp5 = 20 >= a        # Esperado: true

# Explica qué hace esta expresión combinada
edad = 25
altura = 175
expresion_compleja = (edad >= 18) and (altura > 160)
# Explicación: true por que la variable edad es mayor igual que 18 y la variable altura es mayor que 160 

# ========== PARTE 3: OPERADORES LÓGICOS ==========
print("\n=== PARTE 3: Operadores Lógicos ===")

# Completa con and, or, not
es_fin_de_semana = True
tengo_dinero = False
hace_buen_tiempo = True

puedo_salir = es_fin_de_semana and (tengo_dinero and hace_buen_tiempo)
# ¿Cuándo puedo salir? cuando sea fin de semana y tenga dinero y haga buen tiempo

es_adulto = True
es_estudiante = False
tiene_descuento = not es_estudiante and (edad > 65)
# ¿Quién tiene descuento? tendrian descuento quien no es estudiente y tenga edad mayor a 65

# ========== PARTE 4: OPERADORES DE ASIGNACIÓN ==========
print("\n=== PARTE 4: Operadores de Asignación ===")

# Cadena de operaciones complejas
x = 10
y = 5
z = 2

x = x+ y*z            # x = 10 + 5 * 2 = 20
# ¿Cuál es el valor final de x? el valor de x es 20

# ========== PARTE 5: EXPRESIONES COMPLEJAS ==========
print("\n=== PARTE 5: Expresiones Complejas ===")

# Analiza y resuelve estas expresiones complejas
precio = 100
descuento = 20
iva = 21
es_cliente_frecuente = True
tiene_cupon = False

# Expresión 1: Calcula el precio final con descuento e IVA
precio_final = (precio - descuento) * (1 + iva/100)
# Explica paso a paso: se resta el descuento que es 20 al precio que es 100,
# lo multiplico por 1 mas el iva que es 21 dividido entre 100  y el resultado es el precio final


# Expresión 2: Condición compleja para descuento extra
descuento_extra = es_cliente_frecuente and (tiene_cupon and (precio > 50))
# ¿Cuándo hay descuento extra? si el cliente es frecuente y tiene un cupon y si 
# el precio es mayor a 50 tendra descuento

# Expresión 3: Múltiples condiciones
puede_comprar = (precio_final <= 150) and (tiene_cupon or es_cliente_frecuente)
# ¿Quién puede comprar? puede comprar si el precio es menor o igual a 150 y tiene cupon o es cliente

# ========== PARTE 6: CORRECCIÓN DE ERRORES ==========
print("\n=== PARTE 6: Corrección de Errores ===")

# Corrige los errores en estas expresiones:
# 1. resultado = 10 + * 5           # Error: tiene dos signos de operacion
#    Corrección: 10 + 5 o 10 * 5
10 + 5
# 2. if edad = 18:                  # Error: falta el simbolo ==  
#    Corrección: if edad == 18
if edad == 18:
    a = 0
# 3. valor = "10" + 5               # Error: "10" es tipo texto
#    Corrección: valor = 10 + 5
valor = 10 + 5 
# 4. if a > b and or c:             # Error: and or c
#    Corrección: expresion: b and c o b or c
if a > b and c:
    c = 0
print("\n¡Ejercicio completado! Revisa todas tus respuestas.")

