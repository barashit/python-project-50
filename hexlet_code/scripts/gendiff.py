import argparse
from gendiff.generate_diff import generate_diff
import os


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument(
        'first_file',
        help='the first configuration file to compare'
    )

    parser.add_argument(
        'second_file',
        help='the second configuration file to compare'
    )

    parser.add_argument(
        '-f', '--format',
        choices=['plain', 'json'],
        default='plain',
        help='set format of output (default is plain)'
    )

    args = parser.parse_args()

    # Печатаем относительные пути, которые мы получаем через аргументы
    print(f"First file from args: {args.first_file}")
    print(f"Second file from args: {args.second_file}")

    # Формируем правильный путь, убираем лишнее "data"
    file1_path = os.path.abspath(args.first_file)  # Используем путь как есть
    file2_path = os.path.abspath(args.second_file)  # Используем путь как есть

    # Печатаем окончательные пути, чтобы удостовериться, что они правильные
    print(f"Absolute path for first file: {file1_path}")
    print(f"Absolute path for second file: {file2_path}")

    # Проверяем, что файлы существуют
    if not os.path.exists(file1_path):
        print(f"Error: {file1_path} not found!")
    if not os.path.exists(file2_path):
        print(f"Error: {file2_path} not found!")

    # В случае, если пути правильные, продолжаем работу
    diff = generate_diff(file1_path, file2_path)

    print(diff)


if __name__ == '__main__':
    main()
