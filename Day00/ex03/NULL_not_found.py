class Empty(object):
    def __eq__(self, other):
        return not other


def NULL_not_found(object) -> int:
    """return if the value provided is a null or not"""
    stuff = Empty()

    if (object == stuff):
        return 0
    elif (isinstance(object, (float, int))):
        if (object > 0 or object < 0):
            return 0
        else:
            return 1
    else:
        return 1
