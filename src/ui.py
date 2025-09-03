# ui.py
"""
Calculadora básica en consola implementada con principios sólidos de POO.
"""
from src.calculator import Calculator

class CalculatorUI:
    """
    Programa de calculadora que permite al usuario seleccionar opciones desde un menú.
    """
    def __init__(self):
        """
        Inicializa la aplicación de la calculadora.
        """
        self.calculator = Calculator()
        self.setup_operations() # Break point
    
    def setup_operations(self):
        """
        Configura el mapeo de operaciones utilizando una estructura adecuada de programación orientada a objetos
        """
        self.operations = {
            1: ("Raíz Cuadrada", self.handle_square_root),
            2: ("Potencia", self.handle_power),
            3: ("Suma", self.handle_addition),
            4: ("Resta", self.handle_subtraction),
            5: ("Multiplicación", self.handle_multiplication),
            6: ("División", self.handle_division),
            7: ("Historial", self.show_history),
            8: ("Limpiar Historial", self.clear_history),
            9: ("Salir", self.exit_program)
        }

    def show_menu(self):
        """
        Muestra el menú de operaciones disponibles.
        """
        print("\n" + "="*40)
        print("Menú de Calculadora")
        print("Seleccione una operación:")
        print("="*40)
        for key, (name, _) in self.operations.items():
            print(f"{key}: {name}")
        print("="*40)
    
    def handle_square_root(self):
        """
        Maneja la operación de raíz cuadrada.
        """
        print("\nHas seleccionado la operación de raíz cuadrada.")
        num = self.calculator.get_float_input("Ingrese un número no negativo: ")
        try:
            result = self.calculator.square_root(num)
            print(f"La raíz cuadrada de {num} es {result:.3f}")
        except ValueError as e:
            print(f"Error: {e}")
    
    def handle_two_numbers_operation(self, operation_name, operation_method):
        """
        Maneja operaciones que requieren dos números.
        """
        print(f"\nHas seleccionado la operación de {operation_name}.")
        num1 = self.calculator.get_float_input("Ingrese el primer número: ")
        num2 = self.calculator.get_float_input("Ingrese el segundo número: ")
        
        try: # Break point
            result = operation_method(num1, num2)
            print(f"El resultado de {operation_name} entre {num1} y {num2} es {result:.3f}")
        except ValueError as e:
            print(f"Error: {e}")
    
    def handle_power(self):
        """
        Maneja la operación de potencia.
        """
        self.handle_two_numbers_operation("Potencia", self.calculator.power)
    
    def handle_addition(self):
        """
        Maneja la operación de suma.
        """
        self.handle_two_numbers_operation("Suma", self.calculator.add)
    
    def handle_subtraction(self):
        """
        Maneja la operación de resta.
        """
        self.handle_two_numbers_operation("Resta", self.calculator.subtract)
    
    def handle_multiplication(self):
        """
        Maneja la operación de multiplicación.
        """
        self.handle_two_numbers_operation("Multiplicación", self.calculator.multiply)
    
    def handle_division(self):
        """
        Maneja la operación de división.
        """
        self.handle_two_numbers_operation("División", self.calculator.divide)

    def show_history(self):
        """
        Muestra el historial de operaciones.
        """
        print("\nHistorial de operaciones:")
        if not self.calculator.get_history():
            print("No hay operaciones en el historial.")
        else:
            for i, operation in enumerate(self.calculator.get_history(),1):
                print(f"{i} - {operation}")
    
    def clear_history(self):
        """
        Limpia el historial de operaciones.
        """
        self.calculator.clear_history()
        print("Historial de operaciones limpiado.")
    
    def exit_program(self):
        """
        Sale del programa.
        """
        print("Saliendo del programa...")
        return True
    
    def run(self):
        """
        Bucle principal del programa.
        """
        while True:
            self.show_menu()

            try:
                option = int(input("\nElige la opción: "))
                if option not in self.operations: # Break point
                    print("Opción no válida. Por favor, elige una opción del menú.")
                    continue
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número.")
                continue
            operation_name, operation_func = self.operations[option]

            if option == 9:
                if operation_func():
                    break
            else:
                operation_func()