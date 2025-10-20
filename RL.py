import numpy as np

x = 0.25
y = 0.25
gamma = 0.9

states = [0, 1, 2, 3]
actions = [0, 1, 2]

actions_dict = {
    0: [1, 2],
    1: [0],
    2: [0],
    3: [0]
}

def connections(state, action):
    if state == 0:
        if action == 1:
            return [1]
        if action == 2:
            return [2]
    elif state == 1:
        return[1, 3]
    elif state == 2:
        return[0, 3]
    elif state == 3:
        return [0]

def P(init_state, final_state, action):
    if action == 0:
        if init_state == 3 and final_state == 0:
            return 1
        elif init_state == 1:
            if final_state == 1:
                return 1 - x
            elif final_state == 3:
                return x
        elif init_state == 2:
            if final_state == 0:
                return 1 - y
            elif final_state == 3:
                return y
        return 0

    elif action == 1:
        if init_state == 0 and final_state == 1:
            return 1
        else:
            return 0

    elif action == 2:
        if init_state == 0 and final_state == 2:
            return 1
        else:
            return 0

def R(state):
    if state == 3:
        return 10
    elif state == 2:
        return 1
    else:
        return 0

Vk = np.zeros(4)
diff = np.ones(4)

while np.any(diff >= 0.0001):
    oldV = Vk.copy()
    for state in states:
        max_sum = 0
        for action in actions_dict[state]:
            total = 0
            for final_state in connections(state, action):
                total += P(state, final_state, action) * Vk[final_state]
            if total > max_sum:
                max_sum = total
        Vk[state] = R(state) + gamma * max_sum
    diff = np.abs(Vk - oldV)

pi = np.zeros(4, dtype=int)
for state in states:
    max_sum = 0
    max_action = 0
    for action in actions_dict[state]:
        total = 0
        for final_state in connections(state, action):
            total += P(state, final_state, action) * Vk[final_state]
        if total > max_sum:
            max_sum = total
            max_action = action
    pi[state] = max_action

print(f"pi: {pi}")
print(f"V: {Vk}")
