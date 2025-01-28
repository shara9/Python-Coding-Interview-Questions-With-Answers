'''A decorator is a function that takes another function as an argument, extends its behavior, and returns a new function'''

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
def say_hello():
    print("Hello!")
# Now we apply our decorator to the function
decorated_function = my_decorator(say_hello)
# Calling the decorated function
decorated_function()


'''output: 
Something is happening before the function is called.
Hello!
Something is happening after the function is called.'''





'''Using the @ Syntax: Python allows a more convenient way to apply decorators using the @ symbol. Let's rewrite our above example:'''

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")
# Calling the decorated function
say_hello()

'''In this case, the line @my_decorator above the say_hello function is a shorthand for applying the decorator.'''





'''Decorator with Arguments
You can also create decorators that accept arguments. Let’s say we want to add a repeated greeting using a decorator:'''

def repeat(times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Shanu")

'''output:
Hello, Shanu!
Hello, Shanu!
Hello, Shanu!

Explanation:
Outer Function: repeat takes an argument times, which indicates how many times to repeat the greeting.
Inner Function: decorator_repeat is defined inside repeat. This is the actual decorator.
Wrapper Function: wrapper is created to execute the original function multiple times.
Applying the Decorator: Using @repeat(3), we specify that the greet function should be called three times.'''






'''Chaining DecoratorsYou can also stack multiple decorators together.'''

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        return original_result.upper()
    return wrapper

@uppercase_decorator
@repeat(2)
def greet(name):
    return f"Hello, {name}!"

print(greet("Shanu"))

'''output:
HELLO, Shanu!
HELLO, Shanu!

In this case, greet first goes through repeat, which executes it twice, then uppercase_decorator transforms the results to uppercase.'''





'''>>>>>>>>>>>real-time use cases for decorators<<<<<<<<<<<<<<<<
Logging: Decorators can be used to log information about function calls, such as arguments passed, return values, and execution time. This is particularly useful for debugging and monitoring applications.'''

import logging

def log_function_call(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function '{func.__name__}' with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper

@log_function_call
def add(x, y):
    return x + y

add(5, 3)




'''Authorization and Access Control: In web applications, decorators can check if a user has the necessary permissions before allowing the execution of a function.'''

def requires_authentication(func):
    def wrapper(user):
        if not user.is_authenticated:
            raise PermissionError("User must be authenticated.")
        return func(user)
    return wrapper

@requires_authentication
def view_sensitive_data(user):
    return "Sensitive Data"

# Example usage:
# user = User(is_authenticated=True)
# print(view_sensitive_data(user))







'''Caching: Caching the results of function calls can improve performance, especially for functions that perform expensive calculations or database queries.'''

from functools import lru_cache

@lru_cache(maxsize=32)
def compute_factorial(n):
    if n == 0:
        return 1
    else:
        return n * compute_factorial(n - 1)

# The results of compute_factorial will be cached for faster retrieval.
print(compute_factorial(5))  # Computes the result
print(compute_factorial(5))  # Retrieved from cache





'''Timing Functions:You can create decorators to measure the time it takes for a function to execute, which is useful for performance monitoring.'''

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    return "Finished"

slow_function()





'''Input Validation: Decorators can enforce certain validation rules for function arguments.'''

def validate_positive(func):
    def wrapper(value):
        if value < 0:
            raise ValueError("Value must be positive.")
        return func(value)
    return wrapper

@validate_positive
def square_root(value):
    return value ** 0.5

print(square_root(9))  # Works fine
# print(square_root(-9))  # Raises ValueError





'''Rate Limiting: In APIs, decorators can be used to restrict how frequently a function can be called, thereby preventing abuse or overuse of resources.'''

import time

def rate_limiter(limit_per_second: int):
    last_called = [0.0]

    def decorator(func):
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            if elapsed < 1.0 / limit_per_second:
                time.sleep(1.0 / limit_per_second - elapsed)
            last_called[0] = time.time()
            return func(*args, **kwargs)

        return wrapper
    return decorator

@rate_limiter(limit_per_second=2)
def print_message(message):
    print(f"{time.time()}: {message}")

# Call print_message multiple times
for i in range(5):
    print_message("Hello, world!")





'''Memoization: Similar to caching, memoization stores the results of expensive function calls and returns the cached result when the same inputs occur again.'''

def memoize(func):
    cache = {}
    def wrapper(x):
        if x not in cache:
            cache[x] = func(x)
        return cache[x]
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Calls the function
print(fibonacci(10))  # Uses the cached result

