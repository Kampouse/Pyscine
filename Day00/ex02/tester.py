from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

listed = [ft_dict, ft_tuple, ft_set, ft_list,
          '', "je suis beau", None, {}, [], (), 4]
for iter in listed:
    all_thing_is_obj(iter)
