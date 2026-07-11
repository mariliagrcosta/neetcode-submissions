class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        remaining_people = deque(people)
        boats = 0

        while remaining_people:
            heaviest = remaining_people.pop()

            if remaining_people and remaining_people[0] + heaviest <= limit:
                remaining_people.popleft()

            boats += 1

        return boats
