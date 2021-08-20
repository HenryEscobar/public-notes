#
# I don't know source of this data... Wish I saved url.
#

# s='0123456789'

# reverse string:
# s[::-1]

import secrets
import string
from timeit import repeat


def reverse_splice(s):
    return(s[::-1])

def reverse_for_loop(s):
    s1=''
    for c in s:
        s1 = c + s1
    return(s1)

def reverse_while_loop(s):
    s1 = ''
    i = len(s) - 1
    while i >= 0:
        s1 = s1 + s[i]
        i = i -1
    return(s1)

def reverse_join_reversed_itr(s):
    s1 = ''.join(reversed(s))
    return(s1)

def reverse_list(s):
    l = list(s)
    l.reverse()
    return(''.join(l))

def reverse_recursion(s):
    if len(s) == 0:
        return(s)
    else:
        return reverse_recursion(s[1:]) + s[0]

def hello_world(s):
    return()
    

if __name__ == '__main__':
    import timeit
    #my_string="Adlkhasd097324jlaskdjakljKLN(!&*@981274kjasd"
    # string_length=2^1024 - too big for recurision! :-D
    string_length=2^512
    my_string=''.join(secrets.choice(string.ascii_uppercase + string.digits)
                                     for i in range(string_length))
    number_runs=100000
    unit_of_time='usec'
    repeat_cnt=3
    functions_to_time=['reverse_splice','reverse_for_loop', 'reverse_while_loop', 
                       'reverse_join_reversed_itr', 'reverse_list','reverse_recursion']
    # functions_to_time.append('hello_world')
    my_setup = 'from __main__ import {import_list}'.format(import_list=','.join(functions_to_time))

    print('The string to be reversed:\n{s}\n'.format(s=my_string))

    for my_code in functions_to_time:
        my_stmt='{c}(s)'.format(c=my_code)
        timed_reults=timeit.repeat(setup=my_setup, 
                                   stmt = my_stmt, 
                                   globals = {'s': my_string},                                 
                                   number=number_runs,
                                   repeat=repeat_cnt)
        print("{code_name}: {t}".format(code_name=my_code, t=timed_reults))

    


'''

Results:

reverse_splice: 0.05225209996569902
reverse_for_loop: 1.946274199988693
reverse_while_loop: 3.5680021999869496
reverse_join_reversed_itr: 0.5986905000172555
reverse_list: 0.5283471000147983
reverse_recursion: 9.329671200015582


Bad copy and paste below. fix it if you want to try it.
python -m timeit --number 100000 --unit usec 'import best_way_to_reverse_string' 'best_way_to_reverse_string.reverse_slicing("striaskdj")'
100000 loops, best of 5: 0.449 usec per loop

python -m timeit --number 100000 --unit usec 'import best_way_to_reverse_string' 'best_way_to_reverse_string.reverse_list("my_string")'
100000 loops, best of 5: 2.46 usec per loop

python -m timeit --number 100000 --unit usec 'import best_way_to_reverse_string' 'best_way_to_reverse_string.reverse_join_reversed_iter("my_string"*10)'
100000 loops, best of 5: 2.49 usec per loop

python -m timeit --number 100000 --unit usec 'import best_way_to_reverse_string' 'best_way_to_reverse_string.reverse_for_loop("my_string"*10)'
100000 loops, best of 5: 5.5 usec per loop

python -m timeit --number 100000 --unit usec 'import best_way_to_reverse_string' 'best_way_to_reverse_string.reverse_while_loop("my_string"*10)'
100000 loops, best of 5: 9.4 usec per loop

python -m timeit --number 100000 --unit usec 'import best_way_to_reverse_string' 'best_way_to_reverse_string.reverse_recursion("ABç∂EF"*10)'
100000 loops, best of 5: 24.3 usec per loop

'''

