numbers = [int(x) for x in input().split()]
negative_list, positive_list = [], []
[negative_list.append(y) if y < 0 else positive_list.append(y) for y in numbers]
print(sum(negative_list))
print(sum(positive_list))

if abs(sum(negative_list)) > sum(positive_list):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
