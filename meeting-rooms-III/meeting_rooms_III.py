import heapq

class Solution:
    def mostBooked(self, n: int, meetings) -> int:
        # Available rooms
        available_rooms = list(range(n))
        # Booked rooms, ordered by next availability
        booked_rooms = []

        room_counts = [0]*n

        meetings.sort()
        current_time = 0
        for start,end in meetings:
            current_time = start
            meeting_length = end-start
            while booked_rooms and booked_rooms[0][0] <= current_time:
                freed_room = heapq.heappop(booked_rooms)[1]
                heapq.heappush(available_rooms, freed_room)
            if available_rooms:
                room_num = heapq.heappop(available_rooms)
                room_counts[room_num] += 1
                heapq.heappush(booked_rooms, (end, room_num))
            else:
                current_time, freed_room = heapq.heappop(booked_rooms)
                room_counts[freed_room] += 1
                heapq.heappush(booked_rooms, (current_time + meeting_length, freed_room))

        max_index = -1
        max_length = -1
        for i,v in enumerate(room_counts):
            if v > max_length:
                max_length = v
                max_index = i
        return max_index
