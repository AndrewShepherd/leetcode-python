def parsePrice(w):
    if len(w) < 2:
        return None
    if w[0] != '$':
        return None
    try:
        return int(w[1:])
    except:
        return None

def transform(w, discount):
    price = parsePrice(w)
    if price == None:
        return w
    amountNoDecimals = price * (100-discount)
    
    dollars = amountNoDecimals//100
    cents = amountNoDecimals%100
    return "${dollars}.{cents:02}".format(dollars = dollars, cents = cents) 



class Solution(object):
    def discountPrices(self, sentence, discount):
        """
        :type sentence: str
        :type discount: int
        :rtype: str
        """
        return " ".join([
            transform(w, discount) for w in sentence.split(" ")
        ])