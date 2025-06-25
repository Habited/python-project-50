import argparse

from gendiff.gendiff import generate_diff


def parser_func():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument("file_1", help='specify the path to the file')
    parser.add_argument("file_2", help='specify the path to the file')
    parser.add_argument("-f", "--format", help="set format of output",
                        default='stylish', type=str)

    return parser.parse_args()


def main():
    args = parser_func()
    result = generate_diff(args.file_1, args.file_2, format_name=args.format)
    print(result)


if __name__ == "__main__":
    main()
