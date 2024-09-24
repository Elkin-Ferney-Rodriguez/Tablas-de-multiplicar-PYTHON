def tabla_multiplicar(numero):
    numero_mostrar = int(numero) if numero.is_integer() else numero
    print(f"\nTabla de multiplicar del {numero_mostrar}:")
    for i in range(1, 11):
        resultado = numero * i

        if resultado.is_integer():
            resultado = int(resultado)  
        print(f"{numero_mostrar} x {i} = {resultado}")

while True:
    print("Tablas de multiplicar")
    entrada = input("Ingrese un número para ver su tabla de multiplicar: ").strip()
    entrada = entrada.replace(',', '.')  
    try:
        numero = float(entrada)  
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        continue
    tabla_multiplicar(numero)

    continuar = input("¿Desea ver otra tabla? (si/no): ").strip().lower()
    if continuar != "si":
        print("Gracias por utilizar el programa. ¡Hasta luego!")
        break
