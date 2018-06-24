import pyexcel
list_1 = [
{"a": "b"},
{"b": "c"}
]
print(type(list_1))

pyexcel.saveas(records = list_1, dest_file_name = "final.xlsx")

