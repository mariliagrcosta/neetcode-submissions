class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Uses 0 as a sentinel value to represent a destroyed asteroid.
        # Only valid because problem constraints guarantee asteroids[i] != 0.
        surviving_asteroids = []

        for asteroid in asteroids:
            while (
                asteroid < 0
                and surviving_asteroids
                and surviving_asteroids[-1] > 0
            ):
                top_asteroid = surviving_asteroids[-1]

                if top_asteroid < -asteroid:
                    surviving_asteroids.pop()
                elif top_asteroid == -asteroid:
                    surviving_asteroids.pop()
                    asteroid = 0  # Sentinel: both asteroids explode
                    break
                else:
                    asteroid = 0  # Sentinel: incoming asteroid explodes
                    break

            if asteroid != 0:
                surviving_asteroids.append(asteroid)

        return surviving_asteroids
