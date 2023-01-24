stack = [int(x) for x in input().split()]
rev_stack = stack[::-1]
print(" ".join(str(x) for x in rev_stack))
