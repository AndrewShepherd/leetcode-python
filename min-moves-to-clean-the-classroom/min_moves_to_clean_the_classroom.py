# state = row, column, L's remaining
import heapq
from collections import defaultdict, deque

class PositionState:
    def __init__(self, energy, flags):
        self.energy = energy
        self.flags = flags

    def __lt__(self, other):
        if self.energy > other.energy:
            return False
        elif other.energy > self.energy:
            return True
        else:
            return self.flags < other.flags

KEEP_LEFT = "KEEP_LEFT"
KEEP_RIGHT = "KEEP_RIGHT"
KEEP_BOTH = "KEEP_BOTH"
def compare_states(s1, s2):
    if s1.energy > s2.energy:
        if (s2.flags | s1.flags == s2.flags):
            return KEEP_LEFT
    elif s2.energy > s1.energy:
        if (s2.flags | s1.flags) == s1.flags:
            return KEEP_RIGHT
    elif s2.flags | s1.flags == s2.flags:
        return KEEP_LEFT
    elif s1.flags | s2.flags == s1.flags:
        return KEEP_RIGHT
    return KEEP_BOTH

def try_add(existing_states, new_state):
    indexes_to_delete = []
    for i, s in enumerate(existing_states):
        compare_result = compare_states(s, new_state)
        if compare_result == KEEP_LEFT:
            return (existing_states, False)
        elif compare_result == KEEP_RIGHT:
            indexes_to_delete.append(i)
    new_list = [None] * (len(existing_states) - len(indexes_to_delete) + 1)
    id_index = 0
    write_index = 0
    for i, v in enumerate(existing_states):
        if id_index < len(indexes_to_delete) and indexes_to_delete[id_index] == i:
            id_index += 1
        else:
            new_list[write_index] = v
            write_index += 1
    new_list[write_index] = new_state
    return new_list, True

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        l_lookup = dict()
        flag = 1
        
        for r_index, r in enumerate(classroom):
            for c_index,c in enumerate(r):
                if c == 'L':
                   l_lookup[(r_index, c_index)] = flag
                   flag <<= 1
                elif c == 'S':
                    start_pos = (r_index, c_index)
        flag >>= 1
        all_littered_spots = 0
        while(flag):
            all_littered_spots |= flag
            flag >>= 1
        if (all_littered_spots == 0):
            return 0

        initial_state = (start_pos, PositionState(energy, all_littered_spots))
        visited = defaultdict(list)
        visited[start_pos] = [initial_state[1]]
        
        pending_states = deque([(0, initial_state)])
        while(pending_states):
            (moves, state) = pending_states.popleft()
            position, position_state = state           
            r, c = position
            # Is it still in there?
            found = False
            for other in visited[position]:
                if position_state == other:
                    found = True
                    break
            if not found:
                continue
            this_energy = position_state.energy
            littered_spots = position_state.flags
            
            for v in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                new_r, new_c = (r + v[0], c + v[1])
                if not(0 <= new_r < len(classroom)) or not (0 <= new_c < len(classroom[0])):
                    continue
                marker = classroom[new_r][new_c]
                if (marker == 'X'):
                    continue
                if (marker == 'R'):
                    new_energy = energy
                else:
                    new_energy = this_energy - 1
                this_littered_spots = littered_spots

                if marker == 'L':
                    marker_flag = l_lookup[(new_r, new_c)]
                    if (marker_flag & this_littered_spots):
                        this_littered_spots -= marker_flag
                        if (this_littered_spots == 0):
                            return moves + 1
                if (new_energy == 0):
                    continue
                new_pos = (new_r, new_c)
                new_state = PositionState(new_energy, this_littered_spots)

                existing_list = visited[new_pos]
                new_list, can_add = try_add(existing_list, new_state)
                if (not can_add):
                    continue
                visited[new_pos] = new_list
                pending_states.append((moves+1, (new_pos, new_state)))
                #heapq.heappush(pending_states, (moves+1, (new_pos, new_state)))
        return -1
