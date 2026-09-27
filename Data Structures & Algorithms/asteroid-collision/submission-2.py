class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
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
                    break
                else:
                    break
            else:
                # Executes ONLY if the while loop ends without hitting "break"
                surviving_asteroids.append(asteroid)

        return surviving_asteroids
