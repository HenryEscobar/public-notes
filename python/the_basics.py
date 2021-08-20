# from the_basics import *   
# dir(foobar) and type(foobar) are your friends
#
# Examples of ways to print options for a class/variable
# dir(set) 
# print(*dir(set), sep="\n")
# print(' '.join(str(x) for x in dir(set)))
# print(' '.join(map(str,dir(list))))
# print(('\n'.join(dir(list))))
#
# # Utilities
# help('modules')
# pydoc modules
# dir(dict)

# print("something {x} and {y}".format(x=1,y="foo"))
# print(f"{num} something {x * y}")   # Not sure if fan of this format.

my_list=['a','b',1,5, True]   # my_list[0] == 'a'
my_list.append("foobar")

# An array where every item is unique and no index.
my_set=set(my_list)
my_set2={'1','2',5,'bar'}   # only can access elements in a set. no index. not an array!
my_set.add('foo')

my_dict = { 'key1': 'value1', 'key2': 'value2' }  # print(my_dict['key1'])
        
def function_name(x,y="foo"):
    return(x + y)

def hello_world():
    print("hi")

def pass_arg_as_tuple(*arg):  # unlmited args. each one is a tuple
    print(type(arg))
    for i in arg:
        print(i)

def try_except_block(user_input):
    try:
    	if user_input.isdigit():
           foo=int(user_input)    # cast the string of user_input to an int
           print("User input of {} is a digit!".format(user_input))
    	else:
       	   print("User input of {} is not a digit!".format(user_input))
    except ValueError:
	    print("Input is not a valida number")
    except:
	    print("what unkown error code did yo do")
    # return(user_input)

if __name__ == "__main__":
    # user_input=''
    # while user_input.upper() != "Q":
    while True:
        user_input = input("Please enter string or list (Enter q to quit): ")
        for i in user_input.split():   # split(", ") if you wnat to split on , and space
            if i.upper() == "Q":
                print("Exiting as {} was emtered".format(i))
                exit(0)
            try_except_block(i)

    print("User has entered {}. exiting".format(user_input))

