import argparse
from hexlet_code.gendiff.generate_diff import generate_diff

def main():
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    # Добавляем обязательные параметры для файлов
    parser.add_argument(
        'first_file',
        help='The first configuration file to compare.'
    )

    parser.add_argument(
        'second_file',
        help='The second configuration file to compare.'
    )

    # Добавляем опциональный параметр для выбора формата вывода
    parser.add_argument(
        '-f', '--format',
        choices=['plain', 'json', 'stylish'],  # добавляем все возможные форматы
        default='stylish',  # По умолчанию формат stylish
        help='Set format of output (default is stylish)'
    )

    # Чтение аргументов из командной строки
    args = parser.parse_args()

    # Генерация диффа с учетом выбранного формата
    diff = generate_diff(args.first_file, args.second_file, format_name=args.format)

    # Выводим результат
    print(diff)

if __name__ == '__main__':
    main()

