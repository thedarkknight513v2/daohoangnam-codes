# pip install pyeexcel
import pyexcel

dictionary = [
     {
        "Name": 'Adam',
        "Age": 28
     },
     {
        "Name": 'Beatrice',
         "Age": 29
     },
     {
         "Name": 'Ceri',
        "Age": 30
     },
    {
        "Name": 'Dean',
         "Age": 26
     }
      ]

pyexcel.save_as(records= dictionary, dest_file_name="dictionary.xlsx")