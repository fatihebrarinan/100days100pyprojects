from flask import Flask

app = Flask(__name__)

@app.route('/')#Just a forward slash means home page. The @ indicates this is a python decorator
def hello_world():
    return ('<h1 style="text-align: center">hello world!</h1>'
            '<p>This is a paragraph</p>'
            '<img src="https://www.diamondpet.com/wp-content/uploads/2021/03/kitten-sitting-on-floor-031621.jpg"></img>')

def make_underlined(function):
    def wrapper_function():
        return f'<b> {function()} </b>'
    return wrapper_function


@app.route('/bye')
@make_underlined #Makes the output bold.
def bye():
    return 'Bye'

@app.route('/username/<name>/<int:number>')#Putting a word in <> makes it a variable
def greet(name, number):
    return f"Hello {name}! You are {number}"

# __name__ is a special attribute that tells which file are we running
if __name__ == "__main__":
    app.run(debug=True)




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
## On the wrapper class, I can give infinitely many args and kwargs.
def decorator_function_with_args(function):
    def wrapper_function(*args, **kwargs):
        function(args[0])
    return wrapper_function()
@delay_decorator
def say_hello():
    print("Hello")

def say_bye():
    print("Bye")

