# calculator.py

"""
Este módulo proporciona funciones aritméticas básicas y un controlador de entrada para una calculadora sencilla.
Las operaciones compatibles incluyen raíz cuadrada, potencia, suma, resta, multiplicación y división.
"""

import math

class Calculator: 
    """
    Una clase de calculadora sencilla que realiza operaciones aritméticas básicas.
    """
    def __init__(self):
        """
        Inicializa la calculadora con historia de operaciones.
        """
        self.history = [] # Break pount
    
    def square_root(self, num1):
        """
        Retorna la raíz cuadrada de un número dado y guarda la operacion.
        
        Parametros:
            num1 (float): Un número no negativo.

        Retorna:
            float: La raíz cuadrada de num1.
        """
        if num1 < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        
        result = math.sqrt(num1)
        self.history.append(f"sqrt({num1}) = {result}")
        return result
    
    def power(self, base, exponent):
        """
        Eleva la base a la potencia del exponente y registra la operación.

        Parametros:
        base (float): Numero base.
        exponent (float): Numero exponente al que se elevará la base.

        Retorna:
            float: El resultado de base elevado a exponent.
        """
        result = base ** exponent
        self.history.append(f"{base}^{exponent} = {result}")
        return result
    
    def add(self, num1, num2):
        """
        Retorna la suma de dos numeros y guarda la operacion

        Parametros:
            num1 (float): Primer numero.
            num2 (float): Segundo numero.

        Retorna:
            float: La suma de num1 y num2.
        """
        result = num1 + num2
        self.history.append(f"{num1} + {num2} = {result}")
        return result
    
    def subtract(self, num1, num2):
        """
        Retorna el resultado de la resta de dos numeros y guarda la operacion.

        Parametros:
            num1 (float): Primer numero de donde restar.
            num2 (float): Segundo numero.

        Retorna:
            float: La resta de num1 y num2.
        """
        result = num1 - num2
        self.history.append(f"{num1} - {num2} = {result}")
        return result

    def multiply(self, num1, num2):
        """
        Retorna el resultado de la multiplicación de dos números y guarda la operación.

        Parametros:
            num1 (float): Primer número.
            num2 (float): Segundo número.

        Retorna:
            float: El producto de num1 y num2.
        """
        result = num1 * num2
        self.history.append(f"{num1} * {num2} = {result}")
        return result

    def divide(self, num1, num2):
        """
        Retorna el resultado de la división de dos números y guarda la operación.

        Parametros:
            num1 (float): Numerador.
            num2 (float): Denominador(no ser cero).

        Retorna:
            float: El cociente de num1 y num2.

        Excepcion:
            ValueError: Si se intenta dividir entre cero.
        """
        if num2 == 0:
            raise ValueError("No se puede dividir entre cero.")
        result = num1 / num2
        self.history.append(f"{num1} / {num2} = {result}")
        return result
    
    def get_history(self):
        """
        Retorna la historia de operaciones realizadas.

        Retorna:
            lista: Lista de cadenas que representan las operaciones realizadas.
        """
        return self.history.copy()
    
    def clear_history(self):
        """
        Limpia la historia de operaciones realizadas.
        """
        self.history.clear()
    
    def get_float_input(self, prompt):
        """
        Solicita continuamente al usuario un número hasta que se ingrese un valor válido de tipo.

        Parámetros:
            prompt (str): El mensaje que se muestra al usuario.
        Retorna:
            float: El número válido ingresado por el usuario.
        """
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")
                