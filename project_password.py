import random
import string
from typing import List

class PasswordManager:
    def __init__(self, length: int = 12):
        self.length = max(length, 6)  # Минимальная длина пароля — 6 символов
        self.all_chars = string.ascii_letters + string.digits + string.punctuation

    def generate_random_password(self) -> str:
        return ''.join(random.choice(self.all_chars) for _ in range(self.length))

    @classmethod
    def evaluate_strength(password: str) -> str:
        length = len(password)
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special = any(char in string.punctuation for char in password)

        if length >= 12 and has_upper and has_lower and has_digit and has_special:
            return "Высокая"
        elif length >= 8 and (has_upper or has_lower) and has_digit:
            return "Средняя"
        else:
            return "Низкая"

    def generate_password_from_words(self, words: List[str]) -> str:
        """
        Генерация пароля из заданных слов/фраз.
        :param words: список слов/фраз
        :return: сгенерированный пароль.
        """
        if not words:
            raise ValueError("Список слов не должен быть пустым.")

        random.shuffle(words)
        password = ''.join(words)
        if len(password) < self.length:
            password += ''.join(random.choices(self.all_chars, k=self.length - len(password)))
        return password[:self.length]


class PasswordApp:
    def __init__(self):
        self.manager = PasswordManager()

    def run(self):
        print("Выберите действие:\n1. Сгенерировать случайный пароль\n2. Сгенерировать пароль из слов")
        user_choice = input("Ваш выбор: ")

        if user_choice == '1':
            self.handle_random_password()
        elif user_choice == '2':
            self.handle_word_based_password()
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1 или 2.")

    def handle_random_password(self):
        try:
            length = int(input("Введите длину пароля (не менее 6 символов): "))
            self.manager.length = max(length, 6)
            password = self.manager.generate_random_password()
            print('Сгенерированный пароль:', password)
            print('Надежность пароля:', self.manager.evaluate_strength(password))
        except ValueError:
            print("Некорректный ввод. Длина пароля должна быть числом.")

    def handle_word_based_password(self):
        try:
            words_input = input("Введите слова или фразы через пробел: ")
            words = words_input.split()
            length = int(input("Введите желаемую длину пароля (не менее 6 символов): "))
            self.manager.length = max(length, 6)
            password = self.manager.generate_password_from_words(words)
            print('Сгенерированный пароль:', password)
            print('Надежность пароля:', self.manager.evaluate_strength(password))
        except ValueError as e:
            print(f"Ошибка: {e}")


if __name__ == '__main__':
    app = PasswordApp()
    app.run()
