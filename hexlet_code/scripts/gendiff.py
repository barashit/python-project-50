import argparse
import json


def compare_files(file1, file2, format):
    result = f"Comparing {file1} and {file2}"

    if format == 'json':
        result_dict = {
            "status": "success",
            "file1": file1,
            "file2": file2,
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

