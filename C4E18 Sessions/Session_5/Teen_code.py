dictionary_1 = {
    "hc": "hoc tap",
    "ngta" : "nguoi ta",
    "any": "anh nguoi yeu",
    "pt": "phat trien"
}

for key in dictionary_1:
    print(key, end ="\t")
print()
print("*" * 20)

loop = True

while loop:
    question = input("What do you want to look up")
    if question in dictionary_1:
        answer = dictionary_1[question]
        print("{0} means {1}".format(question,answer))
        print()
    else:
        contribute = input("No such word. Do you want to contribute Yes/No?").upper()
        print()
        if contribute == "YES":
            new_word_meaning = input("Meaning?")
            dictionary_1[question] = new_word_meaning
        elif contribute == "NO":
            print("bye")
            break


 
