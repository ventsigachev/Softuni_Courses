def read_matrix_and_text():
    rows, cols = [int(num) for num in input().split()]
    _text = input()

    _matrix = []
    for _ in range(rows):
        _matrix.append([" " for _ in range(cols)])
    return _matrix, _text


def fill_matrix(matrix, text):
    current_text = [letter for letter in text][::-1]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if current_text:
                matrix[row][col] = current_text.pop()
            else:
                current_text = [letter for letter in text][::-1]
                matrix[row][col] = current_text.pop()
    for row in range(len(matrix)):  # Swapping the direction of each second row
        if row % 2 != 0:
            matrix[row] = matrix[row][::-1]
    return matrix


def print_matrix(matrix_to_print):
    for row in matrix_to_print:
        print(''.join(row))


def solve_snake_moves():
    read_matrix, read_text = read_matrix_and_text()
    print_matrix(fill_matrix(read_matrix, read_text))


if __name__ == '__main__':
    solve_snake_moves()
