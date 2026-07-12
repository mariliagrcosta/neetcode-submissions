class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        weight_counts = [0] * (limit + 1)

        for weight in people:
            weight_counts[weight] += 1

        lightest_weight = 1
        heaviest_weight = limit
        boats = 0

        while lightest_weight <= heaviest_weight:
            while lightest_weight <= heaviest_weight and weight_counts[lightest_weight] <= 0:
                lightest_weight += 1

            while lightest_weight <= heaviest_weight and weight_counts[heaviest_weight] <= 0:
                heaviest_weight -= 1

            if lightest_weight > heaviest_weight:
                break
            
            boats += 1

            if lightest_weight + heaviest_weight <= limit:
                weight_counts[lightest_weight] -= 1
                if lightest_weight != heaviest_weight:
                    weight_counts[heaviest_weight] -= 1
                elif weight_counts[heaviest_weight] > 0:
                    weight_counts[heaviest_weight] -= 1
            else:
                weight_counts[heaviest_weight] -= 1

        return boats
