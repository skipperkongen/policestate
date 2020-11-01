# Police State

> He who is subjected to a field of visibility, and who knows it, assumes responsibility for the constraints of power - Foucault

The Police State is a dystopian set of OpenAI gym environments where the objective, for the agent, is to spot the "criminal" dot in a crowd of dots. The agent observes the position of all dots in a grid environment.

```
                    ▒▒▓▓████████▓▓▓▓░░                  
                    ██████████████████                  
                    ██████████████████                  
                    ██████████████████                  
                    ██████████████████                  
            ▓▓██████████████████████████████▓▓          
                    ▒▒░░  ░░        ▒▒                  
                    ██████▓▓▒▒████████                  
                    ██████▒▒  ████████                  
                      ██▓▓    ▓▓▓▓██                    
              ▓▓▒▒                      ▓▓██            
                ██▓▓              ██████████            
                ██████        ██████████████            
                ████████▒▒    ██████████████            
                ██████████▒▒  ██████████████            
              ▓▓██████████▓▓  ██████████████            
          ▓▓████████████████  ████████████████░░        
      ▓▓████████████████████  ████████████████████      
    ████████████████████████▓▓██████████████████████
```

## Getting started

Dependencies:
- Python 3

*Police State* is based on OpenAI Gym. You can install the package as follows, which will automatically install all dependencies:

```
# Warning: not implemented yet!
pip install policestate
```

Minimal example:

```
import gym
import policestate

env = gym.make('Runny-v0')
env.reset()

done = False
while not done:
    action = env.action_space.sample()
    state, reward, done, _ = env.step(action)
    print(state, reward, done)
```

## Environments

An environment is made up by:
- 64 x 64 grid world
- nine dots (numbered 1-9) that move around the grid, seemingly at random
- one dots that is the criminal *c*. Your job is guess who *c* is.

The movement of the dots depends on the environment.

### State

The state of the environment is a list of dot positions in the grid world. For example, the state [0, 0, 0, 0, 0, 0, 0, 0, 0] means that all dots are currently in the upper left corner, while the state [2021, 0, 0, 0, 0, 0, 0, 0, 0] means that the first dot is somewhere around the middle.

### Actions

The agents's objective is to guess who the criminal is and can take two kinds of actions *a*:

|Action|Semantics|
|-|-|
|0|Do nothing|
|1-9|Guess that the *i*'th dot (*i*=action) is the criminal *c*|

The environment runs for at most T=100 rounds, and ends either if you run out of time (i.e. t = T), or the agent correctly guesses the criminal's identity. at each turn the agent must choose an action *a* with a number between 0-9. The enviroment

### Rewards

The reward is computed as follows, for action *a* and time *t*:

|Case|Description|Reward|
|-|-|-|
|a = 0 ∧ t < T|Agent did nothing|-1|
|t ≥ T|Time ran out|-100|
|a > 0 ∧ a ≠ c|Agent guessed wrong|-50|
|a = c|Agent guessed who the criminal is|100|

### Criminal's behaviour

The criminal's behavour depends on the environment. The different environments are listed below.

|Environment name|Criminal behaviour|
|-|-|
|Runny-v0|The criminal runs away from the others|
|Stoppy-v0|The criminal stops near the others|
|Stalky-v0|The criminal follows the others|
|Robby-v0|The criminal runs to and away from others|
|Thiefy-v0|The criminal visits "houses" while others are at "work|"
|Drunky-v0|The criminal walks in a wavy pattern|
|Randy-v0|The criminal randomly chooses one behavior|
|Shifty-v0|The criminal randomly shifts between all behaviours|


## Credits

Ascii art from [textart.sh/topic/spy](https://textart.sh/topic/spy).
