import sys


def ft_counter(arg: str) -> str:
    """return  a string the represent the  value received"""
    content = ["upper letters", "lower letters",
               "spaces", "punctuation marks", "digits"]

    if (arg.isupper()):
        return content[0]
    elif (arg.islower()):
        return content[1]
    elif (arg.isspace()):
        return content[2]
    elif (not (arg.isspace()) and not arg.isalnum()):
        return content[3]
    elif (arg.isdigit()):
        return content[4]
    return "undefined"


def ft_take_user_input():
    return input()


def main():
    line = ""
    if (sys.argv.__len__() == 1):
        line = ft_take_user_input()
    else:
        args = sys.argv[1:]
        for elem in args:
            line = line + elem
        print(line)

    mapping = {"upper letters": 0, "lower letters": 0,
               "spaces": 0, "punctuation marks": 0, "digits": 0}
    for iter in line:
        key = ft_counter(iter)
        value = mapping[key]
        mapping[key] = value + 1

    for key in mapping:
        print(str(mapping[key]) + " " + key, end="\n", sep="\n")


if (__name__ == "__main__"):
    main()
