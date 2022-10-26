def f1(func):
    def wrapper():
        print("Start")
        func()
        print("Stop")
    return wrapper

@f1
def f():
    print("Hello")

print(f())