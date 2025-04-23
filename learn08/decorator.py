import functools
import random

# simple decorator
# def my_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("before")
#         func(*args, **kwargs)
#         print("after")
#     return wrapper
#
# @my_decorator
# def say_hello(message):
#     print(message)
#
# say_hello('hello')

# 装饰器应用
def check_login(request):
    is_check = random.random()
    print(is_check)
    return is_check > 0.5

def authenticate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
       request = args[0]
       if check_login(request):
           return func(*args, **kwargs)
       else:
           raise Exception('login required')
    return wrapper

@authenticate
def post_comment(request):
    print('post comment')

post_comment("abc")