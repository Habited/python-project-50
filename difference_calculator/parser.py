import argparse

from difference_calculator.gendiff import generate_diff

parser = argparse.ArgumentParser(description='''Compares two
                                                 configuration
                                                 files and shows
                                                 a difference.''',)
parser.add_argument('-f', "--format", metavar="FORMAT",
                    help="set format of output")
parser.add_argument("file1")
parser.add_argument("file2")
args = parser.parse_args()


def run_diff():
    print(generate_diff(args.file1,
                        args.file2))
