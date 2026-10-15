def my_decorator(func):
    def wrapper():
        print("Действие ДО вызова функции")
        func()
        print("Действие ПОСЛЕ вызова функции")

    return wrapper


@my_decorator
def say_hello():
    print("Привет!")


say_hello()
