from typing import List
class Solution:
    def asteroidCollision(self,asteroids:List[int])->List[int]:
        stack=[]
        for asteroid in asteroids:
            destroyed=False

            while stack and stack[-1] >0 and asteroid <0:
                if stack[-1] < -asteroid:
                    #stack asteroid is smaller
                     stack.pop()
                elif stack[-1]==-asteroid:
                    #both explode
                      stack.pop()
                      destroyed=True
                      break

                else:
                    #Current asteroids is smaller:
                     destroyed =True
                     break
            if not destroyed:
                stack.append(asteroid)
        return stack
                  
