class NameTooShortError(Exception):
    """ Raised when username is 4 characters or less """
    pass


class MustContainAtSymbolError(Exception):
    """ Raised when e-mail address does not contain '@' symbol """
    pass


class InvalidDomainError(Exception):
    """ Raised when domain-name is invalid"""
    pass


def validate_name(n):
    name = n.split("@")[0]
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")


def validate_symbol(s):
    if "@" not in s:
        raise MustContainAtSymbolError("Email must contain @")


def validate_domain(*args):
    domain = args[0].split(".")[-1]
    domains = [f".{x}" for x in args[1]]
    if domain not in args[1]:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(domains)}")


while True:
    text = input()
    if text == "End":
        break

    valid_domains = ("com", "bg", "net", "org")
    validate_name(text)
    validate_symbol(text)
    validate_domain(text, valid_domains)

    print("Email is valid")
