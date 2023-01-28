def insertion_sorting(a):
    for j in range(1, len(a)):
        current_element = a[j]
        index_of_previous_el = j - 1

        while index_of_previous_el >= 0 and a[index_of_previous_el] > current_element:
            a[index_of_previous_el + 1] = a[index_of_previous_el]
            index_of_previous_el -= 1
        a[index_of_previous_el + 1] = current_element
    return a


arr = [5, 3, 4, 2, 6, 1]
print(insertion_sorting(arr))
