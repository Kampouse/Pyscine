import time

named_tuple = time.localtime()  # get struct_time
time_string = time.strftime("%B %d %Y ", named_tuple)
timed = time.time()
typed_format = f"{timed:,.2f}"
typed_format_b = f"{timed:,.2e}"
print("Seconds since January 1, 1970", typed_format,
      "or", typed_format_b, "in scientific notation")
print(time_string)
