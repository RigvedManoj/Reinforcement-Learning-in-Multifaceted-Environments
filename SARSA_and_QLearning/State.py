import numpy


class State:
    def __init__(self, state, actionCount):
        self.state = state
        self.actionCount = actionCount
        self.action = None
        self.actionProbabilities = [0.25, 0.25, 0.25, 0.25]
        self.transition = [None] * actionCount
        self.move = None
        self.value = 0
        self.oldValue = 0
        self.qValue = [10, 10, 10, 10]
        self.reward = 0

    # left(0),up(1),down(2),right(3) (policies are stochastic)
    def takeAction(self):
        self.action = numpy.random.choice(numpy.arange(0, 4), p=self.actionProbabilities)

    def setActionProbabilities(self, epsilon):
        maxQ = max(self.qValue)
        optimalAction = 0
        for action in range(0, 4):
            if self.qValue[action] == maxQ:
                optimalAction += 1
        for action in range(0, 4):
            if self.qValue[action] == maxQ:
                self.actionProbabilities[action] = (1-epsilon)/optimalAction + epsilon/4
            else:
                self.actionProbabilities[action] = epsilon/4

    # left(0),up(1),down(2),right(3) (policies are stochastic)
    def setAction(self, action):
        self.action = action

    # State value is defined here
    def setValue(self, value):
        self.value = value

    def setTransition(self, actions, stateProbLists):
        for action in actions:
            self.transition[action] = stateProbLists[action]

    def setMove(self):
        self.move = numpy.random.choice(numpy.arange(0, 5), p=self.transition[self.action])

    # Setting reward for given state.
    def setReward(self, reward):
        self.reward = reward

    # [left,up,down,right,same] -> [0,1,2,3,4]
    def getNextState(self):
        newX = self.state[0]
        newY = self.state[1]

        if self.move == 0:  # Left Logic
            newY = self.state[1] - 1
        elif self.move == 1:  # Up Logic
            newX = self.state[0] - 1
        elif self.move == 2:  # Down Logic
            newX = self.state[0] + 1
        elif self.move == 3:  # Right Logic
            newY = self.state[1] + 1

        # Check if position goes outside grid
        if newX < 0 or newX > 4:
            newX = self.state[0]
        if newY < 0 or newY > 4:
            newY = self.state[1]

        # Check Obstacle Space
        if newX == 2 and newY == 2:
            newX = self.state[0]
            newY = self.state[1]
        if newX == 3 and newY == 2:
            newX = self.state[0]
            newY = self.state[1]

        return [newX, newY]

    # Checking EndState by checking number of Actions.
    def checkEndState(self):
        if self.actionCount == 0:
            return True
        else:
            return False
