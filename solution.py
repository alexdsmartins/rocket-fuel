import math
import sys
from day14.ore import (parse_reactions, ore_required_stock, topological_order,
                       ore_required_topological, estimate_fuel_produced)
from day14.finders import bisect, secant


example = """5 ORE => 7 A
3 A => 10 B
1 A, 3 B => 1 C
5 C, 2 B => 1 FUEL"""

if __name__ == "__main__":
    print("Day 14")
    if len(sys.argv) == 2:
        try:
            text = open(sys.argv[1]).read().strip()
        except:
            text = example
    else:
        text = example

    reactions = parse_reactions(text)

    print("\nPART I - ORE required to produce 1 FUEL")

    print("\nStock method:")
    ore_used, i = ore_required_stock(reactions, 1)
    print(f"ORE used to produce one FUEL: {ore_used}; Took {i} iterations.")

    print("\nTopological ordering method:")
    ordering = topological_order(reactions)
    ore_used, i = ore_required_topological(reactions, ordering, 1)
    print(f"ORE used to produce one FUEL: {ore_used}; Took {i} iterations.")

    print("\nPART II - FUEL produced with 1 trillion ORE")
    TRILLION = int(1E12)
    estimations, order = estimate_fuel_produced(reactions, TRILLION)
    print(f"Estimated between {estimations[0]} and {estimations[1]} FUEL.")

    print("\nBisect method:")
    def f(x, reactions, ordering):
        ore, _ = ore_required_topological(reactions, ordering, x)
        return ore
    ordering = topological_order(reactions)
    args = (reactions, ordering)
    result, i = bisect(f, TRILLION, estimations, args)
    print(f"1 trillion ORE can produce: {result} FUEL; Took {i} iterations.")

    print("\nSecant method:")
    result, i = secant(f, TRILLION, estimations, args)
    print(f"1 trillion ORE can produce: {result} FUEL; Took {i} iterations.")
