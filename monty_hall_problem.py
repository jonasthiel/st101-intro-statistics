from random import randint

N = 1000

def simulate(N):
    K = 0
    for i in range(N):
        [1, 2, 3]
        correct_door = randint(1,3)
        picked_door = randint(1,3)
        if correct_door == picked_door:
            opened_door = randint(1,3)
            while opened_door == picked_door:
                opened_door = randint(1,3)
        else:
            opened_door = 6 - correct_door - picked_door
        switched_door = 6 - picked_door - opened_door
        if correct_door == switched_door:
            K += 1

    return float(K) / float(N)

print(simulate(N))