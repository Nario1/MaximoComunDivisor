class CalculadoraMCD:
    def __init__(self, num1, num2):
        self.numero1 = num1
        self.numero2 = num2

    # Getter y Setter con @property para numero1
    @property
    def numero1(self):
        return self._numero1

    @numero1.setter
    def numero1(self, value):
        if self._validar_numero(value):
            self._numero1 = int(value)
        else:
            raise ValueError("numero1 debe ser un número entero positivo.")

    # Getter y Setter con @property para numero2
    @property
    def numero2(self):
        return self._numero2

    @numero2.setter
    def numero2(self, value):
        if self._validar_numero(value):
            self._numero2 = int(value)
        else:
            raise ValueError("numero2 debe ser un número entero positivo.")

    # Método estático para validar que el número sea entero positivo
    @staticmethod
    def _validar_numero(num):
        try:
            num = int(num)
            return num > 0
        except ValueError:
            return False

    # Método para calcular el MCD usando el algoritmo de Euclides
    def calcular_mcd(self):
        a = self.numero1
        b = self.numero2
        while b != 0:
            a, b = b, a % b
        return a


# Función auxiliar para pedir un número al usuario
def solicitar_numero(mensaje):
    while True:
        entrada = input(mensaje)
        if CalculadoraMCD._validar_numero(entrada):
            return int(entrada)
        else:
            print("Por favor, ingrese un número entero positivo.")


# Programa principal
if __name__ == "__main__":
    num1 = solicitar_numero("Ingrese el primer número entero positivo: ")
    num2 = solicitar_numero("Ingrese el segundo número entero positivo: ")

    calculadora = CalculadoraMCD(num1, num2)
    resultado = calculadora.calcular_mcd()

    print(f"El Máximo Común Divisor de {calculadora.numero1} y {calculadora.numero2} es: {resultado}")
