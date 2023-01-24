def tags(t):
    def main(func):
        def wrapper(*args):
            return f"<{t}>{func(*args)}</{t}>"
        return wrapper
    return main


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
