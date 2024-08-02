def determinar_tipo_triangulo(lado1, lado2, lado3):
    if not (isinstance(lado1, (int, float)) and isinstance(lado2, (int, float)) and isinstance(lado3, (int, float))):
        return "Los valores deben ser numeros."

    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        return "Los lados deben ser numeros positivos y mayores que cero."

    if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
        return "No es un triangulo válido."

    if lado1 == lado2 == lado3:
        return "Triangulo equilátero."
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Triangulo isósceles."
    else:
        return "Triangulo escaleno."

try:
    lado1 = float(input("Ingrese el lado 1 del triangulo: "))
    lado2 = float(input("Ingrese el lado 2 del triangulo: "))
    lado3 = float(input("Ingrese el lado 3 del triangulo: "))

    resultado = determinar_tipo_triangulo(lado1, lado2, lado3)
    print("El triangulo es:", resultado)

except ValueError:
    print("Entrada invalida")
