class TreeNode:
    def __init__(self, id, present_price, future_price):
        self.id = id
        self.present_price = present_price
        self.future_price = future_price
        self.children = []

    def add(self, child):
        self.children.append(child)

def calculate(node, budget):
    if not node.children:
        this_profit_no_discount = max(node.future_price - node.present_price, 0)
        this_profit_discount = max(node.future_price - node.present_price//2, 0)
        return (
            [0] * min(node.present_price//2, budget+1) + [this_profit_discount] * max(0, budget+1 - node.present_price//2),
            [0] * min(node.present_price, budget+1) + [this_profit_no_discount] * max(0, budget+1 - node.present_price)
        )
    (child_with_discount, child_with_no_discount) = calculate(node.children[0], budget)
    for child_node in node.children[1:]:
        c_discount, d_no_discount = calculate(child_node, budget)
        d2 = [0] * (budget+1)
        nd2 = [0] * (budget+1)
        for budget_available in range(0, budget+1):
            for budget_for_this_child in range(0, budget_available+1):
                result_no_discount = d_no_discount[budget_for_this_child] + child_with_no_discount[budget_available - budget_for_this_child]
                result_discount = c_discount[budget_for_this_child] + child_with_discount[budget_available - budget_for_this_child]
                d2[budget_available] = max(d2[budget_available], result_discount)
                nd2[budget_available] = max(nd2[budget_available], result_no_discount)
        child_with_discount = d2
        child_with_no_discount = nd2  

    final_dp_with_no_discount = []
    final_dp_with_discount = []
    
    this_profit_no_discount = node.future_price - node.present_price
    this_profit_discount = node.future_price - node.present_price//2
    for i in range(0, budget+1):
        if node.present_price <= i:
            if_I_buy = this_profit_no_discount + child_with_discount[i - node.present_price]
            if_I_dont = child_with_no_discount[i]
            final_dp_with_no_discount.append(max(if_I_buy, if_I_dont))
        else:
            final_dp_with_no_discount.append(child_with_no_discount[i])
        if node.present_price // 2 <= i:
            if_I_buy = this_profit_discount + child_with_discount[i - node.present_price//2]
            if_I_dont = child_with_no_discount[i]
            final_dp_with_discount.append(max(if_I_buy, if_I_dont))
        else:
            final_dp_with_discount.append(child_with_no_discount[i])
    return (final_dp_with_discount, final_dp_with_no_discount)

    

class Solution:
    def maxProfit(
        self, 
        n: int,
        present: list[int],
        future: list[int],
        hierarchy: list[list[int]],
        budget: int
    ) -> int:
        nodes = [TreeNode(i+1, present[i], future[i]) for i in range(0, n)]
        for p,c in hierarchy:
            nodes[p-1].add(nodes[c-1])
        dp_with_discount, dp_with_no_discount = calculate(nodes[0], budget)
        return max(dp_with_no_discount[-1], 0)
