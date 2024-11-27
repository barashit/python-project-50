#!/usr/bin/env python3

from gendiff.arg_parser import parse_args
from gendiff.generate_diff import generate_diff


def main():
    args = parse_args()
    file1 = args.first_file
    file2 = args.second_file
    name_of_format = args.format
    diff = generate_diff(file1, file2, format_name=name_of_format)

    print(diff)

if __name__ == "__main__":
    main()

