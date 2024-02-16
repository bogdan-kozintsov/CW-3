from src.utils import (operations_list, get_operations, get_executed_only, sort_by_date,
                       last_five_operations, show_recent_operations)

all_operations = get_operations(operations_list)

filtered_operations = get_executed_only(all_operations)

sorted_operations = sort_by_date(filtered_operations)

recent_operations = last_five_operations(sorted_operations)

show_recent_operations(recent_operations)
