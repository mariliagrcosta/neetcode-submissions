from sortedcontainers import SortedList

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        weights = SortedList(people)
        boats = 0

        while weights:
            heaviest = weights.pop()            
            
            partner_idx = weights.bisect_right(limit - heaviest) - 1

            if partner_idx >= 0:
                weights.pop(partner_idx)

            boats += 1

        return boats
