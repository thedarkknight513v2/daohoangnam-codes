dictionary_games = {
    "1": "PES 17",
    "2": "Uncharted 4",
    "3": "FIFA 17",
    "4": "The witcher 3",
    "5": "Horizon zero dawn",
    "6": "GTA V",
    "7": "Tekken 7"
}

# for index, item in enumerate(dictionary_games):
#     print(*dictionary_games, end =" ")

loop = True

while loop:
    for i in dictionary_games:
        print(i, end ="\t")

    lookup_key = input("What do you want to look up").upper()
    if lookup_key in dictionary_games:
        print("{0} is {1}".format(lookup_key,dictionary_games[lookup_key]))
    else:
        contribute_status = input("There is no such word. Do you want to contribute(Y/N)").upper()
        if contribute_status == "YES":
            new_word_meaning = input("Please define the meaning")
            dictionary_games[lookup_key]= new_word_meaning
            print("Updated. Thank you")
        elif contribute_status == "NO":
            print("bye")
            loop = False
        else:
            print("ZZZz")