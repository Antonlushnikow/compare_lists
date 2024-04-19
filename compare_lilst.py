import csv
import sys

LIST_NAMES = [
    'FIRST',
    'SECOND',
    'THIRD',
]


def print_help():
    print('Usage: python3 compare_list.py LIST1 LIST2 ... \n'
          'Number of lists sets by LIST_NAMES')


def read_list(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]


def create_csv(output_path):
    files = []

    # Handle arguments
    for i in range(len(LIST_NAMES)):
        try:
            files.append(sys.argv[i+1])
        except IndexError:
            print_help()

    lists = [read_list(l) for l in files]  # list with lists of items from each file
    include_lists = [{item: 'Yes' if item in list_ else 'No' for item in list_} for list_ in lists]  # detect if include in list
    items = tuple(set(item for list_ in lists for item in list_))  # list of all unique items

    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['item', *LIST_NAMES])
        writer.writeheader()

        for item in items:
            dict_ = {'item': item}
            for i, name_ in enumerate(LIST_NAMES):
                dict_[name_] = include_lists[i].get(item, 'No')
            writer.writerow(dict(dict_))

if __name__ == '__main__':
    create_csv('result.csv')
