class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        moves = {'G': (0, 1), 'L': (-1, 0), 'R': (0, 1)}
        initial = (0,0)

        for i in instructions:
            if i == moves.keys():
                initial.append()