from src.utils import (operations_list, get_operations, get_executed_only, sort_by_date,
                       last_five_operations, formate_date, hide_number)

all_operations = get_operations(operations_list)

filtered_operations = get_executed_only(all_operations)

sorted_operations = sort_by_date(filtered_operations)

recent_operations = last_five_operations(sorted_operations)

for operation in recent_operations:
    date = formate_date(operation['date'])
    description = operation['description']
    amount = operation["operationAmount"]['amount']
    operation_to = hide_number(operation['to'])
    if operation.get('from', False) != False:
        operation_from = hide_number(operation['from'])
        print(f'{date} {description}\n{operation_from} -> {operation_to}\n{amount} руб.\n')
    else:
        print(f'{date} {description}\n-> {operation_to}\n{amount} руб.\n')

# "date" (форматированная) "description"
# "from" (с шифром) -> "to" (с шифром)
# "amount" руб.


# "id": 441945886,
# "state": "EXECUTED",
# "date": "2019-08-26T10:50:58.294041",
# "operationAmount": {
#   "amount": "31957.58",
#   "currency": {
#     "name": "руб.",
#     "code": "RUB"
#   }
# },
# "description": "Перевод организации",
# "from": "Maestro 1596837868705199",
# "to": "Счет 64686473678894779589"


# # Пример вывода для одной операции:
# 14.10.2018 Перевод организации
# Visa Platinum 7000 79** **** 6361 -> Счет **9638
# 82771.72 руб.
