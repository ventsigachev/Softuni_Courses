class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, name):
        if len(self.storage) < self.capacity:
            self.storage.append(name)

    def get_products(self):
        return self.storage
