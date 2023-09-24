import math



# returns a list [(start_at, addition)]
def getPrices(required_per_iteration, initial_amount, cost):
    result = []
    free_iterations =  initial_amount // required_per_iteration
    cost_per_turn = required_per_iteration * cost
    first_top_up_cost = required_per_iteration * cost if initial_amount == 0 else (required_per_iteration - initial_amount % required_per_iteration) * cost
    result.append((free_iterations, first_top_up_cost))
    if first_top_up_cost != cost_per_turn:
        result.append((free_iterations + 1, cost_per_turn - first_top_up_cost))
    return result


def normalize(prices_additions):
    prices_additions.sort()
    if prices_additions[0][0] != 0:
        yield (0, 0)
    index = 0
    while(True):
        if index == len(prices_additions):
            break
        c = 0
        t = prices_additions[index][0]
        while(index < len(prices_additions) and prices_additions[index][0] == t):
            c += prices_additions[index][1]
            index += 1
        yield (t, c)
    yield (math.inf, 0)

def calculateForMachine(budget: int, composition: list[int], stock: list[int], cost: list[int]):
    prices_additions = []
    for e in zip(composition, stock, cost):
        prices = getPrices(*e)
        prices_additions.extend(prices)

    normalized = list(normalize(prices_additions))

    price_per_unit = 0
    total = 0
    for i in range(1, len(normalized)):
        left = normalized[i - 1]
        right = normalized[i]
        price_per_unit = price_per_unit + left[1]
        available = right[0] - left[0]
        affordable = available if price_per_unit == 0 else budget // price_per_unit
        if not affordable:
            break
        bought = min(available, affordable)
        total += bought
        budget -= bought * price_per_unit

    return total


class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: list[list[int]], stock: list[int], cost: list[int]) -> int:
        result = 0
        for c in composition:
            this_result = calculateForMachine(budget, c, stock, cost)
            result = max(result, this_result)
        return result
