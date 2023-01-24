def age_assignment(*args, **kwargs):
    final_dict = {arg: kwargs[arg[0]] for arg in args}
    return final_dict


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
