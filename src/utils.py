import os
import json
from config import ROOT_DIR

operations_list = os.path.join(ROOT_DIR, 'operations.json')

def get_operations(operations_list):
    """Функция открытия файла"""
    with open(operations_list, encoding='UTF8') as file:
        file = json.load(file)
    return file


def get_executed_only(file):
    """Функция получает все операции и фильтрует список, возвращая только EXECUTED"""
    valid_file = list(filter(lambda i: 'id' in i, file))
    executed_operations = list(filter(lambda x: x["state"] == "EXECUTED", valid_file))
    return list(executed_operations)


def sort_by_date(executed_operations):
    """Функция получает все выполненные операции и сортирует их по дате в обратном порядке """
    sorted_list = sorted(executed_operations, key=lambda x: x['date'], reverse=True)
    return sorted_list


def last_five_operations(sorted_operations):
    """Функция принимает отсортированные выполненные операции и возвращает 5 последних операций"""
    five_operations = sorted_operations[:5]
    return five_operations


def hide_number(requisites: str):
    """Функция шифрования номера счета или карты"""
    parts = requisites.split()
    number = parts[-1]
    if requisites.lower().startswith('счет'):
        hided_number = f'**{number[-4:]}'
    else:
        hided_number = f'**{number[:4]} {number[4:6]}** **** {number[-4:]}'
    parts[-1] = hided_number
    return ' '.join(parts)


def formate_date(date):
    """Функция форматирования даты"""
    date_only = date[:10]
    parts = date_only.split('-')
    return '.'.join(reversed(parts))
