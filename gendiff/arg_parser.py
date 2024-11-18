import argparse

def parse_args():
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

    return parser.parse_args()

