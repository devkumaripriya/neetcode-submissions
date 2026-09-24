from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            destroyed = False

            while stack and stack[-1] > 0 and asteroid < 0:

                if stack[-1] < -asteroid:
                    # Stack asteroid is smaller
                    stack.pop()

                elif stack[-1] == -asteroid:
                    # Both explode
                    stack.pop()
                    destroyed = True
                    break

                else:
                    # Current asteroid is smaller
                    destroyed = True
                    break

            if not destroyed:
                stack.append(asteroid)

        return stack