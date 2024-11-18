import argparse
from gendiff import *

def main():
    args = parse_args()

    diff = generate_diff(args.first_file, args.second_file, format_name=args.format)

    print(diff)

if __name__ == '__main__':
    main()

