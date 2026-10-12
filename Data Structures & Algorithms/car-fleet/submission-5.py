class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_cars = sorted(zip(position, speed))
        fleet_times = []

        for car_position, car_speed in sorted_cars:
            arrival_time = (target - car_position) / car_speed

            # Merge fleets behind that can catch up to the current car
            while fleet_times and arrival_time >= fleet_times[-1]:
                fleet_times.pop()

            fleet_times.append(arrival_time)

        return len(fleet_times)
