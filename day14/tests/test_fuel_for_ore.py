import pytest
from day14.ore import parse_reactions, topological_order, ore_required_topological, ore_required_stock
from day14.finders import bisect, secant
from .test_data import data


fuel_for_ore_examples = [
    (e['reactions'], int(e['fuel_per_1T_ore'])) for e in data if e.get('fuel_per_1T_ore', 0)]


def ids(examples):
    ids = []
    for example in examples:
        text, _fuel_per_1T_ore = example
        id = f"reaction_len:{len(text.splitlines())}_starts:{text[:20]}"
        ids.append(id)
    return ids


@ pytest.mark.parametrize("text,expected", fuel_for_ore_examples, ids=ids(fuel_for_ore_examples))
def test_fuel_for_ore_stock_bisect(text, expected):
    reactions = parse_reactions(text)

    def f(x, reactions):
        ore, _ = ore_required_stock(reactions, x)
        return ore

    target = int(1E12)
    interval = (1, int(1E10))
    args = (reactions,)
    result, _ = bisect(f, target, interval, args)
    assert result == expected


@ pytest.mark.parametrize("text,expected", fuel_for_ore_examples, ids=ids(fuel_for_ore_examples))
def test_fuel_for_ore_topological_bisect(text, expected):
    reactions = parse_reactions(text)
    ordering = topological_order(reactions)

    def f(x, reactions, ordering):
        ore, _ = ore_required_topological(reactions, ordering, x)
        return ore

    target = int(1E12)
    interval = (1, int(1E10))
    args = (reactions, ordering)
    result, _ = bisect(f, target, interval, args)
    assert result == expected


@ pytest.mark.parametrize("text,expected", fuel_for_ore_examples, ids=ids(fuel_for_ore_examples))
def test_fuel_for_ore_stock_secant(text, expected):
    reactions = parse_reactions(text)

    def f(x, reactions):
        ore, _ = ore_required_stock(reactions, x)
        return ore

    target = int(1E12)
    interval = (1, int(1E10))
    args = (reactions,)
    result, _ = secant(f, target, interval, args)
    assert result == expected


@ pytest.mark.parametrize("text,expected", fuel_for_ore_examples, ids=ids(fuel_for_ore_examples))
def test_fuel_for_ore_topological_secant(text, expected):
    reactions = parse_reactions(text)
    ordering = topological_order(reactions)

    def f(x, reactions, ordering):
        ore, _ = ore_required_topological(reactions, ordering, x)
        return ore

    target = int(1E12)
    interval = (1, int(1E10))
    args = (reactions, ordering)
    result, _ = bisect(f, target, interval, args)
    assert result == expected
