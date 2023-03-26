def merge_sort(word: str) -> str:
    if len(word) > 1:
        middle = len(word) // 2
        left = merge_sort(word[:middle])
        right = merge_sort(word[middle:])
        word = merge(left, right)
    return word


def merge(left: str, right: str) -> str:
    merge_letters = []
    i = 0
    f = 0

    while i < len(left) and f < len(right):
        if left[i] < right[f]:
            merge_letters.append(left[i])
            i += 1
        else:
            merge_letters.append(right[f])
            f += 1

    merge_letters += left[i:] if i < len(left) else right[f:]
    return "".join(merge_letters)


def is_anagram(first_string: str, second_string: str) -> bool:
    sort_first = merge_sort(first_string.lower())
    sort_second = merge_sort(second_string.lower())
    if not sort_first or not sort_second:
        comparison = False
    else:
        comparison = sort_first == sort_second
    return (sort_first, sort_second, comparison)
