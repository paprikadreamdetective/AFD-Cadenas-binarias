from FSM import FiniteStateMachine

if __name__ == "__main__":
    AFD = FiniteStateMachine()
    AFD.setTransition("q0", 1, "q1")
    AFD.setTransition("q0", 0, "q3")
    AFD.setTransition("q1", 1, "q0")
    AFD.setTransition("q1", 0, "q2")
    AFD.setTransition("q2", 1, "q3")
    AFD.setTransition("q2", 0, "q1")
    AFD.setTransition("q3", 1, "q2")
    AFD.setTransition("q3", 0, "q0")


    

