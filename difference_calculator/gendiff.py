from difference_calculator import diff, formater, utilites


def generate_diff(file_1, file_2):
    file1_path: str = utilites.get_the_file_path(file_1)
    file2_path: str = utilites.get_the_file_path(file_2)

    dict1: dict = utilites.get_a_python_object(file1_path)
    dict2: dict = utilites.get_a_python_object(file2_path)

    updated_dict = diff.get_diff(dict1, dict2)

    form = formater.stalish(updated_dict)

    return form
