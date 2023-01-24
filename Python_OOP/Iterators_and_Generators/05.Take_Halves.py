def solution():
    def integers():
        num = 1
        while 1:
            yield num
            num += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        list_nums = []
        [list_nums.append(next(seq)) for _ in range(n)]
        return list_nums

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
