import os
import json

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
    with open(file_path, "r") as json_file:
        data = json.load(json_file)

    return data[field]


def linear_search(sequence, number):
    indices = []
    count = 0
    idx = 0
    while idx < len(sequence):
        if sequence[idx] == number:
            count = count + 1
            indices.append(idx)
        idx = idx + 1

    return {"positions": indices, "count": count}


def pattern_search(sequence, pattern):
    pos = set()
    idx = 0
    while idx < len(sequence) - len(pattern):
        index = 0   # substring = sequence[idx:idx + len(pattern)]
        while index < len(pattern):
            if sequence[idx + index] == pattern[index]:
                index = index + 1   # if substring == pattern:
            else:
                break
        else:
            pos.add(idx)
        idx = idx + 1

    return pos


def binary_search(sequence, number):
    left = 0
    right = len(sequence) - 1
    middle = right // 2
    while right >= left:
        if sequence[middle] == number:
            return middle
        elif sequence[middle] < number:
            left = middle + 1
            middle = (left + right) // 2
        elif sequence[middle] > number:
            right = middle - 1
            middle = (left + right) // 2
    return None


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    my_number = 10
    results = linear_search(sequential_data, my_number)
    print(results)

    sequential_data = read_data("sequential.json", "dna_sequence")
    my_pattern = "ATA"
    results = pattern_search(sequential_data, my_pattern)
    print(results)

    sequential_data = read_data("sequential.json", "ordered_numbers")
    my_number = 5
    results = binary_search(sequential_data, my_number)
    print(results)


if __name__ == '__main__':
    main()