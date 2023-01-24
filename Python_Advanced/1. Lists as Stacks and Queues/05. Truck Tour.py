from collections import deque

r = int(input())
pumps = deque()

for _ in range(r):
    pump = [int(x) for x in input().split()]
    pumps.append(pump)

for pump_number in range(r):
    current_pump = True
    fuel = 0

    for _ in range(r):
        tokens = pumps.popleft()
        current_fuel, needed_fuel = tokens[0], tokens[1]
        fuel += current_fuel - needed_fuel
        if fuel < 0:
            current_pump = False
        pumps.append(tokens)

    if current_pump:
        print(pump_number)
        break

    pumps.append(pumps.popleft())
