num_1 = int(input())
num_2 = int(input())
result = ''
result += f'Before:\na = {num_1}\nb = {num_2}\n'
temp = num_1
num_1 = num_2
num_2 = temp
result += f'After:\na = {num_1}\nb = {num_2}'
print(result)
