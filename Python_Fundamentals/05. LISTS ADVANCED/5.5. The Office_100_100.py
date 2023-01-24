employees_list = [int(x) for x in input().split()]
increasing_factor = int(input())
employees_list = list(map(lambda x: x * increasing_factor, employees_list))
filtered_emp_list = list(filter(lambda x: x >= sum(employees_list) / len(employees_list), employees_list))

if len(filtered_emp_list) >= len(employees_list) / 2:
    print(f"Score: {len(filtered_emp_list)}/{len(employees_list)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_emp_list)}/{len(employees_list)}. Employees are not happy!")
