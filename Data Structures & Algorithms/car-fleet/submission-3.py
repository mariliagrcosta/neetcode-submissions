class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arrival_times = {}

        for car_position, car_speed in zip(position, speed):
            arrival_times[car_position] = (target - car_position) / car_speed

        leading_fleet_time = 0.0
        fleet_count = 0

        for road_position in range(target - 1, -1, -1):
            arrival_time = arrival_times.get(road_position, 0.0)

            # Empty positions default to 0.0, never raising the running maximum
            if arrival_time > leading_fleet_time:
                leading_fleet_time = arrival_time
                fleet_count += 1

        return fleet_count
