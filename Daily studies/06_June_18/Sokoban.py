# the initial location
map_sokoban = {
    "x": 5,
    "y": 5
}

player_location = {
    "x": 4,
    "y": 0
}

boxes_location = [
    {"x": 1, "y": 1},
    {"x": 2, "y": 2},
    {"x": 3, "y": 3}
]

destination_location = [
    {"x": 2, "y": 1},
    {"x": 3, "y": 2},
    {"x": 4, "y": 3}
]

playing_status = True

# Draw map
# them while playing vao day nua
while playing_status:
    for y in range(map_sokoban["y"]):
        for x in range(map_sokoban["x"]):

            player_is_here = False
            if x == player_location["x"] and y == player_location["y"]:
                player_is_here = True

            destination_is_here = False
            for destination in destination_location:
                if destination["x"] == x and destination["y"] == y: 
                    destination_is_here = True
            
            box_is_here = False
            for box in boxes_location:
                if box["x"] == x and box["y"] == y:
                    box_is_here = True

            if player_is_here == True:
                print("P ", end =" ")
            elif destination_is_here == True:
                print("D ", end = " ")
            elif box_is_here == True:
                print("B ", end =" ")
            else:
                print("_ ", end =" ")

        print()

    win_status = True
    for box in boxes_location:
        if box not in destination_location:
            win_status = False

    if win_status == True:
        print("You win")
        playing_status = False
        break

    your_move = input("Input your move").upper()
    dx = 0
    dy = 0

    if your_move == "W":
        print("Up")
        dy = -1
    elif your_move == "S":
        print("Down")
        dy = 1
    elif your_move == "A":
        print("Left")
        dx = -1
    elif your_move == "D":
        print("Right")
        dx = 1
    else:
        playing_status = False
        print("Bye")

    if 0 <= player_location["x"] + dx < map_sokoban["x"] and 0 <= player_location["y"] + dy < map_sokoban["y"]:
        player_location["x"] += dx
        player_location["y"] += dy

    for box in boxes_location:
        if box["x"] == player_location["x"] and box["y"] == player_location["y"]:
            box["x"] += dx
            box["y"] += dy


 









