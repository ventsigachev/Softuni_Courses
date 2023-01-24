all_roads = []

while True:
    data = input().split("->")
    if data[0] == "END":
        break
    elif data[0] == "Add":
        trace_in_all_roads = False
        for trace in all_roads:
            if trace[0] == data[1]:
                trace_in_all_roads = True
                trace += [data[2]]
                break
        if not trace_in_all_roads:
            all_roads += [[data[1], data[2]]]
    elif data[0] == "Move":
        for trace in all_roads:
            if trace[0] == data[1]:
                if data[2] in trace:
                    trace.remove(data[2])
                    for trace_2 in all_roads:
                        if trace_2[0] == data[3]:
                            trace_2 += [data[2]]
    elif data[0] == "Close":
        for trace in all_roads:
            if trace[0] == data[1]:
                all_roads.remove(trace)

all_roads = sorted(sorted(all_roads, key=lambda x: x[0]), key=lambda x: len(x), reverse=True)

print("Practice sessions:")
for road in all_roads:
    print(road[0])
    for driver in road[1:]:
        print(f"++{driver}")
