def sort_with_builtin(arr):
    return sorted(arr)


def count_occurrences(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq