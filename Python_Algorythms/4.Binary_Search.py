# def iterative_binary_search(arr, start, end, target):
#     """Linear Binary Search"""
#     while start <= end:
#         mid = (start + end) // 2
#
#         if arr[mid] < target:
#             start = mid + 1
#         elif arr[mid] > target:
#             end = mid - 1
#         else:
#             return mid
#
#     return start
#
#
# _array = [1, 2, 3, 4, 5, 6, 7]
# tar = 6
#
# result = iterative_binary_search(_array, 0, len(_array) - 1, tar)
# print(result)


def recursive_binary_search(arr, start, end, target):
    """Recursive Binary Search"""
    if end >= start:
        mid = (start + end) // 2
        if arr[mid] < target:
            recursive_binary_search(arr, mid + 1, end, target)
        elif arr[mid] > target:
            return recursive_binary_search(arr, start, mid - 1, target)
        else:
            return mid
    else:
        return None


_array = [1, 2, 3, 4, 5, 6, 7]
tar = 4

result = recursive_binary_search(_array, 0, len(_array) - 1, tar)

if result:
    print(f"Element is present at index: {result}")
else:
    print("Element is not present in array")
