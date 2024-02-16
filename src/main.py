from src.utils import (operations_list, get_operations, get_executed_only, sort_by_date,
                       last_five_operations, show_recent_operations)

all_operations = get_operations(operations_list)

filtered_operations = get_executed_only(all_operations)

sorted_operations = sort_by_date(filtered_operations)

recent_operations = last_five_operations(sorted_operations)

show_recent_operations(recent_operations)


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


