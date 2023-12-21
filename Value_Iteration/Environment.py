
from State import State


# Set all states by defining policies, transitions and rewards.
def setStaticStates():
    states = []
    for i in range(0, 5):
        tempStates = []
        for j in range(0, 5):
            if i != 4 or j != 4:

                # Set Obstacles
                if (i == 2 or i == 3) and j == 2:
                    s = State([i, j], 0)
                    s.setReward(0)
                    tempStates.append(s)
                    continue

                # Set all other States
                s = State([i, j], 4)
                s.setAction(0)  # left(0),up(1),down(2),right(3) (policies are deterministic)
                transitionLeft = [0.8, 0.05, 0.05, 0, 0.1]  # left,up,down,right,same
                transitionUp = [0.05, 0.8, 0, 0.05, 0.1]  # left,up,down,right,same
                transitionDown = [0.05, 0, 0.8, 0.05, 0.1]  # left,up,down,right,same
                transitionRight = [0, 0.05, 0.05, 0.8, 0.1]  # left,up,down,right,same
                s.setTransition([0, 1, 2, 3], [transitionLeft, transitionUp, transitionDown, transitionRight])
                s.setReward(0)

                # Set reward for Water State
                if i == 4 and j == 2:
                    s.setReward(-10)
                tempStates.append(s)

            # Set Goal State
            else:
                s = State([i, j], 0)
                s.setReward(10)
                tempStates.append(s)

        states.append(tempStates)

    return states
