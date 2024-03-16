class FiniteStateMachine():
    def __init__(self):
        delta = {}
    
    def setTransition(self, currentState, input, nextSate):
        self.delta = {(currentState, input) : nextSate}
    
    def getState(self, currentState, input):
        return self.delta[(currentState, input)]