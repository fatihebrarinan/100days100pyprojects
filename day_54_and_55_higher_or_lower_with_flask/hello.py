from flask import Flask

app = Flask(__name__)

@app.route('/')#Just a forward slash means home page. The @ indicates this is a python decorator
def hello_world():
    return "hello world!"

# __name__ is a special attribute that tells which file are we running
if __name__ == "__main__":
    app.run()

## Python decorator functions
def decorator_function(function):
    def wrapper_function():
        function()
    return wrapper_function()

##Simple decorator function example
import time
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do smthng before calling the function
        function()
        #Do something after calling the function
    return wrapper_function()

@delay_decorator
def say_hello():
    print("Hello")

def say_bye():
    print("Bye")

