
input_file = 'test.txt'


def read_dictionary(filename):
    my_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            if ':' in line:
                key, value = line.strip().split(':')
                key = key.strip()
                values = []
                for v in value.split(','):
                    values.append(v.strip())
                my_dict[key] = values
    print('\nText converted to dictionary: \n', my_dict)
    return my_dict



def invert_dictionary(d):
    inverted = {}
    for key, values in d.items():
        for value in values:
            if value not in inverted:
                inverted[value] = []
            inverted[value].append(key)
    print('\nInverted dictionary:\n', inverted)
    return inverted


def write_dictionary(filename, f):
    with open(filename, 'w') as file:
        for key, values in f.items():
            file.write(f"{key}: {', '.join(values)}\n")

def do_assignment8():
    input_filename = 'test.txt'
    output_filename = 'inverted.txt'

    original_dict = read_dictionary(input_filename)
    inverted_dict = invert_dictionary(original_dict)
    write_dictionary(output_filename, inverted_dict)
    print('\nInverted dictionary written to', output_filename)

