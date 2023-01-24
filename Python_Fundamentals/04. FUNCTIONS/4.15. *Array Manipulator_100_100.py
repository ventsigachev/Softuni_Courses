initial_list = [int(num) for num in input().split()]

result = ''

while True:
    input_data = input().split()

    if input_data[0] == "end":
        break

    if input_data[0] == "exchange":
        i = int(input_data[1])
        if 0 <= i < len(initial_list):
            initial_list = initial_list[i + 1:] + initial_list[:i + 1]
        else:
            result += f"Invalid index\n"

    elif input_data[0] == "max":
        end_index = -1
        maximum = -999999999999999999999999999999999

        if input_data[1] == "even":
            for ind, value in enumerate(initial_list):
                if value % 2 == 0 and value >= maximum:
                    maximum = value
                    end_index = ind
        elif input_data[1] == "odd":
            for ind, value in enumerate(initial_list):
                if value % 2 == 1 and value >= maximum:
                    maximum = value
                    end_index = ind

        if end_index < 0:
            result += f"No matches\n"
        else:
            result += f"{end_index}\n"

    elif input_data[0] == "min":
        end_index = -1
        maximum = 999999999999999999999999999999999

        if input_data[1] == "even":
            for ind, value in enumerate(initial_list):
                if value % 2 == 0 and value <= maximum:
                    maximum = value
                    end_index = ind

        elif input_data[1] == "odd":
            for ind, value in enumerate(initial_list):
                if value % 2 == 1 and value <= maximum:
                    maximum = value
                    end_index = ind

        if end_index < 0:
            result += f"No matches\n"
        else:
            result += f"{end_index}\n"

    elif input_data[0] == "first":
        new_list = list()

        if int(input_data[1]) > len(initial_list):
            result += f"Invalid count\n"
            continue
        else:
            if input_data[2] == "even":
                for num in initial_list:
                    if num % 2 == 0:
                        new_list.append(num)

            elif input_data[2] == "odd":
                for num in initial_list:
                    if num % 2 == 1:
                        new_list.append(num)

        result_list = new_list[: int(input_data[1])]
        result += f"{result_list}\n"

    elif input_data[0] == "last":
        new_list = list()

        if int(input_data[1]) > len(initial_list):
            result += f"Invalid count\n"
            continue
        else:
            if input_data[2] == "even":
                for num in initial_list:
                    if num % 2 == 0:
                        new_list.append(num)

            elif input_data[2] == "odd":
                for num in initial_list:
                    if num % 2 == 1:
                        new_list.append(num)

        temp_list = list(reversed(new_list))
        result_list = list(reversed(temp_list[: int(input_data[1])]))
        result += f"{result_list}\n"

result += f"{initial_list}"
print(result)
