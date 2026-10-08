class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_cars = sorted(zip(position, speed), reverse=True)
        leading_fleet_time = 0.0
        fleet_count = 0

        for car_position, car_speed in sorted_cars:
            arrival_time = (target - car_position) / car_speed

            if arrival_time > leading_fleet_time:
                leading_fleet_time = arrival_time
                fleet_count += 1

        return fleet_count
