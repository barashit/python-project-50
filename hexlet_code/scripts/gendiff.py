import argparse
from hexlet_code.gendiff.generate_diff import generate_diff

def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument(
        'first_file',
        help='The first configuration file to compare.'
    )

    parser.add_argument(
        'second_file',
        help='The second configuration file to compare.'
    )

    parser.add_argument(
        '-f', '--format',
        choices=['plain', 'json', 'stylish'],
        default='stylish',
        help='Set format of output (default is stylish)'
    )

    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file, format_name=args.format)

    print(diff)

if __name__ == '__main__':
    main()

