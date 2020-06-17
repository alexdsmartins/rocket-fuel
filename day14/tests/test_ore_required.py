import pytest
from day14.ore import parse_reactions, ore_required_stock, topological_order, ore_required_topological
from day14.tests.test_data import data


ore_required_examples = [
    (e['reactions'], int(e['ore_per_1_fuel'])) for e in data]


def ids(examples):
    ids = []
    for example in examples:
        text, ore_per_1_fuel = example
        id = f"reaction_len:{len(text.splitlines())}_expected:{ore_per_1_fuel}_starts:{text[:30]}"
        ids.append(id)
    return ids


@ pytest.mark.parametrize("text,expected", ore_required_examples, ids=ids(ore_required_examples))
def test_ore_required_stock(text, expected):
    reactions = parse_reactions(text)
    ore, _ = ore_required_stock(reactions, 1)
    assert ore == expected


@ pytest.mark.parametrize("text,expected", ore_required_examples, ids=ids(ore_required_examples))
def test_ore_required_topological(text, expected):
    reactions = parse_reactions(text)
    ordering = topological_order(reactions)
    ore, _ = ore_required_topological(reactions, ordering, 1)
    assert ore == expected
