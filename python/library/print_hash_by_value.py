
import errno
import logging
import os
import random

# sudo apt-get install ispell # easiest way to to get linxu dictionary

def print_dict_by_value(mydict,col_width=20):
    for key, value in sorted(mydict.items(), key=lambda item: item[1]):
        print("{k:15} : {v:15}".format(k=key,v=value))

def load_words(word_file_name='/usr/share/dict/words', MIN_LENGTH=5, MAX_LENGTH=8):
    word_list=[]

    try:
        with open(word_file_name, 'r') as f:
            for line in f:
                line=line.rstrip().lower()
                if line.isalpha():
                    line_lenght=len(line)
                    if (line_lenght >= MIN_LENGTH) and (line_lenght <= MAX_LENGTH):
                        word_list.append(line)
    except IOError as err_x:
        if err_x.errno == errno.ENOENT:
            logging.error('ERROR: {f} does not exist'.format(f=word_file_name))
        elif err_x.errno == errno.EACCES:
            logging.error('ERROR: {f} cannot be read'.format(f=word_file_name))
        else:
            logging.error('ERROR: {f} unknownerror {x}'.format(f=word_file_name,x=err_x))

    return(word_list)
    
if __name__ == '__main__':
    my_dict = {}
    SIZE_OF_DICT=20
    list_of_keys=load_words()
    for i in range(SIZE_OF_DICT+1):
        new_key = random.choice(list_of_keys)
        if new_key in my_dict:
            continue
        my_dict[new_key] = random.randint(0,1000)
        if len(my_dict) >= SIZE_OF_DICT:
            break

    print_dict_by_value(my_dict)


    
