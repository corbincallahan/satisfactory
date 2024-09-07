# TODO Alt recipes?

import sys

recipes = {}

with open("./recipes.csv", "r") as fh:
    for line in [line.rstrip(",\n ").split(",") for line in fh]:
        key, full_name, amount = line[:3]
        components = line[3:]
        if key in recipes:
            print(f"Duplicate key {key}, exiting")
            exit()
        recipe = {components[i]: int(components[i + 1]) for i in range(0, len(components), 2)}
        recipes[key] = (full_name, int(amount), recipe)

totals = {}

class Recipe:
    key = ""
    full_name = ""
    quantity = 0
    components = {}

    def __init__(self, key, full_name, quantity, components):
        self.key = key
        self.full_name = full_name
        self.quantity = quantity
        self.components = components

    def print_components(self, amount, indent):
        indent_str = "\t" * indent
        print(f"{indent_str}{round(amount, 4)} {self.full_name}")
        if self.components:
            ratio = amount / self.quantity
            for key in self.components:
                if key in rb:
                    amount_needed = self.components[key]
                    rb[key].print_components(round(amount_needed * ratio, 8), indent + 1)
        else:
            if self.key not in totals:
                totals[self.key] = 0
            totals[self.key] += amount

def make_recipe_book():
    rb = {}
    for key in recipes:
        full_name, quantity, components = recipes[key]
        rb[key] = Recipe(key, full_name, quantity, components)
    return rb

rb = make_recipe_book()

def main():
    for i in range((len(sys.argv) - 1) // 2):
        goal_quantity = float(sys.argv[i * 2 + 1])
        goal_item = sys.argv[i * 2 + 2]
        rb[goal_item].print_components(goal_quantity, 0)
    for key in totals:
        print(f"{round(totals[key], 4)} {rb[key].full_name}")

if __name__ == "__main__":
    main()