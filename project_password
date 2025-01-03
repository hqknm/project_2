import random
import string


def generate_password(length=12):
    # Все возможные символы для пароля
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Генерация пароля нужной длины
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password


def password_strength(password):

    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    # Условия для оценки надежности
    if length >= 12 and has_upper and has_lower and has_digit and has_special:
        return "Высокая"
    elif length >= 8 and (has_upper or has_lower) and has_digit:
        return "Средняя"
    else:
        return "Низкая"


def generate_password_from_words(words, length=12):

    if not words:
        return "Ошибка: список слов пуст."

    random.shuffle(words)
    password = ''.join(words)
    if len(password) < length:
        password += ''.join(random.choices(string.ascii_letters + string.digits, k=length - len(password)))
    return password[:length]

if __name__ == '__main__':
    try:
        user_choice = input("Выберите действие:\n1. Сгенерировать случайный пароль\n2. Сгенерировать пароль из слов\nВаш выбор: ")

        if user_choice == '1':
            user_length = int(input("Введите длину пароля (не менее 6 символов): "))
            if user_length < 6:
                print("Длина пароля должна быть не менее 6 символов.")
            else:
                password = generate_password(user_length)
                print('Сгенерированный пароль:', password)
                print('Надежность пароля:', password_strength(password))

        elif user_choice == '2':
            words_input = input("Введите слова или фразы через пробел: ")
            words = words_input.split()
            user_length = int(input("Введите желаемую длину пароля (не менее 6 символов): "))
            if user_length < 6:
                print("Длина пароля должна быть не менее 6 символов.")
            else:
                password = generate_password_from_words(words, user_length)
                print('Сгенерированный пароль:', password)
                print('Надежность пароля:', password_strength(password))

        else:
            print("Некорректный выбор. Пожалуйста, выберите 1 или 2.")

    except ValueError:
        print("Пожалуйста, введите корректные данные.")
