def second_func(value):
    """ 
    Функция для заглавных букв
    """
    list_val = value.split()
    new_list = []
    for val in list_val:
        new_val = val.capitalize()
        new_list.append(new_val)

    return ' '.join(new_list)

