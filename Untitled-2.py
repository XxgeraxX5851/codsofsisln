def duplicate_or_unique(arr):
    total = sum(arr)
    unique_values = set(arr)
    unique_sum = sum(unique_values)
    length = len(arr)
    
    if length == len(unique_values) + 1:
        
        return total - unique_sum
    else:
        return 2* unique_sum - total
