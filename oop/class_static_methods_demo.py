class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: doesn't depend on class or instance data"""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: can access class-level data like calculation_type"""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
