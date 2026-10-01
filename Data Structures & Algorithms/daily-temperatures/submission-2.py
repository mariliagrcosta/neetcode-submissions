class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        day_count = len(temperatures)
        wait_days = [0] * day_count
        pending_pairs = []  # Stores (temperature, day)

        for day, temperature in enumerate(temperatures):
            while pending_pairs and temperature > pending_pairs[-1][0]:
                _, pending_day = pending_pairs.pop()
                wait_days[pending_day] = day - pending_day

            pending_pairs.append((temperature, day))

        return wait_days
