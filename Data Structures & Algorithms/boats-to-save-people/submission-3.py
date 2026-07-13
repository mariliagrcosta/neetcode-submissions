from sortedcontainers import SortedList

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        weights = SortedList(people)
        boats = 0

        while weights:
            heaviest = weights.pop()

            # weights[0] is always the lightest remaining weight
            if weights and weights[0] + heaviest <= limit:
                weights.pop(0)

            boats += 1

        return boats
