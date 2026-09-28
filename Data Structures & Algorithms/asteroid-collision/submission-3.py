class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Reuses the input array as the stack - stack_size marks its end
        stack_size = 0

        for asteroid in asteroids:
            while (
                asteroid < 0
                and stack_size > 0
                and asteroids[stack_size - 1] > 0
            ):
                top_asteroid = asteroids[stack_size - 1]

                if top_asteroid < -asteroid:
                    stack_size -= 1
                elif top_asteroid == -asteroid:
                    stack_size -= 1
                    break
                else:
                    break
            else:
                # Executes only if the while loop ends without hitting "break"
                asteroids[stack_size] = asteroid
                stack_size += 1

        return asteroids[:stack_size]
