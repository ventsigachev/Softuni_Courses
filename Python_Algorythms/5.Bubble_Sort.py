def bubble_sorting(a):
    iterations = 0
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            iterations += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a, iterations


arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
result = bubble_sorting(arr)
print(f"Sorted list is {result[0]}, for {result[1]} iterations")
