UP = 1
LEVEL = 0
DOWN = -1

class Solution:
    def candy(self, ratings) -> int:
        previous_direction = LEVEL
        total = 1
        previous_top_value = 1
        previous_value = 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                this_direction = UP
            elif ratings[i] < ratings[i-1]:
                this_direction = DOWN
            else:
                this_direction = LEVEL
            if this_direction == UP:
                if previous_direction == UP:
                    this_value = previous_value + 1
                else:
                    this_value = 2
                previous_top_value = this_value
            elif this_direction == DOWN:
                if previous_direction == DOWN:
                    this_value = previous_value + 1 # NOt exactly true but good enough
                else:
                    this_value = 1
                if (previous_top_value == this_value):
                    previous_top_value += 1
                    total += 1
            else:
                this_value = 1
                previous_top_value = 1
            total += this_value
            previous_value = this_value
            previous_direction = this_direction
        return total
