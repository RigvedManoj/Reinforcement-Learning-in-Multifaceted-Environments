# RLBasics

This application is used to simulate an Agent-Environment Interaction.

## Code Structure:

- Agent.py : Agent Class defines current state, reward and function checkEndState
- Dynamics.py : Dynamics Class sets environment dynamics like mass and gravity. It calculates next state given current state and action.
- EvolutionStrategy.py : This class determines optimal theta using ES. It will iteratively determine newer theta's that give better rewards.
- Estimators.py : Set of Estimator Functions that estimates theta rewards and plots them.
- Episode.py : Runs one Episode taking as input theta and m.
- CommonFunctions.py : Contains all helper functions.
- TuneHyperParameters.py : Main function to be run to get optimal hyperParameters.
- SampleHyperParameters.py : Main function to be run to plot few returns with different sets of hyperParameters.

## Setup:

- Requires python3 to be installed. 
- Python version used to test is Python 3.11.5
- Requires numpy, matplotlib and math packages.
- Command: python SampleHyperParameters.py
- Command: python TuneHyperParameters.py
