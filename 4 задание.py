def find_min_max(arr):
    if not arr:  # Проверка на пустой массив
        return None, None
    return min(arr), max(arr)


result1 = find_min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(result1)

result2 = find_min_max([])
print(result2)