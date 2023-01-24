numbers_dictionary = {}

line = input()

try:
    while line != "Search":
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number
        line = input()

    line_1 = input()

    while line_1 != "Remove":
        searched = line_1
        print(numbers_dictionary[searched])
        line_1 = input()

    line_2 = input()

    while line_2 != "End":
        searched = line_2
        del numbers_dictionary[searched]
        line_2 = input()

except ValueError:
    print("The variable number must be an integer")
except KeyError:
    print("Number does not exist in dictionary")

print(numbers_dictionary)
