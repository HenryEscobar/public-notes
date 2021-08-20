
## File manipulation

str=input('give me data')
colors = eval(input('list favorite colors: '))# must be python... useless just use like this:
age = int(input('how old are you: '))

# obj = open(f_name, [access_mode], [buffering])

def read_file(filename):
    with open(filename, 'r') as fh:
        for line in fh:
            # do work
            print(line)

# Working with strings
