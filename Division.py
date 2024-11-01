def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

def main():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        resultado = dividir(num1, num2)
        print(f"El resultado de la división es: {resultado}")
    except ValueError:
        print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    main()
