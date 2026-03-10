# calculator.py - простой калькулятор для демонстрации
def add(a, b):
    """Возвращает сумму двух чисел"""
    return a + b

def subtract(a, b):
    """Возвращает разность двух чисел"""
    return a - b

def multiply(a, b):
    """Возвращает произведение двух чисел"""
    return a * b

def divide(a, b):
    """Возвращает частное двух чисел"""
    if b != 0:
        return a / b
    else:
        return "Ошибка: деление на ноль"

if __name__ == "__main__":
    print("=== Демонстрация калькулятора ===")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"15 / 3 = {divide(15, 3)}")
