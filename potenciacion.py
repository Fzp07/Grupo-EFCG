# Calculadora simple para potenciar un número

def potencia(base, exponente):
    return base ** exponente

def main():
    try:
        # Solicitar al usuario la base
        base = float(input("Introduce la base: "))
        # Solicitar al usuario el exponente
        exponente = float(input("Introduce el exponente: "))

        # Calcular la potencia
        resultado = potencia(base, exponente)

        # Mostrar el resultado
        print(f"{base} elevado a la {exponente} es: {resultado}")
    except ValueError:
        print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    main()
