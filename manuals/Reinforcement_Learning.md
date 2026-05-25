Reinforcement Learning

Convertito da: Reinforcement_Learning.pdf

Reinforcement Learning
| 1

Reinforcement Learning
It is an action selection technique, used when you can tell if
something went right or wrong when applying a certain solution,
but it’s hard (or impossible) to say what the best solution is.

Reinforcement Learning – main concepts
An acting agent is situated in an environment.
- State (s): the current situation of agent and environment.
- Action (a): it’s performed by the agent to change its state.
- Policy (Q): the strategy according to which the agent selects actions.
- Reward (r): the outcome of the chosen action, also negative (penalty).

Reinforcement Learning – sequence of events
1. The agent observes the state s
2. The agent selects an action a according to state s and policy Q(s, a).
3. The agent receives a reward r for its action.
4. The chosen action changes the state s’.
5. The policy is updated according to the action outcome Q’(s, a).

Reinforcement Learning – example
Agent: a robot manipulator.
State: an object to grasp, its position in the environment.
Actions: the possible positions of the gripper on the object.
Policy: how to place the gripper according to the target object.
1. The agent observes the object and consults the policy.
2. The agent selects a gripper configuration on the object.
3. The agent performs the selected action, and observes the outcome:
- The object is lifted successfully, the agent receives a reward.
- The object is NOT lifted successfully, the agent receives a penalty. 4. The policy is updated:
- If there was a reward, the last choice is reinforced, and will be more likely next time.
- If there was a penalty, the last choice is modified, in favour of alternative options.

The basic algorithm: Q learning
s, a, r; s’
1. Select action a based on s, Q(s, a), ε
2. Receive reward r based on selected action a
3. Environment updates state s’ according to s, a
4. Update the policy Q’(s, a) according to r, γ, α, Q(s, a)
5. Repeat from state s’ until a terminal state is reached

α – step size, or learning rate
γ – discount rate for future reward
ε – exploration coefficient

Q-table

|         | Action 1 | Action 2 | Action j |
| ------- | -------- | -------- | -------- |
| State 1 | Value 11 | Value 12 | Value 1j |
| State 2 | Value 21 | Value 22 | Value 2j |
| State i | Value i1 | Value i2 | Value ij |

1. Action selection

Select action with highest value from current state with probability (1-ε):
a = arg_max
a
(Q(s, a))
Select a random action with probability ε
Setting ε = 1 will make algorithm always explore and not converge
Setting ε = 0 (greedy) will make algorithm quickly settle on a policy (often non optimal)
Gradually decreasing ε is often a good solution

2. Receive reward

The reward r is provided by the environment.
r depends on s and a and is usually hard-coded at the beginning, as part of the problem
definition.
r values can be saved in a look-up table or as a function.

3. State update

s’ depends on s and a and depends on the environment.
It can be hard-coded initially as part of the problem definition.
There may be a probabilistic component to it.

4. Policy update

Q’(s, a) = (1-α) Q(s, a) + α (r + γ max
a
(Q(s’, a)))
if α=0, nothing new can be learnt;
if α=1, there’s no memory of previous experience;
It’s common to have α gradually decreasing.
γ > 0 takes into account the maximum possible reward from the new state, even if a non
optimal action will be selected;
γ allows to balance current and future (expected) rewards

5. End of learning iteration

The learning epoch, or iteration, finishes when the state s has no further action possibilities
(terminal state).
Another learning epoch will start, using the Q-table learnt so far.
Learning stops when the maximum number of epochs is reached (or when a specific
stopping condition is met)

The curse of dimensionality

|         | Action 1 | Action 2 | Action j |
| ------- | -------- | -------- | -------- |
| State 1 | Value 11 | Value 12 | Value 1j |
| State 2 | Value 21 | Value 22 | Value 2j |
| State i | Value i1 | Value i2 | Value ij |

The number of states and actions can become very large very quickly.
E.g. imagine that we have 5 cards and need to choose one to play.
The states represented by a hand of 5 cards are: 135 = 371293, the
possible actions 13, so the table would have 136 = 4826809 values.
How can we learn such a huge Q-table?

Deep Reinforcement Learning
state
descriptors
actions
For the previous example, this is a
classifier with 5 inputs and 13 classes:
we can learn that!
Join RL and ANN

DQN – Deep Q learning
o
Neural network for learning the policy Q
 Able to learn much larger spaces
 Approximate and fills missing experiences
 The use of CNN allow to employ very complex states (e.g. images)
o
Experience replay
 Memorise experiences (states, actions, rewards) and replays them randomly for learning
 Avoid correlated sequences
 Can learn again from the same data
o
Fixed Q-Targets
 There are two neural networks for the policy Q
 One is updated at each step, the other less frequently
 The fixed network is used for action selection to avoid oscillations

PPO - Proximal Policy Optimization
o
Based on Actor-critic architecture
 The Actor choses the actions and learns the policy
 The Critic evaluates the outcomes and learns the values of states
 The Critic provides feedback to the Actor
o
Clipped policy gradient
 Best policy improvement by the Actor
 Limited by the Critic to avoid too large updates