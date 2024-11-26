import gymnasium as gym
import numpy as np
import random

# Agente para o Frozenlake que considera as recompensas:
# 1  - se atingir o objetivo
# -1 - se cair no buraco
# 0  - para os demais casos

class Agent2:

    def __init__ (self, env:gym.Env):
        self._env = env
        self._qtable = np.zeros((env.observation_space.n, env.action_space.n))
        self.reset()    

    def setEnv(self, env:gym.Env):
        self._env = env
        self.reset()

    def setTraningMode(self, t:bool, learning_rate = 0.7, gamma = 0.95):
        self._trainingMode = t
        self._learning_rate = learning_rate
        self._gamma = gamma

    def step(self, epsilon = 0.0):
        if self._trainingMode:
            action = self._epsilon_greedy_policy(epsilon)
        else:
            action = self._greedy_policy()

        new_state, reward, done, trunc, _ = self._env.step(action)

        #if hole, punish
        if reward == 0 and done == True:
            reward = -1

        if self._trainingMode:
            #Bellman equation ( Q-learning TD - Temporal-difference)
            self._qtable[self._state,action] = self._qtable[self._state,action] + self._learning_rate * (reward + self._gamma * np.max(self._qtable[new_state,:]) - self._qtable[self._state,action])        
        
        self._done = done or trunc

        self._state = new_state
        self._total_reward += reward
        return reward


    def reset(self):
        self._state = self._env.reset()[0]
        self._done = False
        self._total_reward = 0.0

    def done(self):
        return self._done

    def totalReward(self):
        return self._total_reward

    def _greedy_policy(self):
        action = np.argmax(self._qtable[self._state,:])
        return action

    def _epsilon_greedy_policy(self, epsilon):
        random_int = random.uniform(0.0,1.0)
        if random_int > epsilon:
            action = self._greedy_policy()
        else:
            action = self._env.action_space.sample()
        return action

    def getQTable(self):
        return self._qtable