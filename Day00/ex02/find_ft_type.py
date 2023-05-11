def all_thing_is_obj(object) -> int:
    value = type(object).__name__
    if (value == "str"):
        print(object, ":", type(object))
    elif (isinstance(object, (int, float, complex))):
        print(object)
    else:
        print(value, ":", type(object))
    return 42
