import gymnasium as gym
import numpy as np
import random
from SomaticMarker import *

# Agente "somático" para Frozenlake considerando as recompensas:
# 1  - chegar ao objetivo
# -1 - cair no buraco
# 0  - demais casos


class Agent3:

    def __init__ (self, env:gym.Env):
        self._env = env
        self._qtable = np.zeros((env.observation_space.n, env.action_space.n))
        self._somaticMarker = SomaticMarker(0.7, -0.7)
        self.reset()    

    def setTraningMode(self, t:bool, learning_rate = 0.7, gamma = 0.95):
        self._trainingMode = t
        self._learning_rate = learning_rate
        self._gamma = gamma

    def step(self, epsilon = 0.0):
        if self._trainingMode:
            action = self._epsilon_greedy_policy(epsilon)
        else:
            action = self._greedy_somatic_policy()

        new_state, reward, done, trunc, _ = self._env.step(action)

        #if hole, punish
        if reward == 0 and done == True:
            reward = -1

        self._somaticMarker.learning(self._state,action,reward)

        if self._trainingMode:
            #Bellman equation (Q-learning TD - Temporal-difference)
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

    def _greedy_somatic_policy(self):

        markers = self._somaticMarker.searchState(self._state)

        actions = self._qtable[self._state,:]

        for key in markers:
            actions[key] = markers[key]

        action = np.argmax(self._qtable[self._state,:])
        return action

    def _epsilon_greedy_policy(self, epsilon):
        random_int = random.uniform(0.0,1.0)
        if random_int > epsilon:
            action = self._greedy_somatic_policy()
        else:
            action = self._env.action_space.sample()
        return action

    def getSomaticMemory(self):
        return self._somaticMarker.getSomaticMemory()

    def getQTable(self):
        return self._qtable