import re
import math
from collections import defaultdict


def parse_reactions(text):
    """Converts reactions text to reactions dictionary"""
    reactions = {}
    for line in text.split("\n"):
        reaction_list = re.findall(r'(\d+) (\w+)', line)
        qty_produced, product = reaction_list.pop()
        ingredients = [(int(qty_required), ingredient)
                       for qty_required, ingredient in reaction_list]
        reactions[product] = (int(qty_produced), ingredients)
    return reactions


def ore_required_stock(reactions, qty):
    """Calculates the ore required to make a certain qty of FUEL"""
    ore_required = 0
    needs = defaultdict(int, {'FUEL': qty})
    stock = defaultdict(int)

    def get_from_stock(qty, chemical):
        in_stock = stock[chemical]
        qty -= in_stock
        stock[chemical] = abs(qty) if qty < 0 else 0
        return in_stock - stock[chemical]

    iterations = 0
    while needs:
        iterations += 1
        chemical, qty_required = needs.popitem()
        from_store = get_from_stock(qty_required, chemical)
        qty_required -= from_store
        qty_produced, ingredients = reactions[chemical]
        n = math.ceil(qty_required/qty_produced)
        stock[chemical] = qty_produced*n - qty_required
        for qty_ingredient, ingredient in ingredients:
            if ingredient == 'ORE':
                ore_required += qty_ingredient*n
            else:
                needs[ingredient] += qty_ingredient*n
    return (ore_required, iterations)


def topological_order(reactions):
    """Returns the topological order of each chemical in the reaction"""
    visited_nodes = []
    order = []

    def dfs(reactions, node):
        visited_nodes.append(node)
        if node == 'ORE':
            return
        _, ingredients = reactions[node]
        for _, ingredient in ingredients:
            if ingredient not in visited_nodes:
                dfs(reactions, ingredient)
        order.append(node)

    dfs(reactions, 'FUEL')
    order.reverse()
    order.append('ORE')
    ordering = {element: index for index, element in enumerate(order)}
    return ordering


def ore_required_topological(reactions, ordering, qty):
    """Calculates the ore required to make a certain qty of FUEL by using topological ordering"""
    ore_required = 0
    needs = defaultdict(int, {'FUEL': qty})
    iterations = 0
    while needs:
        iterations += 1
        chemical = sorted(needs.keys(), key=lambda k: ordering[k])[0]
        qty_required = needs.pop(chemical)
        qty_produced, ingredients = reactions[chemical]
        n = math.ceil(qty_required/qty_produced)
        for qty_ingredient, ingredient in ingredients:
            if ingredient == 'ORE':
                ore_required += qty_ingredient*n
            else:
                needs[ingredient] += qty_ingredient*n
    return (ore_required, iterations)


def estimate_fuel_produced(reactions, ore_qty):
    """Returns under and over estimations for FUEL produced by a certain amount of ORE"""
    ordering = topological_order(reactions)
    ratio, _ = ore_required_topological(reactions, ordering, 1)
    under_estimation = ore_qty//ratio
    order = math.log10(under_estimation)
    qty = 10**order
    ore, _ = ore_required_topological(reactions, ordering, qty)
    while ore < ore_qty:
        print(qty)
        order += 1
        qty = 10**order
        ore, _ = ore_required_topological(reactions, ordering, qty)
    ratio = math.floor(ore/qty)
    over_estimation = ore_qty//ratio
    return (under_estimation,over_estimation), order
