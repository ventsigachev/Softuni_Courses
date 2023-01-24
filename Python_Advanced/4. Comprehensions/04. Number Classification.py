int_numbers = [int(x) for x in input().split(", ")]
print(f"Positive: {', '.join([str(p) for p in int_numbers if p >= 0])}")
print(f"Negative: {', '.join([str(n) for n in int_numbers if n < 0])}")
print(f"Even: {', '.join([str(e) for e in int_numbers if e % 2 == 0])}")
print(f"Odd: {', '.join([str(o) for o in int_numbers if o % 2 == 1])}")
