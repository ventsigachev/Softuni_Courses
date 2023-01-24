class NameTooShortError(Exception):
    """ Raised when username is 4 characters or less """

    def __init__(self, message=None):
        pattern = "Name must be more than 4 characters"
        if not message:
            self.message = pattern
        else:
            self.message = message
        super().__init__(self.message)


class MustContainAtSymbolError(Exception):
    """ Raised when e-mail address does not contain '@' symbol """

    def __init__(self, message=None):
        pattern = "Email must contain @"
        if not message:
            self.message = pattern
        else:
            self.message = message
        super().__init__(self.message)


class InvalidDomainError(Exception):
    """ Raised when domain-name is invalid"""

    def __init__(self, ds, message=None):
        pattern = f"Domain must be one of the following: {', '.join(ds)}"
        if not message:
            self.message = pattern
        else:
            self.message = message
        super().__init__(self.message)


def validate_name(n):
    name = n.split("@")[0]
    if len(name) <= 4:
        raise NameTooShortError()


def validate_symbol(s):
    if "@" not in s:
        raise MustContainAtSymbolError()


def validate_domain(*args):
    domain = args[0].split(".")[-1]
    domains = (f".{x}" for x in args[1])
    if domain not in args[1]:
        raise InvalidDomainError(domains)


while True:
    text = input()
    if text == "End":
        break

    valid_domains = ("com", "bg", "net", "org")
    validate_name(text)
    validate_symbol(text)
    validate_domain(text, valid_domains)

    print("Email is valid")
