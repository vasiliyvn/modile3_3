def print_params(a, b, c):
    print(a, b, c)


print_params(1, 'строка', True)
value_list_ = [1, 2, 3]
value_dict_ = {'a': 1, 'b': 2, 'c': 3}
value_list2_ = [54.32, 'Строка']
print_params(*value_list_)
print_params(**value_dict_)
print_params(*value_list2_, 42)
