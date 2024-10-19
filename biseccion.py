import math

def biseccion(f, a, b, tol):
    # Comprobamos que los extremos del intervalo tienen signos opuestos
    if f(a) * f(b) >= 0:
        print("El método de bisección no es aplicable.")
        return None
    
    # Inicialización de variables
    iteraciones = 0
    error = abs(b - a) / 2

    print(f"{'Iteración':>10} {'a':>10} {'b':>10} {'c (punto medio)':>20} {'f(c)':>15} {'Error':>10}")
    print("-" * 70)
    
    # Ejecutamos el ciclo mientras el error sea mayor que la tolerancia
    while error > tol:
        iteraciones += 1
        # Punto medio del intervalo
        c = (a + b) / 2
        f_c = f(c)
        
        # Imprimimos los detalles de la iteración actual
        print(f"{iteraciones:>10} {a:>10.6f} {b:>10.6f} {c:>20.6f} {f_c:>15.6f} {error:>10.6f}")
        
        # Verificamos si c es una raíz o el error es menor que la tolerancia
        if f_c == 0 or error < tol:
            break
        
        # Decidimos en qué subintervalo continuar
        if f(a) * f_c < 0:
            b = c
        else:
            a = c
        
        # Recalculamos el error
        error = abs(b - a) / 2
    
    # Devolvemos el valor aproximado de la raíz y el número de iteraciones
    return c, iteraciones


# Ejemplo de uso: F(x) = (x - 2)^2 - ln(x)
def funcion(x):
    return math.sin(x) - math.exp(-x)

# Parámetros iniciales
a = 0  # Límite inferior del intervalo
b = 1  # Límite superior del intervalo
tolerancia = 0.03  # Tolerancia del error

# Llamamos a la función bisección
raiz, total_iteraciones = biseccion(funcion, a, b, tolerancia)

# Imprimimos el resultado final
if raiz is not None:
    print("\nResultado final:")
    print(f"Raíz encontrada: {raiz}")
    print(f"Número total de iteraciones: {total_iteraciones}")
else:
    print("No se pudo encontrar una raíz en el intervalo dado.")
