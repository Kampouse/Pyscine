import sys
import re


def is_int(Str: str) -> bool:
    try:
        int(Str)
    except ValueError:
        return False
    return True


def lst_of_valid_str(Str: str, len: int) -> list[str]:
    lst = re.split('\t| | \r| \v', Str)
    return [elm for elm in lst if elm.__len__() > len]


def main():
    if (sys.argv.__len__() == 1):
        print(
            "AssertionError: the arguments are bad: Expect [string,number]\n \
Got [None]")
    elif (sys.argv.__len__() == 2):
        print("AssertionError: the arguments are bad: Expect[string,number]\n \
Got [any]")
    elif (sys.argv.__len__() == 3):
        if (type(sys.argv[2]) == str and is_int(sys.argv[2])):
            print(lst_of_valid_str(sys.argv[1], int(sys.argv[2])))
        else:
            print("AssertionError: wrong type of arguments")

    else:
        print("handling error is important do your job")


if (__name__ == "__main__"):
    main()
