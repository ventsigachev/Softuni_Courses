def linear_search(a, t):
    for i in range(len(a)):
        if a[i] == t:
            return f"The index of target number is {i}"
    return "There is no match"


arr = [1, 3, 40, 50, 98, 100, 20]
target = 4
print(linear_search(arr, target))
