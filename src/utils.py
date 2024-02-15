import os
import json
from datetime import datetime
from config import ROOT_DIR

OPERATION = os.path.join(ROOT_DIR, 'operations.json')

def get_operations(OPERATION):
    """Функция открытия файла"""
    with open(OPERATION, encoding='UTF8') as file:
        file = json.load(file)

    return file

print(get_operations(OPERATION))


def get_executed_only(file):

    valid_file = list(filter(lambda i: 'id' in i, file))
    executed_operations = list(filter(lambda x: x["state"] == "EXECUTED", valid_file))
    return list(executed_operations)

all_operations = get_operations(OPERATION)
print(all_operations)

filtered_operations = get_executed_only(all_operations)
print(filtered_operations)










def sort_by_date():
    pass


def get_formated_operation():
    pass



# def sorted_date(date):
#     new_data = []
#     for item in date:
#         if item == {}:
#             continue
#         elif item['state'] == 'EXECUTED': # {} .get()
#             new_data.append(item)
#
#     sort_date = sorted(new_data, key=lambda x: x['date'], reverse=True)
#     five_transactions = sort_date[:5]
#
#     return five_transactions





# def format_date(_date):
#     date_format = _date.split('T'[0].split('-'))
#     date_format = '{}.{}.{}'.format(date_format[2], date_format[1], date_format[0])
#     return date_format
#
# print(format_date(open_file['date']))
#
# def silence_card(card):
#     card_silence = '{} {}** **** {}'.format(card[:-12], card[-10:-8], card[-4:])
#     return card_silence
#
# print(silence_card(sorted_date(open_file())))


# def silence_account(account):
#     account_silence = 'Счёт **{}'.format(account[-4:])
#     return account_silence
#
# print(silence_account(sorted_date(open_file())))

# def format_operation(transaction):
#     """
#     "id": 214024827,
#     "state": "EXECUTED",
#     "date": "2018-12-20T16:43:26.929246",
#     "operationAmount": {
#       "amount": "70946.18",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Счет 10848359769870775355",
#     "to": "Счет 21969751544412966366"
#     """
#
#
#     transaction['date'] = sorted_date(transaction['date'])
#     # обработать если нет ключа from
#     transaction['from'] = modify_bill(transaction['from'])
#     #
#     transaction['to'] = modify_bill(transaction['to'])
#     # оставить строку для принта
#
#     return f"14.10.2018 Перевод организации\nVisa Platinum 7000 79** **** 6331 -> Счёт **9638\n82771.72 руб."