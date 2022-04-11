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
    with open(file_path, 'r') as data_file:
        data = json.load(data_file)
    print(data[field])
    return data[field]

def linear_search(sequential_data, number):
    slovnik = {}
    a = []
    count = 0
    for i, num in enumerate(sequential_data):
        if num == number:
            a.append(i)
            count +=1
    print(a)
    print(count)
    return{"positions": a, "count": count}

def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    number = 0
    linear = linear_search(sequential_data, number)
    print(linear)



if __name__ == '__main__':
    main()