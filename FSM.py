class FiniteStateMachine():
    def __init__(self):
        self.delta = {():''}
    
    def setTransition(self, currentState, input, nextSate):
        self.delta.update({(currentState, input) : nextSate})
    
    def getState(self, currentState, input):
        return self.delta[(currentState, input)]
    
