import os
import json


# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, 'r') as json_file:
        seq = json.load(json_file)

    return seq[field]


def linear_search(sequence, number):
    indices = list()
    count = 0
    for index, num in enumerate(sequence):
        if num == number:
            indices.append(index)
            count += 1
    return {"position": indices, "count": count}


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    linear = linear_search(sequential_data, 0)
    print(linear)
    pass


if __name__ == '__main__':
    main()