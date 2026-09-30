class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        day_count = len(temperatures)
        wait_days = [0] * day_count

        for day in range(day_count - 2, -1, -1):
            future_day = day + 1

            while (
                future_day < day_count
                and temperatures[day] >= temperatures[future_day]
            ):
                # If future_day never found a warmer day, neither will day.
                # Mark it out of bounds to stop and keep wait_days[day] as 0.
                if wait_days[future_day] == 0:
                    future_day = day_count
                    break

                future_day += wait_days[future_day]

            if future_day < day_count:
                wait_days[day] = future_day - day

        return wait_days
