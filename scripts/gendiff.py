import argparse
from gendiff.generate_diff import generate_diff
from gendiff.arg_parser import arg_parser

def main():
    args = parse_args()

    diff = generate_diff(args.first_file, args.second_file, format_name=args.format)

    print(diff)

if __name__ == '__main__':
    main()

