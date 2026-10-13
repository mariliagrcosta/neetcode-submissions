class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_cars = sorted(zip(position, speed), reverse=True)
        leading_distance = 0
        leading_speed = 1  # Positive sentinel ensures the first car is counted
        fleet_count = 0

        for car_position, car_speed in sorted_cars:
            car_distance = target - car_position

            # Cross-multiplied form of: car arrival time > leading fleet arrival time
            if car_distance * leading_speed > leading_distance * car_speed:
                leading_distance = car_distance
                leading_speed = car_speed
                fleet_count += 1

        return fleet_count
