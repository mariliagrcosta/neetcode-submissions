class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arrival_times = {}

        for car_position, car_speed in zip(position, speed):
            arrival_times[car_position] = (target - car_position) / car_speed

        leading_fleet_time = 0.0
        fleet_count = 0

        # Visit car positions from closest to the target to farthest
        for car_position in sorted(arrival_times, reverse=True):
            arrival_time = arrival_times[car_position]

            # A strictly greater arrival time signals a new fleet leader
            if arrival_time > leading_fleet_time:
                leading_fleet_time = arrival_time
                fleet_count += 1

        return fleet_count
