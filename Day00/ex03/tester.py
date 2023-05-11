from NULL_not_found import NULL_not_found
stored_variable = {"String": "", "array": [],
                   "object": {}, "none": None, "float": float("NaN")}
for var in stored_variable.keys():
    print(str(var) + ":", stored_variable[var], type(stored_variable[var]),)
print("-----------------")
print(NULL_not_found("hello"))
print(NULL_not_found(""))
print(NULL_not_found(None))
print(NULL_not_found(False))
print(NULL_not_found([]))
print(NULL_not_found({}))
