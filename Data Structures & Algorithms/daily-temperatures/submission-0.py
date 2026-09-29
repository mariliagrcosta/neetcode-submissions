class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        wait_days = [0] * len(temperatures)
        pending_indices = []

        for day, temperature in enumerate(temperatures):
            while (
                pending_indices
                and temperatures[pending_indices[-1]] < temperature
            ):
                pending_day = pending_indices.pop()
                wait_days[pending_day] = day - pending_day

            pending_indices.append(day)

        return wait_days
