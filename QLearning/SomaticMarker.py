
class SomaticMarker:
    
    def __init__ (self, up_threshold, down_threshold):
        self._somaticMemory = {}
        self._up_threshold = up_threshold
        self._down_threshold = down_threshold


    def searchState(self, st):
        ret = {}
        for key in self._somaticMemory:
            if key[0] == st:
                ret[key[1]] = self._somaticMemory[key]

        return ret

    def learning(self,state,action,reward):
        if reward >= self._up_threshold or reward <= self._down_threshold:
            self._somaticMemory[(state,action)] = reward

    def getSomaticMemory(self):
        return self._somaticMemory