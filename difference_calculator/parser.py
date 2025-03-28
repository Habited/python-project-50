import argparse

from difference_calculator import gendiff

parser = argparse.ArgumentParser(description='''Compares two
                                                 configuration
                                                 files and shows
                                                 a difference.''',)
parser.add_argument('-f', "--format", metavar="FORMAT",
                    help="set format of output")
parser.add_argument("file_1", help='specify the path to the file')
parser.add_argument("file_2", help='specify the path to the file')
args = parser.parse_args()


def run_diff():
    print(gendiff.generate_diff(args.file_1,
                                args.file_2))
