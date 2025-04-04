def gcd(a, b):
    """
    Calcula el Máximo Común Divisor (MCD) de dos números enteros positivos utilizando el algoritmo de Euclides.

    Args:
    a (int): El primer número entero positivo.
    b (int): El segundo número entero positivo.

    Returns:
    int: El MCD de a y b.
    """
    while b != 0:
        a, b = b, a % b
    return a


# Función para validar si el número ingresado es positivo
def validar_numero(num):
    try:
        num = int(num)
        if num <= 0:
            print("Por favor, ingrese un número entero positivo.")
            return False, None
        return True, num
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
        return False, None


def solicitar_numero(mensaje):
    """
    Solicita entrada de usuario para un número entero positivo.

    Args:
    mensaje (str): El mensaje que se muestra al solicitar la entrada.

    Returns:
    int: El número entero positivo ingresado por el usuario.
    """
    while True:
        num = input(mensaje)
        valido, num = validar_numero(num)
        if valido:
            return num

# Solicitar entrada de usuario para el primer número
num1 = solicitar_numero("Ingrese el primer número entero positivo: ")

# Solicitar entrada de usuario para el segundo número
num2 = solicitar_numero("Ingrese el segundo número entero positivo: ")


# Calcular y mostrar el MCD
print("El Máximo Común Divisor de", num1, "y", num2, "es:", gcd(num1, num2))
