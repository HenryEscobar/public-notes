#
# https://realpython.com/primer-on-python-decorators/
#   ^^^ great page!
# See my_decorators.py in library


import functools
import time

# ----------------------------------------------------

def decorator_do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

# ----------------------------------------------------

# use me in real life
def decorator(func):
    """ boilerplate decorator"""
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        print("before function")
        value = func(*args, **kwargs)
        # Do something after
        print("after function")
        return value
    return wrapper_decorator

# ----------------------------------------------------


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

# ----------------------------------------------------


def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

# ----------------------------------------------------

def printer_header(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        print("-" * 30, "Function: ", func.__name__, '-' * 30)
        value = func(*args, **kwargs)
        return value
    return wrapper_decorator
# ----------------------------------------------------

@printer_header
@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

# ----------------------------------------------------

@printer_header
@debug
@decorator_do_twice
def repeat_me(message):
    print(message)

@printer_header
@decorator
def something(message):
    print(message)

# ----------------------------------------------------
class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

    def get_call_count(self):
        return(self.num_calls)

@printer_header
@CountCalls
def say_whee():
    print("Whee!")



# ----------------------------------------------------


if __name__ == '__main__':
    repeat_me("foobar")
    something("exciiting")
    waste_some_time(10)
    say_whee()
    say_whee()

    print("not accessing this var for some reason. what silly mistake am i doing?")
    print("Using the CountCalls class that was use as a decortorar/class counter")
    print("How many times was whee called? {}".format(say_whee.num_calls))
    foo=say_whee.num_calls
    print(foo)

    

"""
(venv) escobar@basementpc-2020:~/irad/public-notes/python$ python decorators.py 
------------------------------ Function:  wrapper_do_twice ------------------------------
Calling wrapper_do_twice('foobar')
foobar
foobar
'wrapper_do_twice' returned None
------------------------------ Function:  something ------------------------------
before function
exciiting
after function
------------------------------ Function:  waste_some_time ------------------------------
Finished 'waste_some_time' in 0.0165 secs
------------------------------ Function:  say_whee ------------------------------
Call 1 of 'say_whee'
Whee!
------------------------------ Function:  say_whee ------------------------------
Call 2 of 'say_whee'
Whee!
not accessing this var for some reason. what silly mistake am i doing?
Using the CountCalls class that was use as a decortorar/class counter
How many times was whee called? 0
0
(venv) escobar@basementpc-2020:~/irad/public-notes/python$ 
"""
