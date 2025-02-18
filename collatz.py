current_value = int(input("Please enter a positive integer: "))
values_list = []

while current_value != 1:
    values_list.append(current_value)
    if not current_value % 2:
        current_value = int(current_value/2)
    else:
        current_value = current_value * 3 + 1

values_list.append(1)

# https://stackoverflow.com/questions/15769246/pythonic-way-to-print-list-items
# A Whirlwind Tour of Python by Jake VanderPlas, Iterators: Iterators as function arguments
# print(*values_list)

# alternatively, from lecture:
for value in values_list:
    print(value, end=" ")