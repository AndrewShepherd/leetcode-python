class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = x
        readBit = 1
        writeBit = 1
        while(writeBit & x):
            writeBit <<= 1
        while(readBit <= (n-1)):
            if (readBit & (n-1)):
                result |= writeBit
            writeBit <<= 1
            while(writeBit & x):
                writeBit <<= 1           
            readBit <<= 1
        return result
