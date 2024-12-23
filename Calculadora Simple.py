# Función para sumar dos números
def add(x, y):
    return x + y

# Función para restar dos números
def subtract(x, y):
    return x - y

# Función para multiplicar dos números
def multiply(x, y):
    return x * y

# Función para dividir dos números
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."  # Manejo de división por cero
    return x / y

# Función principal de la calculadora
def calculator():
    while True:  # Bucle infinito para mostrar el menú después de cada operación
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")  # Opción para salir del programa

        # Solicita al usuario que elija una operación
        choice = input("Enter choice(1/2/3/4/5): ")

        # Verifica si la elección es válida
        if choice in ['1', '2', '3', '4']:
            # Solicita al usuario que ingrese dos números
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Realiza la operación correspondiente según la elección del usuario
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break  # Sale del bucle y termina el programa
        else:
            print("Invalid input")  # Mensaje de error si la elección no es válida

# Punto de entrada del programa
if __name__ == "__main__":
    calculator()