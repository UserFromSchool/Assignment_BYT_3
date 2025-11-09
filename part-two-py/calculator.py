from typing import Literal


class Calculator:
    """
    Simple calculator class implementation supporting addition, subtraction, multiplication, and division.
    As task says takes the method as a intialization parameter, not method argument.
    """

    def __init__(self, operation: Literal["+", "-", "*", "/"]):
        self.mode = operation
        if operation == "+":
            self.operation = lambda a, b: self._add(a, b)
        elif operation == "-":
            self.operation = lambda a, b: self._subtract(a, b)
        elif operation == "*":
            self.operation = lambda a, b: self._multiply(a, b)
        elif operation == "/":
            self.operation = lambda a, b: self._divide(a, b)
        else:
            raise NotImplementedError(f"Operation not supported: {operation}")

    def _validate_operands(self, a: float, b: float) -> None:
        allowed_types = (float, int)
        if not any(isinstance(a, t) for t in allowed_types) or not any(isinstance(b, t) for t in allowed_types):
            raise TypeError(f"Operands must be floats or ints. Got {type(a)} and {type(b)} instead.")

    def _add(self, a: float, b: float) -> float:
        self._validate_operands(a, b)
        return a + b

    def _subtract(self, a: float, b: float) -> float:
        self._validate_operands(a, b)
        return a - b

    def _multiply(self, a: float, b: float) -> float:
        self._validate_operands(a, b)
        return a * b

    def _divide(self, a: float, b: float) -> float:
        self._validate_operands(a, b)
        return a / b

    def calculate(self, a: float, b: float) -> float:
        self._validate_operands(a, b)
        return self.operation(a, b)

    def __str__(self) -> str:
        return f"Caclulator supporting {self.mode} operation."

    def __repr__(self) -> str:
        return f"Calculator(mode={self.mode})"
        

if __name__ == "__main__":
    print("Addition: 1 + 2 = ", end="")
    print(Calculator('+').calculate(1, 2))
    print("Subtraction: 1 - 2 = ", end="")
    print(Calculator('-').calculate(1, 2))
    print("Multiplication: 1 * 2 = ", end="")
    print(Calculator('*').calculate(1, 2))
    print("Division: 1 / 2 = ", end="")
    print(Calculator('/').calculate(1, 2))
