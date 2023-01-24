from collections import deque


def list_manipulator(seq, command, position, *args):

    new_list = []
    if command == "remove":
        if position == "beginning" and not args:
            seq.pop(0)
            new_list = seq
        elif position == "end" and not args:
            seq.pop()
            new_list = seq
        elif position == "beginning" and len(args) == 1:
            for _ in range(int(args[0])):
                seq.pop(0)
            new_list = seq
        elif position == "end" and len(args) == 1:
            for _ in range(int(args[0])):
                seq.pop()
            new_list = seq

    elif command == "add":
        seq = deque(seq)
        if position == "beginning":
            seq.extendleft(args[::-1])
            new_list = list(seq)
        elif position == "end":
            seq.extend(args)
            new_list = list(seq)

    return new_list
