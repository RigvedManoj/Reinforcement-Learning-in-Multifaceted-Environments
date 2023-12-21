class State:
    def __init__(self, state, actionCount):
        self.transition = [None] * actionCount
        self.reward = 0
        self.actionCount = actionCount
        self.action = None
        self.value = 0
        self.state = state

    # left(0),up(1),down(2),right(3) (policies are deterministic)
    def setAction(self, action):
        self.action = action

    # State value is defined here
    def setValue(self, value):
        self.value = value

    def setTransition(self, actions, stateProbLists):
        for action in actions:
            self.transition[action] = stateProbLists[action]

    # Setting reward for given state.
    def setReward(self, reward):
        self.reward = reward

    # [left,up,down,right,same] -> [0,1,2,3,4]
    def getNextState(self, move):
        newX = self.state[0]
        newY = self.state[1]

        if move == 0:  # Left Logic
            newY = self.state[1] - 1
        elif move == 1:  # Up Logic
            newX = self.state[0] - 1
        elif move == 2:  # Down Logic
            newX = self.state[0] + 1
        elif move == 3:  # Right Logic
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
