class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        values_and_indexes = sorted([(n,i) for i,n in enumerate(nums)])
        result = [None] * len(nums)

        this_value_batch = None
        this_index_batch = None
        for v,i in values_and_indexes:
            if (this_value_batch == None):
                this_value_batch = [v]
                this_index_batch = [i]
            elif (v - this_value_batch[-1] <= limit):
                this_value_batch.append(v)
                this_index_batch.append(i)
            else:
                this_index_batch.sort()
                for v2,i2 in zip(this_value_batch, this_index_batch):
                    result[i2] = v2
                this_value_batch = [v]
                this_index_batch = [i]
        if this_value_batch != None:
            this_index_batch.sort()
            for v2,i2 in zip(this_value_batch, this_index_batch):
                result[i2] = v2
        return result
