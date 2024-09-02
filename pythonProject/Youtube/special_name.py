# print("hello"+ __name__)

# this indicates the starting point of execution. it is used mostly in modules. if you are running the code as the main code __name__ will display __main__
# but if you are importing the module __name__ changes to the module name.

# __name__ is useful when you want to run your code if the  module is your main module. ok lets do it like this
def greet():
    print("hello")
    print("welcome User")

if __name__ == '__main__':
    greet()