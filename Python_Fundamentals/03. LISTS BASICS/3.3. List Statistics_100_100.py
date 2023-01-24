lines = int(input())
list_positives = list()
list_negatives = list()

for l in range(lines):
    num = int(input())
    if num < 0:
        list_negatives.append(num)
    else:
        list_positives.append(num)

print(f'{list_positives}\n{list_negatives}\nCount of positives: {len(list_positives)}. '
      f'Sum of negatives: {sum(list_negatives)}')
