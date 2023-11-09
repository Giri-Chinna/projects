def v_sum(a, b, c):
    return a + b + c

def set_state(x_state, z_state, val):
    if x_state[val]:
        return 'X'
    return 'O' if z_state[val] else val

def print_broad(x_state,z_state)-> None:
    zero =  set_state(x_state, z_state, 0)
    one = set_state(x_state, z_state, 1) 
    two =  set_state(x_state, z_state, 2) 
    three =  set_state(x_state, z_state, 3) 
    four =  set_state(x_state, z_state, 4)
    five =  set_state(x_state, z_state, 5)
    six =  set_state(x_state, z_state, 6) 
    seven =  set_state(x_state, z_state, 7)
    eigth =  set_state(x_state, z_state, 8) 

    print(f"{zero} | {one} | {two}")
    print("--|---|--")
    print(f"{three} | {four} | {five}")
    print("--|---|--")
    print(f"{six} | {seven} | {eigth}")

def check_win(x_state,z_state):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8],[0,3,6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if v_sum(x_state[win[0]], x_state[win[1]], x_state[win[2]]) == 3:
            print('X wins')
            return 1
        if v_sum(z_state[win[0]], z_state[win[1]], z_state[win[2]]) == 3:
            print('Z wins')
            return 0
    return -1

def check_full(x_state, z_state):
    if sum(x_state) + sum(z_state) == 9:
        print("Match is draw")
        return -1        

if __name__ == "__main__":
    x_state = [0,0,0,0,0,0,0,0,0]
    z_state = [0,0,0,0,0,0,0,0,0]
    turn = 1 # 1 foe X and 0 for O
    print('Welcome to tic tac toe')

    while(True):
        print_broad(x_state,z_state)
        if turn == 1:
            print("X's chance")
            value = int(input("Please enter a value: "))
            if z_state[value] != 1:
                x_state[value] = 1
            else:
                print('Re-enter at different block')
                continue
        else:
            print("Z's chance")
            value = int(input("Please enter a value: "))
            if x_state[value] != 1:
                z_state[value] = 1
            else:
                print('Re-enter at different block')
                continue

        cwin = check_win(x_state, z_state)
        full = check_full(x_state, z_state)
        if cwin != -1 or full == -1:
            print('Match Over')
            print_broad(x_state,z_state)
            break

        turn = 1 - turn