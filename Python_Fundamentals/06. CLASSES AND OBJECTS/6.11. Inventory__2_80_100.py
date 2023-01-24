class Inventory:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.counter = 0
        self.items = []

    def add_item(self, item):
        if self.__capacity > self.counter:
            self.items.append(item)
            self.counter += 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return f"{self.__capacity}"

    def __str__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity - self.counter}"
