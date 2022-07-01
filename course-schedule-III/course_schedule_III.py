import math

class Course:
    def __init__(self, max_location, length):
        self.max_location = max_location
        self.length = length

class Placement:
    def __init__(self, course, location):
        self.course = course
        self.location = location

    @property
    def space_remaining(self):
        return self.location - self.course.length

class PlacementNode:
    def __init__(self, index, placement, best_index_to_remove, remaining_after_removal):
        self.index = index
        self.placement = placement
        self.best_index_to_remove = best_index_to_remove
        self.remaining_after_removal = remaining_after_removal


def place(previous, course):
    location = min(course.max_location, previous.placement.space_remaining)
    placement = Placement(course, location)
    alternative_placement = Placement(course, min(course.max_location, previous.remaining_after_removal))
    index = previous.index + 1
    if alternative_placement.space_remaining > previous.placement.space_remaining:
        best_index_to_remove = previous.best_index_to_remove
        remaining_after_removal = alternative_placement.space_remaining
    else:
        best_index_to_remove = index
        remaining_after_removal = previous.placement.space_remaining
    return PlacementNode(index, placement, best_index_to_remove, remaining_after_removal)

class Solution:
    def scheduleCourse(self, courses) -> int:
        courses.sort(key = lambda e: (0-e[1], e[0]))
        
        count = 0
        placements = [PlacementNode(0, Placement(Course(math.inf, 0), math.inf), -1, 0-math.inf)]
        for course_length,course_max_location in courses:
            course = Course(course_max_location, course_length)
            last_placement = placements[-1]
            placements.append(place(last_placement, course))
            if(placements[-1].placement.space_remaining < 0):
                index_to_remove = placements[-1].best_index_to_remove
                courses_to_readd = [p.placement.course for p in placements[index_to_remove+1:]]
                placements = placements[:index_to_remove]
                for c in courses_to_readd:
                    placements.append(place(placements[-1], c))
        return len(placements) - 1

