from random import randint
points = randint(0,101)


if points < 30:
    print("Bad mood")
elif points < 60:
    print("Normal mood")
else:
    print("Good mood")

