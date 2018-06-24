Letter_number = 1

for Letter in ("Howdy!"):
    if Letter == "w":
        continue
        print("Encounter w, not processed")
    print("Letter ", Letter_number,"is ",Letter)
    Letter_number += 1