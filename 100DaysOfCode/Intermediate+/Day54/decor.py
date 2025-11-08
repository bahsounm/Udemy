# python decorators

# this is the general definition
# def decorator(function):
#     def wrapper_function():
#         function()
#     return wrapper_function
import time
def delay_decorator(function):
    def wrapper_function():
        print("We have etered and will wait 2 seconds")
        time.sleep(2)
        print("2 seconds are done now run the fucntions")
        function()
        print("we finished running the fucntion")
    return wrapper_function

# lets say we wanted to wait before we said hello, there are 2 ways to do this
    # one way is to import time and add a delay just before we print hello
    # the second way, is better if we want to do this to multiple functions and have the abilty to add more fucntionsality

@delay_decorator
def say_hello():
    print("Hello")

# or we could do this
dec_fun = delay_decorator(say_hello)
dec_fun()
