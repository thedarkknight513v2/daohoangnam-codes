map_sokoban = {  # ok
    "size_x": 5,# ok
    "size_y": 5# ok
}

player = {# ok
    "x": 4,   # ok                 
    "y": 0# ok
}

boxes = [# ok
    {"x": 1, "y": 1},# ok
    {"x": 2, "y": 2},# ok
    {"x": 3, "y": 3}# ok
]

destination= [# ok
    {"x": 2, "y": 1}, # ok
    {"x": 3, "y": 2},# ok
    {"x": 4, "y": 3}# ok
]

playing = True # ok

# Print map

# check
    

while playing: 
    for y in range(map_sokoban["size_y"]): #ok 
        for x in range(map_sokoban["size_x"]): #ok 

            box_is_here = False #ok 
            for box in boxes: #ok 
                if box["x"] == x and box["y"] == y:
                    # print("B ", end ="") #ok 
                    box_is_here = True #ok 

            player_is_here = False #ok
            if x == player["x"] and y == player["y"]: # ok
                # print("P ", end ="") # ok
                player_is_here = True # ok

            destination_is_here = False #ok 
            for dest in destination:#ok 
                if  dest["x"] == x and dest["y"] == y: #ok 
                    destination_is_here = True #ok 

            if player_is_here: #ok
                print("P ", end ="") #ok
            elif box_is_here: #ok
                print("B ", end="") #ok
            # elif box_is_here is not True:  #ok
            elif destination_is_here: #ok
                print("D ", end ="") #ok
            else: #ok
                print("_ ", end ="") #ok

        print() #ok
# _________________________________________________________________________________________________________________________________
### End of print map
    win = True #ok 
    for box in boxes: #ok 
        if box not in destination: #ok 
            win = False #ok 

    if win is True: #ok 
        print("You will") #ok 
        playing = False #ok 
        
#_____________________________________________________________________________________________________________________________________
    move = input("Your move: ").upper() # ok
#Move ban cach update toa do player # ok
    dx = 0 # khoang player di chuyen # ok
    dy = 0 # khoang player di chuyen # ok
    # Neu di chuyen duoc: toa do moi bang player[x] + dx, player[y] + dy # ok
# 0<= player[x] + dx < 5 # ok
# 0<= player[y] + dy < 5 # ok


    if move == "W":  # ok
        print("Up") # ok
        # player["y"] -= 1 # ok
        dy = -1 # ok
    elif move == "S": # ok
        print("Down") # ok
        # player["y"] += 1 # ok
        dy = 1 # ok
    elif move =="A": # ok
        print("Left") # ok
        # player["x"] -= 1 # ok
        dx = -1 # ok
    elif move == "D": # ok
        print("Right") # ok
        # player["x"] += 1 # ok
        dx = 1 # ok
    else: # ok
        playing = False # ok

 # dung \ de the hien cung 1 dong lenh #ok
    if 0 <= player["x"] + dx < map_sokoban["size_x"] and 0 <= player["y"] + dy < map_sokoban["size_y"]: #ok
        player["x"] += dx #ok
        player["y"] += dy #ok

    for boxes in boxes: #ok
        if box["x"] == player["x"] and box["y"] == player["y"]: #ok
            box["x"] += dx #ok
            box["y"] += dy #ok

# Win khi 3 box trung 3 destination
# dam bao boxes da nam trong het destination

    


# Exception:
# ko day duoc box ra ngoai map
# khong day duoc 2 box canh nhau
# map co chuong ngai vat



    

