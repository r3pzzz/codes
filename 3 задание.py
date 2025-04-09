def filter_greater_than(arr, threshold):
    return [x for x in arr if x > threshold]

result = filter_greater_than([1, 5, 8, 3, 10], 5)
print(result)
