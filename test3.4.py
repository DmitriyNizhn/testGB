# name = ("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Агар Саитов",
#         "Инна Ипатова", "Ирина Серова", "Игорь Семенков", "Игорь Игнатьев")
name = ("Иван Сергеев", "Инна Ипатова")
name = list(name)
name.sort(key=lambda x: x.split()[1])
dict = {}
for el in name:
    split_el = el.split()
    letter_surname = split_el[1][0]
    letter_name = split_el[0][0]
    if letter_surname in dict:
        if letter_name in dict[letter_surname]:
            # dict[letter_surname][letter_name] = [dict[letter_surname][letter_name]]
            # dict[letter_surname][letter_name].append(el)
            # srt_dict = dict.popitem()
            # new_dict = {srt_dict[0]: srt_dict[1:]}
            # new_dict[letter_name] = new_dict.setdefault(letter_name, []) + [el]
            dict_name[letter_name] = dict_name.setdefault(letter_name, []) + [el]
        else:
            dict_name = {}
            dict_name[letter_name] = {}
            dict[letter_name] = el
    else:
        dict_surname = {}
        dict_surname[letter_surname] = {}
        dict_name = {}
        dict_name[letter_name] = [el]
        dict_surname.update(dict_name)
        dict.update(dict_surname)
        # dict.update({letter_surname: {letter_name: el}})
print(dict)
