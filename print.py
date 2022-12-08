def hello(name):
    if name == "":
        raise Exception("name is empty")
    if len(name) > 30:
        raise Exception("more than 30 characters")
    return "Hello " + name


print("Hello world")