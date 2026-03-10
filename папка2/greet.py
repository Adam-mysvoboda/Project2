# greet.py - скрипт для приветствия
def greet_user(name):
    """Приветствует пользователя по имени"""
    return f"Привет, {name}! Добро пожаловать в мир Python."

def ask_how_are_you():
    """Спрашивает, как дела"""
    return "Как твои дела сегодня?"

def say_goodbye():
    """Прощается"""
    return "До свидания! Хорошего дня!"

if __name__ == "__main__":
    print("=== Программа-приветствие ===")
    print(greet_user("Адам"))
    print(ask_how_are_you())
    print(say_goodbye())
