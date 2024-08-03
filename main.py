def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(1, 'строка', True)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
value_list_ = ['bot', False, 3]
value_dict_ = {'a': True, 'b': 'строка', 'c': 3}
print_params(*value_list_)
print_params(**value_dict_)
value_list2_ = [54.32, 'Строка']
print_params(*value_list2_, 42)
