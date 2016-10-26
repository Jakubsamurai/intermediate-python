#some args and kwargs usage
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args("first", "second", "third")

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

greet_me(name='Jakub')

def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

args = ("two" , 4, 6)
test_args_kwargs(*args)

kwargs = {"arg1": 1, "arg2": "two", "arg3": 5}
test_args_kwargs(**kwargs)

import someclass
def get_info(self, *args):
    return "Test data"
someclass.get_info = get_info

#debugging: breakpoints
import pdb

def make_something():
    pdb.set_trace()
    return "I have no time"
print(make_something())
