
# Fn = Fn -1 + Fn -2

fibonacci_cache = {}
fibonacci_cache[0] = 0
fibonacci_cache[1] = 1

def fibonacci(n):
    if n not in fibonacci_cache:
        fibonacci_cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return(fibonacci_cache[n])
    

if __name__ == '__main__':
        user_input = input("Please enter an int): ")

        try:
            if user_input.isdigit():
                n=int(user_input)    # cast the string of user_input to an int
                print(fibonacci(n))
            else:
                print("User input of {} is not a digit!".format(user_input))

        except ValueError:
            print("Input is not a valid number {}".format(user_input))
        except:
            print("what unkown error code did yo do")
        
        
