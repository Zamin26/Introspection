def introspection_info(obj):                                                            # функция
    value_obj_type = type(obj).__name__                                                 # Определение типа объекта
    value_attributes = [x for x in dir(obj) if not callable(getattr(obj, x))]           # Определение атрибутов объекта
    value_methods = [y for y in dir(obj) if callable(getattr(obj, y))]                  # Определение методов объекта
    value_module = obj.__class__.__module__                                             # Определение модуля объекта


    another_properties = []                                                             # Определение длины объекта
    if hasattr(obj, '__len__'):
        another_properties.append(f"Длина объекта: {len(obj)}")


    if isinstance(obj, (int, float, complex)):                                          # Определение на достоверность
        another_properties.append(f"Является числом: True")                             # и значение 
        another_properties.append(f"Значение числа: {obj}")




# Создание словаря, ключ искомый объект, значение - значение искомого объекта
    dict_introspection_info = {'type': value_obj_type, 'attributes': value_attributes,'methods': value_methods,
                               'module': value_module, 'another_properties': another_properties }
    return dict_introspection_info

number_info = introspection_info(42)                                                    # obj по условию равен 42
print(number_info)

word_info = introspection_info('Hello')                                                 # вместо числа указано слово
print(word_info)
