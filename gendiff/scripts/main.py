import argparse

from gendiff.gendiff import generate_diff


def main():
    """Точка входа в программу."""
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument(
        '-f', "--format", 
        metavar="FORMAT", 
        help="set format of output")
    parser.add_argument("file_1", help='specify the path to the file')
    parser.add_argument("file_2", help='specify the path to the file')
    parser.add_argument("format_name", 
                        help='specify the type of output data')
    args = parser.parse_args()

    print(generate_diff(args.file_1, args.file_2, args.format_name))


if __name__ == "__main__":
    main()
