# hexlet_code/scripts/gendiff.py

import argparse
from hexlet_code.gendiff.generate_diff import generate_diff

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

    diff = generate_diff(args.first_file, args.second_file)

    print(diff)

if __name__ == '__main__':
    main()

