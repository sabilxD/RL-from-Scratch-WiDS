import pprint

bw_mdp = {

    0: {
        "Right": [(1, 0, 0, True)],
        "Left": [(1, 0, 0, True)]
    },

    1: {
        "Right": [(1, 2, 1, True)],
        "Left": [(1, 0, 0, True)]
    },

    2: {
        "Right": [(1, 2, 0, True)],
        "Left": [(1, 2, 0, True)]
    }

}





swf_mdp = {}
for i in range(0, 7):
    if i == 6 or i == 0:
        swf_mdp[i] = {
                    "Right":
                        [(1, i, 0, True)],
                    "Left":
                        [(1, i, 0, True)],
                        }
    else:
        swf_mdp[i] = {
                "Right": [
                    (1 / 2, i+1, int(i+1 == 6), i+1 == 6),
                    (1 / 3, i, 0, False),
                    (1 / 6, i-1, 0, i-1 == 0),
                ],
                "Left": [
                    (1 / 2, i-1, 0, i-1 == 0),
                    (1 / 3, i, 0, False),
                    (1 / 6, i+1, int(i+1 == 6 ), i+1 == 6),
                ]
            }





#TODO Frozen Lake MDP


def t_state(state):
    if state == 5 or state == 7 or state == 11 or state == 12 or state == 15:
        return True
    else:
        return False


def move_up(state):
    if state == 0 or state == 1 or state == 2 or state == 3:
        return state
    else:
        return (state - 4)


def move_down(state):
    if state == 12 or state == 13 or state == 14 or state == 15:
        return state
    else:
        return ( state + 4 )


def move_left(state):
    if state == 0 or state == 4 or state == 8 or state == 12:
        return state
    else:
        return (state-1)


def move_right(state):
    if state == 3 or state == 7 or state == 11 or state == 15:
        return state
    else:
        return (state+1)


def move( state , action):
    possibilities = []
    if action == "Up":
        possibilities = [  (1 / 3 , move_up(state) , int(move_up(state) == 15) , t_state(move_up(state))) ,
                            (1 / 3, move_left(state), int(move_left(state) == 15), t_state(move_left(state))),
                             (1 / 3, move_right(state), int(move_right(state) == 15), t_state(move_right(state)))
                              ]
    if action == "Down":
        possibilities = [  (1 / 3 , move_down(state) , int( move_down(state) == 15 ) , t_state(move_down(state))),
                           (1 / 3, move_left(state), int(move_left(state) == 15), t_state(move_left(state))),
                           (1 / 3, move_right(state), int(move_right(state) == 15), t_state(move_right(state)))
                           ]
    if action == "Right":
        possibilities = [  (1 / 3 , move_right(state) , int(move_right(state) == 15 ) , t_state(move_right(state))),
                           (1 / 3, move_up(state), int(move_up(state) == 15), t_state(move_up(state))),
                           (1 / 3, move_down(state), int(move_down(state) == 15), t_state(move_down(state)))]
    if action == "Left":
        possibilities = [  (1 / 3 , move_left(state) , int( move_left(state) == 15 ) , t_state(move_left(state))),
                           (1 / 3, move_up(state), int(move_up(state) == 15), t_state(move_up(state))),
                           (1 / 3, move_down(state), int(move_down(state) == 15), t_state(move_down(state)))]
    return possibilities


fl_mdp = {}
for state in range(0, 16):
       transitions = {}
       for action in ["Up", "Down", "Right", "Left"]:
                transitions[action] = []
                if t_state(state):
                   transitions[action].append((1.0 , state , 0.0 , True))
                else:
                   transitions[action] = move(state,action)
       fl_mdp[state] = transitions
pprint.pprint(fl_mdp)
