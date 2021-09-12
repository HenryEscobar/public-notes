
import logging
import random
import sys

# sudo apt-get install ispell # easiest way to to get linux dictionary


def print_dict_by_value(my_dict, col_width=20):
    for key, value in sorted(my_dict.items(), key=lambda item: item[1]):
        print("{k:15} : {v:15}".format(k=key, v=value))


def load_words(word_file_name='/usr/share/dict/words', MIN_LENGTH=5, MAX_LENGTH=8):
    word_list = []

    try:
        f = open(word_file_name, 'r')
    except FileNotFoundError:
        logging.error('ERROR: {f} does not exist. May need to install ispell'.format(f=word_file_name))
        sys.exit(4)
    except OSError:
        logging.error('ERROR: OS Error opening {f}'.format(f=word_file_name))
        sys.exit(5)
    except Exception as err:
        logging.error('ERROR: Unexpected error opening {f} is {e}'.format(f=word_file_name, e=repr(err)))
        sys.exit(6)
    else:
        for line in f:
            line = line.rstrip().lower()
            if line.isalpha():
                line_length = len(line)
                if (line_length >= MIN_LENGTH) and (line_length <= MAX_LENGTH):
                    word_list.append(line)
    return(word_list)


if __name__ == '__main__':
    my_dict = {}
    SIZE_OF_DICT = 20
    list_of_keys = load_words()
    for i in range(SIZE_OF_DICT+1):
        new_key = random.choice(list_of_keys)
        if new_key in my_dict:
            continue
        my_dict[new_key] = random.randint(0, 1000)
        if len(my_dict) >= SIZE_OF_DICT:
            break

    print_dict_by_value(my_dict)
