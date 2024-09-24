# Formulas Python
def operacion(opcion, a, b):
    match opcion:
        case "1":
            return a + b
        case "2":
            return a - b
        case "3":
            return a * b
        case "4":
            if b != 0:
                return a / b
            else:
                return "Dividir por cero es indefinido."
        case _:
            return "Escoja una de las opciones."

while True:
    print("Bienvenido")
    print("Escoja la operación que necesita:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Digite su opción: ")

    if opcion == "5":
        print("Gracias por utilizar el programa. ¡Hasta luego!")
        break

    if opcion in ["1", "2", "3", "4"]:
        a = float(input("Digite el primer número: "))
        b = float(input("Digite el segundo número: "))

        resultado = operacion(opcion, a, b)
        
        if isinstance(resultado, float) and resultado.is_integer():
            resultado = int(resultado)  

        print(f"El resultado de : {resultado}")
        
        # Preguntar si desea realizar otra operación
        continuar = input("¿Desea realizar otra operación? (si/no): ").strip().lower()
        if continuar != "si":
            print("Gracias por utilizar el programa. ¡Hasta luego!")
            break  # Salir del bucle principal
    else:
        print("Escoja una de las opciones válidas.")
