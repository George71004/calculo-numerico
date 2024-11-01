def newton_raphson(func, deriv_func, x0, tolerance=1e-6, max_iterations=100):
    # Lista para almacenar los resultados de cada iteración
    results = []
    
    x = x0
    for i in range(max_iterations):
        fx = func(x)
        f_prime_x = deriv_func(x)
        
        # Añadir a la tabla el valor de la iteración actual
        results.append({'i': i + 1, 'xi': x, 'F(xi)': fx})
        
        # Si la derivada es cero, no se puede continuar
        if f_prime_x == 0:
            print("La derivada es cero; no se puede continuar.")
            return None
        
        # Calcula el próximo valor de x usando Newton-Raphson
        x_next = x - fx / f_prime_x
        
        # Verifica la convergencia
        if abs(x_next - x) < tolerance:
            print(f"Convergencia alcanzada después de {i + 1} iteraciones.")
            results.append({'i': i + 1, 'xi': x_next, 'F(xi)': func(x_next)})
            break
        
        x = x_next

    # Mostrar la tabla de resultados
    print("i\t\txi\t\t\tF(xi)")
    print("-" * 40)
    for row in results:
        print(f"{row['i']}\t\t{row['xi']:.6f}\t\t{row['F(xi)']:.6f}")

    return x

# Definir la función y su derivada para f(x) = x^3 - 2x + 1
def func(x):
    return x**3 - 2 * x + 1

def deriv_func(x):
    return 3 * x**2 - 2

# Llamada a la función con punto de partida x0 = -1.5
root = newton_raphson(func, deriv_func, x0=-1.5)
print(f"\nLa raíz encontrada es aproximadamente: {root}")
