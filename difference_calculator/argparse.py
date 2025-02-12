import argparse

from difference_calculator.gendiff import generate_diff

parser = argparse.ArgumentParser(description='''Compares two
                                                 configuration
                                                 files and shows
                                                 a difference.''',)
parser.add_argument('-f', "--format", metavar="FORMAT",
                    help="set format of output")
parser.add_argument("file1_path")
parser.add_argument("file2_path")
args = parser.parse_args()


def run_diff():
    print(generate_diff(file1_path=args.file1_path,
                        file2_path=args.file2_path))
