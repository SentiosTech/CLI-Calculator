# test_calculator.py

"""
Pruebas unitarias para el módulo calculator.py usando pytest.

Basado en Python Crash Course 3ra edición - Enfoque para principiantes.
"""

import pytest
from cli.calculator import Calculator


class TestCalculator:
    """Clase de pruebas para la calculadora."""
    
    def setup_method(self):
        """Método de setup que se ejecuta antes de cada prueba."""
        self.calc = Calculator()
        print("\n" + "="*50)
        print("Iniciando nuevo test...")
        print("="*50)
    
    def teardown_method(self):
        """Método que se ejecuta después de cada test."""
        print(f"Test completado. Historial: {len(self.calc.get_history())} operaciones")
        print("="*50)

    def test_add_two_numbers(self):
        """Prueba que la suma de dos números sea correcta."""
        result = self.calc.add(5, 3)
        assert result == 8
        assert f"5 + 3 = {result}" in self.calc.get_history()

    def test_add_negative_numbers(self):
        """Prueba suma con números negativos."""
        result = self.calc.add(-5, -3)
        assert result == -8
        assert f"-5 + -3 = {result}" in self.calc.get_history()

    def test_add_mixed_numbers(self):
        """Prueba suma de números positivos y negativos."""
        result = self.calc.add(10, -3)
        assert result == 7
        assert f"10 + -3 = {result}" in self.calc.get_history()

    def test_add_zero(self):
        """Prueba suma con cero."""
        result = self.calc.add(10, 0)
        assert result == 10
        assert f"10 + 0 = {result}" in self.calc.get_history()

    def test_add_decimal_numbers(self):
        """Prueba suma con números decimales."""
        result = self.calc.add(2.5, 3.5)
        assert result == 6.0
        assert f"2.5 + 3.5 = {result}" in self.calc.get_history()

    def test_subtract_two_numbers(self):
        """Prueba que la resta de dos números sea correcta."""
        result = self.calc.subtract(10, 4)
        assert result == 6.0
        assert f"10 - 4 = {result}" in self.calc.get_history()
    
    def test_subtract_negative_result(self):
        """Prueba resta que da resultado negativo."""
        result = self.calc.subtract(5, 10)
        assert result == -5.0
    
    def test_multiply_two_numbers(self):
        """Prueba que la multiplicación sea correcta."""
        result = self.calc.multiply(6, 7)
        assert result == 42.0
        assert f"6 * 7 = {result}" in self.calc.get_history()
    
    def test_multiply_by_zero(self):
        """Prueba multiplicación por cero."""
        result = self.calc.multiply(5, 0)
        assert result == 0.0
    
    def test_divide_two_numbers(self):
        """Prueba que la división sea correcta."""
        result = self.calc.divide(10, 2)
        assert result == 5.0
        assert f"10 / 2 = {result}" in self.calc.get_history()
    
    def test_divide_by_zero_raises_error(self):
        """Prueba que dividir por cero lance ValueError."""
        with pytest.raises(ValueError, match="No se puede dividir entre cero."):
            self.calc.divide(10, 0)
    
    def test_divide_negative_numbers(self):
        """Prueba división con números negativos."""
        result = self.calc.divide(-10, 2)
        assert result == -5.0
    
    def test_power_operation(self):
        """Prueba la operación de potencia."""
        result = self.calc.power(2, 3)
        assert result == 8.0
        assert f"2^3 = {result}" in self.calc.get_history()
    
    def test_power_zero_exponent(self):
        """Prueba potencia con exponente cero."""
        result = self.calc.power(5, 0)
        assert result == 1.0
    
    def test_power_negative_exponent(self):
        """Prueba potencia con exponente negativo."""
        result = self.calc.power(2, -2)
        assert result == 0.25
    
    def test_square_root_positive_number(self):
        """Prueba raíz cuadrada de número positivo."""
        result = self.calc.square_root(9)
        assert result == 3.0
        assert f"sqrt(9) = {result}" in self.calc.get_history()
    
    def test_square_root_zero(self):
        """Prueba raíz cuadrada de cero."""
        result = self.calc.square_root(0)
        assert result == 0.0
    
    def test_square_root_negative_raises_error(self):
        """Prueba que raíz cuadrada de negativo lance error."""
        with pytest.raises(ValueError, match="No se puede calcular la raíz cuadrada de un número negativo."):
            self.calc.square_root(-4)
    
    def test_get_history_after_multiple_operations(self):
        """Prueba que el historial contenga múltiples operaciones."""
        # Realizar varias operaciones
        self.calc.add(1, 2)
        self.calc.subtract(5, 3)
        self.calc.multiply(2, 4)
        
        history = self.calc.get_history()
        
        assert len(history) == 3
        assert "1 + 2 = 3" in history
        assert "5 - 3 = 2" in history
        assert "2 * 4 = 8" in history
    
    def test_clear_history(self):
        """Prueba que clear_history limpie el historial."""
        # Agregar algunas operaciones
        self.calc.add(1, 2)
        self.calc.subtract(5, 3)
        
        # Verificar que hay operaciones
        assert len(self.calc.get_history()) == 2
        
        # Limpiar historial
        self.calc.clear_history()
        
        # Verificar que está vacío
        assert len(self.calc.get_history()) == 0
    
    def test_history_returns_copy(self):
        """Prueba que get_history retorne una copia, no la referencia."""
        self.calc.add(1, 1)
        
        history1 = self.calc.get_history()
        history2 = self.calc.get_history()
        
        # Deben ser iguales en contenido
        assert history1 == history2
        
        # Pero deben ser objetos diferentes (copias)
        assert history1 is not history2