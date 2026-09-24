class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for asteroid in asteroids:
            destoryed = False
            # collision happens when :
            #stack open is moving right(+)
            #current asteroid is moving left(-)
            while stack and stack[-1]>0 and  asteroid < 0:

                if stack[-1] < -asteroid:
                    #stack asteroid is similar
                    stack.pop()
                elif stack[-1] == -asteroid:
                    stack.pop()
                    destroyed=True
                    break
                else:
                    #Current asteroid is smaller
                    destroyed =True

                    break
        return stack 

        