import csv
import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    database = []
    str_list = []
    csv_path = sys.argv[1]

    with open(csv_path) as csv_file:
        reader = csv.DictReader(csv_file)
        str_list = reader.fieldnames[1:]

        for row in reader:
            for str_name in str_list:
                row[str_name] = int(row[str_name])
            database.append(row)

    sequence_path = sys.argv[2]
    with open(sequence_path) as txt_file:
        sequence = txt_file.read()

    computed_counts = {}
    for str_name in str_list:
        computed_counts[str_name] = find_longest_run(sequence, str_name)

    for person in database:
        match = True
        for str_name in str_list:
            if person[str_name] != computed_counts[str_name]:
                match = False
                break

        if match:
            print(person["name"])
            return

    print("No match")


def find_longest_run(sequence, str_name):
    max_run = 0
    str_len = len(str_name)
    seq_len = len(sequence)
    i = 0

    while i < seq_len:
        current_run = 0

        while True:
            start = i + (current_run * str_len)
            end = start + str_len

            if sequence[start:end] == str_name:
                current_run += 1
            else:
                break

        if current_run > max_run:
            max_run = current_run

        if current_run > 0:
            i += current_run * str_len
        else:
            i += 1

    return max_run


if __name__ == "__main__":
    main()
