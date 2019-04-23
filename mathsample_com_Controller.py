import time


def benchmark(func):
    """ Декоратор, выводящий время, которое заняло выполнение декорируемой функции """

    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print()
        func.__name__, time.clock() - t
        return res

    return wrapper


def logging(func):
    """ Декоратор, логирующий работу кода. (хорошо, он просто выводит вызовы, но тут могло быть и логирование!) """

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print()
        func.__name__, args, kwargs
        return res

    return wrapper


def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("{0} была вызвана: {1}x".format(func.__name__, wrapper.count))
        return res

    wrapper.count = 0
    return wrapper
