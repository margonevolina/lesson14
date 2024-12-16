def calculate_structure_sum(data_structure):
    total_sum = 0
    def process_(i):
        nonlocal total_sum
        if isinstance(i, (int, float)):
            total_sum += i
        elif isinstance(i, str):
            total_sum += len(i)
        elif isinstance(i, (list, tuple, set)):
            for j in i:
                process_(j)
        elif isinstance(i, dict):
            for key, value in i.items():
                process_(key)
                process_(value)
    process_(data_structure)
    return total_sum

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)