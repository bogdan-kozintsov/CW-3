# import json

# from utils import open_file, sorted_date, format_operation

# file = open_file() # Все операции
# date = modify_date(file) # только executed
# data = date.sort()[:5] # [start:stop:step] сортируем по дате, и выводим последние 5 операций
#
# for transaction in date:
#     formated = format_operation(transaction)
#     print(formated)



# ниже код из консультации с наставником:


import json
from src.utils import get_operations, get_executed_only, sort_by_date, get_formated_operation

all_operations = get_operations('operations.json')
print(all_operations)

filtered_operations = get_executed_only(all_operations)
print(filtered_operations)

sorted_operations = sort_by_date(filtered_operations)
print(sorted_operations)

five_operations = sorted_operations[:5]
print(five_operations)


for operation in five_operations:
    print(get_formated_operation(operation))
