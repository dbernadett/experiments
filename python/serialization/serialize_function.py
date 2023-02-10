import inspect
def foo(lmao):
    return lmao + 5
lines = inspect.getsource(foo)
print(lines, end="")