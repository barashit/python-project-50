import argparse
import json
import os


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Ошибка: Файл '{file_path}' не является корректным JSON.")
        exit(1)


def compare_files(file1, file2, format):
    file1_path = os.path.join(os.getcwd(), 'data', file1)
    file2_path = os.path.join(os.getcwd(), 'data', file2)

    data1 = read_file(file1_path)
    data2 = read_file(file2_path)

    print(f"Data from {file1_path}: {data1}")
    print(f"Data from {file2_path}: {data2}")

    result = f"Comparing {file1_path} and {file2_path}"

    if format == 'json':
        result_dict = {
            "status": "success",
            "file1": file1_path,
            "file2": file2_path,
            "comparison_result": result
        }
        print(json.dumps(result_dict, indent=2))
    else:
        print(result)


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

    parser.add_argument('first_file', help='the first configuration file to compare')
    parser.add_argument('second_file', help='the second configuration file to compare')

    parser.add_argument(
        '-f', '--format',
        choices=['plain', 'json'],
        default='plain',
        help='set format of output (default is plain)'
    )

    args = parser.parse_args()

    compare_files(args.first_file, args.second_file, args.format)

if __name__ == '__main__':
    main()

