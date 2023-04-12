# def update_dict(key, value, defaults={}):
#     defaults[key] = value
#     print(defaults)
#
#
# update_dict(key='fruit', value='apple')  # Здесь простое создание новой пары ключ-значение в пустом словаре
# update_dict(key='vegetable', value='tomato', defaults={'tree': 'oak'})  # Здесь добавление новой пары
# vegetable-tomato в словарь также переданный в функцию параметром defaults. Словарь создаётся заново.
# update_dict(key='car', value='ferrari') # Здесь словарь опять создаётся заново.
#
# Вывод будет такой:
#
# {'fruit': 'apple'}
# {'tree': 'oak', 'vegetable': 'tomato'}
# {'fruit': 'apple', 'car': 'ferrari'}
#
# Если задача была добавлять пары в словарь и "не терять" старые значения, то нужно добавить ещё один
# параметр и каждый раз сливать два словаря, "новый" и "старый". У меня получилось так:

def update_dict(key, value, defaults={}, result={}):
    defaults[key] = value
    result.update(defaults)
    print(result)

update_dict(key='fruit', value='apple')
update_dict(key='vegetable', value='tomato', defaults={'tree': 'oak'})
update_dict(key='car', value='ferrari')