from FSM import FiniteStateMachine

def isEven(fsm, initState, finalState, string):
    currentState = initState
    for symbol in string:
       nextState = fsm.getState(currentState, symbol)
       currentState = nextState
    acceptedState = currentState
    if acceptedState == finalState:
        return "SI es aceptada"
    else:
        return "NO es aceptada"

if __name__ == "__main__":

    AFD = FiniteStateMachine()
    AFD.setTransition("q0", "1", "q1")
    AFD.setTransition("q0", "0", "q3")

    AFD.setTransition("q1", "1", "q0")
    AFD.setTransition("q1", "0", "q2")

    AFD.setTransition("q2", "1", "q3")
    AFD.setTransition("q2", "0", "q1")

    AFD.setTransition("q3", "1", "q2")
    AFD.setTransition("q3", "0", "q0")

    print("0011 " + isEven(AFD, "q0", "q0", "0011"))
    print("00 " + isEven(AFD, "q0", "q0", "00"))
    print("001 " + isEven(AFD, "q0", "q0", "001"))
    print("00011 " + isEven(AFD, "q0", "q0", "00011"))
    print("000111 " + isEven(AFD, "q0", "q0", "000111"))
    print("" + isEven(AFD, "q0", "q0", ""))
    


