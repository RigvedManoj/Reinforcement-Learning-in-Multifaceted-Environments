# RLBasics

This application is used to simulate an Agent-Environment Interaction.

## Code Structure:

- State.py : Contains State Definition including policy, transition, rewards and getNextState.
- Environment.py : Defines objects of State (all 23 states and 2 obstacles).
- ValueIteration.py : Contains the value iteration algorithm to find optimal policy.
- Episode.py : Runs one episode.
- TDFunctions.py: Contains TD estimation, SARSA and QLearning Functions.
- CommonFunctions.py: Contains a few necessary common functions.
- Q1.py : Runs Experiment given in Question 1. 
- Q2AB.py : Runs Experiment given in Question 2A and 2B.
- Q2C.py : Runs Experiment given in Question 2C.
- Q3AB.py : Runs Experiment given in Question 3A and 3B.
- Q3C.py : Runs Experiment given in Question 3C.

## Setup:

- Requires python3 to be installed. 
- Python version used to test is Python 3.11.5
- Command: python Q1.py
- Command: python Q2AB.py
- Command: python Q2C.py
- Command: python Q3AB.py
- Command: python Q3C.py
