def sample(*args):  # any type of arguments
    z = 0
    for number in args:
        z += number
    return z


print(sample(1, 2, 3))


def humans(*kwargs):  # key word arguments

    return kwargs


person = {"name": "candy", "age": "21"}
print(humans(*person))

# cognitive complexity...how is easy is ur code to read
