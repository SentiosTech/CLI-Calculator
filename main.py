# main.py

"""
Punto de entrada principal de la aplicación Calculadora.
Este módulo solo se encarga de iniciar la aplicación.
"""

from src.ui import CalculatorUI

def main():
    """Función principal que inicia la calculadora."""
    app = CalculatorUI()
    app.run()

if __name__ == "__main__":
    main()