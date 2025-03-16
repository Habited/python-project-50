from difference_calculator import diff
from difference_calculator import utilites


def generate_diff(file1, file2):
    file_1 = utilites.get_the_file_path(file1)
    file_2 = utilites.get_the_file_path(file2)
    res = []
    for key1, value1 in file_1.items():
        if diff.get_diff(file_1) in file_2:
            res.append(f'{key1}:\n{value1}')
        else:
            res.append(f'- {key1}: \n{value1}')
    res = '\n'.join(res)
    print(res)