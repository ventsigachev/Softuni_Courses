def permute(string, pocket=''):
    if len(string) == 0:
        permutations.append(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0: i]
            back = string[i + 1:]
            together = front + back
            permute(together, letter + pocket)
    return permutations


def result(s):
    permute(s)
    print(permutations)


if __name__ == "__main__":
    permutations = []
    result(input("Please, enter your string here:"))

