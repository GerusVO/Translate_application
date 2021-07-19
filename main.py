import json
#from colorama import Fore, Back, Style

new_dict = {
    "work out the solution": ["18.08.2021", "найти решение проблемы"],
}

print(len(new_dict))
# print(new_dict["UDP(User Datagram Protocol) -> socket.SOCK_DGRAM"])

def change_data(key):
    response = input(
        'Нажмите ентер если знаете слово, если нет введите день пробел и месяц когда хотите его повторить:')  # добавляем активность между выводом
    if response:
        day, month = response.split()
        new_dict[key][0] = f"{day}.{month}.2021"

def foo():
    """функция которая выводит слова с указаной датой и меняет ее на указаную. Есть пробелы
    для того чтобы увидеть слово
    data - определяет какое именно число нужно повторять слова"""
    data = int(input(f'Введите цифру которая присвоенна дате которую хотите повторить {all_data()}\n'))
    data = all_data()[data-1][1]
    lang = input('Напишите rus или eng или both. Чтобы выбрать язык:\n')
    if lang == 'eng':
        for key in new_dict.keys():  # Санчала английские слова
            if new_dict[key][0] == data: # Запрашиваем конкретную дату.
                print(key)
                need_to_repeat(key)
                print(key, '--> ', end='')
                print(new_dict[key][1])
                print(f'\n{"*"*80}')


    elif lang == 'rus':
        for key in new_dict.keys():  # Санчала английские слова
            if new_dict[key][0] == data: # Запрашиваем конкретную дату.
                print(new_dict[key][1])
                need_to_repeat(key)
                print(new_dict[key][1], '--> ', end = '')
                print(key)
                print(f'\n{"*"*80}')


    elif lang == 'both':
        for key in new_dict.keys():  # Санчала английские слова
            if new_dict[key][0] == data:  # Запрашиваем конкретную дату.
                print(f'{key} - {new_dict[key][1]}\n{"*" * 80}')


def all_data():
    """функция которая собирает все даты слов и возвращает их пронумированым списком"""
    list_data = []
    for key in new_dict.keys():
        if new_dict[key][0] not in list_data:
            list_data.append(new_dict[key][0])
    return list(enumerate(list_data, 1))


def need_to_repeat(dict_key):
    """Фунция которая запрашивает у пользователя нужно ли ему повторить это слово если нужно
    то сохраняет его в блокнот для удобства."""
    ans = input('Введите любой символ если хотите повторить слово.')
    if ans:
        with open('repeat.txt', 'a') as f:
            f.write(f'{new_dict[dict_key][1]} - {dict_key}\n')

foo()

