def bubble_sort(items):
    """Return a sorted copy of *items* using the bubble-sort algorithm."""
    result = list(items)

    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if not swapped:
            break

    return result
