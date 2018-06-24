person = ["Quy", 20, 0 ,"Vinh Phuc", 2, ["Manga", "Coding"], 3, 20]

#dictionary
person = {
    "name": "Quy",
    "age": 20,
    "ex": 0,
    "fav": ["Manga", "Coding"]
}
print(person)


# truy cuu theo key >>> CREATE
name = person["name"]
print(name)
fav = person["fav"]
print(fav)

# them phan tu vao list >>> update. Khac CREATE la luc create thi chua co key
# UPDATE

person["length"] = 20
print(person)

person["length"] = 10
print(person)

# person.pop("fav")
# DELETE
del person["length"]
print(person)


# Kiem tra 1 item co trong list hay khong
key = "length"
age = "age"
if age in person:
    print(person["age"])
else:
    print("Not found")

# Print item in list: duyet key
for k in person:
    print(k, person[k])

for u,v in person.items():
    print(u,v)

for value in person.values():
    print(value)

