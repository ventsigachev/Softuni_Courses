class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        f_l_list = [pr for pr in self.products if pr[0] == first_letter]
        return f_l_list

    def __str__(self):
        result = ''
        result_list = [x for x in sorted(self.products)]
        result += f"Items in the {self.name} catalogue:\n"
        result += f"\n".join(result_list)
        return result
