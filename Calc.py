class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero")
        return a / b


# Example usage of the Calculator class
if __name__ == "__main__":
    calculator = Calculator()
    print("Addition:", calculator.add(5, 3))
    print("Subtraction:", calculator.subtract(5, 3))
    print("Multiplication:", calculator.multiply(5, 3))
    print("Division:", calculator.divide(5, 3))
