import math


# Agent Class defines current state, reward and function checkEndState
class Agent:
    def __init__(self, x, v, w, w0, t):
        self.reward = [1, 1]  # reward is 1 for both action Left and Right
        self.x = x
        self.v = v
        self.w = w
        self.w0 = w0
        self.t = t

    # Checking EndState
    def checkEndState(self):
        if self.x <= -2.4 or self.x >= 2.4:
            return True
        leftBound = math.radians(-12)
        rightBound = math.radians(12)
        if self.w <= leftBound or self.w >= rightBound:
            return True
        if self.t >= 500:
            return True
        return False
