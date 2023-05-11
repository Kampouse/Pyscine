
class Empty(object):
    def __eq__(self, other):
        return not other


def NULL_not_found(object) -> bool:
    stuff = Empty()
    if (object == stuff):
        return True
    elif (isinstance(object, (float, int))):
        if (object > 0 or object < 0):
            return False
        else:
            return True
    else:
        return False


print(NULL_not_found(False))
print(NULL_not_found(""))
print(NULL_not_found([]))
print(NULL_not_found({}))
print(NULL_not_found(None))
print(NULL_not_found(float("NaN")))
print(NULL_not_found(float("25.5")))
