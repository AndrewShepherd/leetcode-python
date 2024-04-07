from collections import defaultdict;

class Solution:
    def mostFrequentIDs(self, nums: list[int], freq: list[int]) -> list[int]:
        frequencies = defaultdict(int)
        heap_index_lookup = dict()
        heap = []
        result = []

        def update_lookup(i):
            heap_index_lookup[heap[i]] = i

        def swap(i1, i2):
            heap[i1],heap[i2] = heap[i2],heap[i1]
            update_lookup(i1)
            update_lookup(i2)

        def heap_check_down(index):

            cLeft, cRight = index*2+1, index*2+2

            if cLeft < len(heap):
                n = heap[index]
                this_value = frequencies[n]
                nLeft = heap[cLeft]
                left_value = frequencies[nLeft]
                if left_value > this_value:
                    swap(index, cLeft)
                    heap_check_down(cLeft)
            if cRight < len(heap):
                n = heap[index]
                this_value = frequencies[n]
                nRight = heap[cRight]
                right_value = frequencies[nRight]
                if right_value > this_value:
                    swap(index, cRight)
                    heap_check_down(cRight)


        def heap_check_up(index):
            if index == 0:
                return False
            this_value = frequencies[heap[index]]
            upper_index = (index-1)//2
            upper_value = frequencies[heap[upper_index]]
            if upper_value < this_value:
                swap(index, upper_index)
                heap_check_up(upper_index)
                return True
            else:
                return False

        def heap_add(n):
            heap.append(n)
            index = len(heap)-1
            heap_index_lookup[n] = index
            heap_check_up(index)

        def heap_check(n):
            index = heap_index_lookup[n]
            if not heap_check_up(index):
                heap_check_down(index)
        
        for n,f in zip(nums,freq):
            frequencies[n] += f
            if n in heap_index_lookup:
                heap_check(n)
            else:
                heap_add(n)
            result.append(frequencies[heap[0]])


        return result
