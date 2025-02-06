from difference_calculator import gendiff


def main():
    print(gendiff.generate_diff(gendiff.args.first_file,
                                gendiff.args.second_file))


if __name__ == "__main__":
    main()
