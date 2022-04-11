import json
import os

# get current working directory path
cwd_path = os.getcwd()

def linear_search(sequence,number_look_for):
    """
    :param sequence:
    :param number_look_for(int):
    :return:
    """
    count = 0
    indicie = list()
    for index,num in enumerate(sequence):
        if num == number_look_for:
            indicie.append(index)
            count += 1
    return {'pozice': indicie, 'count':count}

def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {'unordered_numbers','ordered_numbers','dna_sequence'}:
        return None

    file_path = os.path.join(cwd_path, file_name)

    with open(file_path,'r') as json_file:
        seq = json.load(json_file)
    return seq[field]

def main():
    sequential_data = read_data('sequential.json', 'unordered_numbers')
    print(sequential_data)
    linear = linear_search(sequential_data, 9)
    print(linear)
    pass


if __name__ == '__main__':
    main()