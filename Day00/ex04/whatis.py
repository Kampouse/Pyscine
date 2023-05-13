import sys
import numbers


def is_int(value: str) -> bool:
    value = value.lstrip('-+')
    for content in value:
        if (not (content.isdigit())):
            return False
    return True


def ft_positivity(value: str) -> int:
    sign = '+'
    for content in value:
        if (content.isdigit()):
            break
        sign = content
    if (sign == '+'):
        return 1
    return -1


def init():
    len = sys.argv.__len__()
    assert len != 1, "AssertionError: more than one argument are provided"
    assert is_int(sys.argv[1]), "AssertionError: The argument -> '" + \
        sys.argv[1] + "' is not a number"
    sign = ft_positivity(sys.argv[1])
    value = sys.argv[1].lstrip('-+')
    actual_value = int(value) * sign
    is_even = "Odd"
    if (not (actual_value % 2)):
        is_even = "Even"
    print("I am " + str(actual_value) + " and its " + is_even)


try:
    init()
except AssertionError as error:
    print(error)
