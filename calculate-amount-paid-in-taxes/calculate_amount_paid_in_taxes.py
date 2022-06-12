class Solution:
    def calculateTax(self, brackets, income):
        tax = 0
        lower_threshold = 0
        for upper, percent in brackets:
            portion = min(income, upper) - lower_threshold
            if (portion < 0):
                break
            tax += portion * percent / 100.0
            lower_threshold = upper
        return tax
        